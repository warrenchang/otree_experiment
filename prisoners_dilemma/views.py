from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random


class BasePage(Page):
    def vars_for_template(self):
        v =  {
            'treatment': self.session.config['treatment'],
        }
        v.update(self.extra_vars_for_template())
        return v

    def extra_vars_for_template(self):
        return {}


class BaseWaitPage(WaitPage):
    def vars_for_template(self):
        return {
            'treatment': self.session.config['treatment'],
        }


class Introduction(BasePage):
    timeout_seconds = 30

    def is_displayed(self):
        if self.round_number == 1:
            print('This is the start of PD')
        return self.round_number == 1 and (not self.session.config['debug'])
        # return self.round_number == 1


class Decision(BasePage):
    # timeout_seconds = 30
    form_model = models.Player
    form_fields = ['action']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.action = random.choice(['A','B'])


class DecisionWaitPage(BaseWaitPage):
    template_name = 'my_PD90/DecisionWaitPage.html'

    def after_all_players_arrive(self):
        # it only gets executed once
        self.group.interact()
        # print('players have interacted!')


class Results(BasePage):
    timeout_seconds = 8


class Continuation(BasePage):
    timeout_seconds = 8

    def is_displayed(self):
        return Constants.number_sequence[self.subsession.round_number-1] <= 6


class InteractionResults(BasePage):
    timeout_seconds = 30

    def is_displayed(self):
        return self.round_number == Constants.num_rounds



page_sequence = [
    Introduction,
    Decision,
    DecisionWaitPage,
    Results,
    InteractionResults,
]
