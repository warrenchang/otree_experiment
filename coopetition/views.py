from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random


class BasePage(Page):
    def vars_for_template(self):
        v =  {
            'other_player': self.player.get_partner(),
        }
        v.update(self.extra_vars_for_template())
        return v

    def extra_vars_for_template(self):
        return {}


class BaseWaitPage(WaitPage):
    def vars_for_template(self):
        return {
            'other_player': self.player.get_partner(),
        }

    def extra_vars_for_template(self):
        return {}


class Introduction(BasePage):
    # timeout_seconds = 30

    def is_displayed(self):
        if self.player.round_in_interaction == 1:
            print('This is the start of new match')
        return self.player.round_in_interaction == 1 and (not self.session.config['debug'])
        # return self.round_number == 1


class Decision(BasePage):
    # timeout_seconds = 30
    form_model = models.Player
    form_fields = ['a1','a2','a3']

    def error_message(self, values):
        if values["a1"] + values["a2"] > 10:
            return 'The sum of the numbers cannot be greater than 0.'

        if abs(values["a1"] + values["a2"] + values["a3"] - 10)>0.01:
            a3_value = 10 - values["a1"] - values["a2"]
            return 'The numbers must add up to 10. In order to add up to 10, you need to allocate %.2f to P3'%a3_value

    def before_next_page(self):
        if self.timeout_happened:
            self.player.a1 = round(random.random()*5,2)
            self.player.a2 = round(random.random()*5,2)
            self.player.a3 = round(10 - self.player.a1 - self.player.a2,2)


class DecisionWaitPage(BaseWaitPage):
    template_name = 'coopetition/DecisionWaitPage.html'

    def after_all_players_arrive(self):
        # it only gets executed once
        self.group.interact()
        # print('players have interacted!')


class Results(BasePage):
    timeout_seconds = 45
    # def get_timeout_seconds(self):
    #     if self.player.treatment == 'reputation':
    #         return None
    #     else:
    #         return 30

    def before_next_page(self):
        self.player.cum_payoff = sum([p.payoff for p in self.player.in_all_rounds()
                                      if p.interaction_number == self.player.interaction_number])


# class ResultsWaitPage(BaseWaitPage):
class ResultsWaitPage(WaitPage):
    template_name = 'coopetition/ResultsWaitPage.html'
    wait_for_all_groups = True

    def is_displayed(self):
        return self.player.treatment == 'reputation'



class InteractionResults(BasePage):
    timeout_seconds = 30

    def is_displayed(self):
        return self.player.round_in_interaction == Constants.interaction_length[self.player.interaction_number-1]

    def extra_vars_for_template(self):
        paying_rounds = [p.round_in_interaction for p in self.player.in_all_rounds()
                         if p.interaction_number == self.player.interaction_number and p.paying_round == 1]
        return {
            'paying_round': paying_rounds[0],
        }


class InteractionWaitPage(BaseWaitPage):
    template_name = 'coopetition/InteractionWaitPage.html'
    wait_for_all_groups = True

    def is_displayed(self):
        return self.player.round_in_interaction == Constants.interaction_length[self.player.interaction_number-1]

    def extra_vars_for_template(self):
        paying_rounds = [p.round_in_interaction for p in self.player.in_all_rounds()
                         if p.interaction_number == self.player.interaction_number and p.paying_round == 1]
        return {
            'paying_round': paying_rounds[0],
        }

page_sequence = [
    Introduction,
    Decision,
    DecisionWaitPage,
    Results,
    ResultsWaitPage,
    InteractionResults,
    InteractionWaitPage,
]
