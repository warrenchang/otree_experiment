from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import random

class Waiting(Page):
    # timeout_seconds = 30
    def is_displayed(self):
        return (self.round_number==1)
        # return self.round_number == 1

    def vars_for_template(self):
        return {'debug_mode': self.session.config['debug']}


class BasePage(Page):
    def vars_for_template(self):
        v =  {
            'treatment': self.session.config['treatment'],
            'other_player': self.player.get_partner(),
            # 'num_rounds': Constants.interaction_length[0],
        }
        v.update(self.extra_vars_for_template())
        return v

    def extra_vars_for_template(self):
        return {}


class BaseWaitPage(WaitPage):
    def vars_for_template(self):
        v = {
            'treatment': self.session.config['treatment'],
            'other_player': self.player.get_partner(),
            # 'num_rounds': Constants.interaction_length[0],
        }
        v.update(self.extra_vars_for_template())
        return v

    def extra_vars_for_template(self):
        return {}


class Introduction(BasePage):
    timeout_seconds = 10

    def is_displayed(self):
        if self.player.round_in_interaction == 1:
            print('This is the start of new match')
        return self.player.round_in_interaction == 1
        # return self.round_number == 1

    def vars_for_template(self):
        return {'debug_mode': self.session.config['debug']}


class Decision1(BasePage):
    # timeout_seconds = 30
    form_model = models.Group
    form_fields = ['action1']

    def is_displayed(self):
        return self.player.id_in_group == 1

    def before_next_page(self):
        if self.timeout_happened:
            self.group.action1 = random.choice(['U','M','D'])
        self.player.action = self.group.action1


class Decision2(BasePage):
    # timeout_seconds = 30
    form_model = models.Group
    form_fields = ['action2']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def before_next_page(self):
        if self.timeout_happened:
            self.group.action2 = random.choice(['L','M','R'])
        self.player.action = self.group.action2


class PracticeWaitPage(BaseWaitPage):
    """Waitpage for the practice match that pause to wait for all participants"""
    template_name = 'asymmetric_PD/DecisionWaitPage.html'
    wait_for_all_groups = True

    def is_displayed(self):
        return self.player.interaction_number == 0

    def after_all_players_arrive(self):
        players = self.subsession.get_players()
        print('After all players arrive',players)
        for p in players:
            p.practice()


class DecisionWaitPage(BaseWaitPage):
    template_name = 'asymmetric_PD/DecisionWaitPage.html'
    def is_displayed(self):
         return self.player.interaction_number > 0

    def after_all_players_arrive(self):
        # it only gets executed once
        self.group.interact()
        # print('players have interacted!')


class BeliefStartPage(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        if not ('belief_elicitation' in self.session.config):
            return False
        else:
            return (self.player.interaction_number == 1) & (self.player.round_in_interaction == 1) & self.session.config['belief_elicitation']


class Belief(BasePage):
    # timeout_seconds = 30
    form_model = models.Player
    form_fields = ['belief1','belief2','belief3']

    def is_displayed(self):
        if not ('belief_elicitation' in self.session.config):
            return False
        else:
            return (self.player.interaction_number == 1) & (self.player.round_in_interaction == 1) & self.session.config['belief_elicitation']

    def error_message(self, values):
        num_others = int(len(self.subsession.get_players())/2)
        if values["belief1"] + values["belief2"] + values["belief3"] != num_others:
            return 'The numbers must add up to %d.'%(num_others)

    def extra_vars_for_template(self):
        return {
            'role': self.player.id_in_group,
        }

    def before_next_page(self):
        if self.timeout_happened:
            num_players = len(self.subsession.get_players())
            a1 = round(random.random() * int(num_players/2))
            a2 = round(random.random() * int(num_players/2 - a1))
            a3 =  int(num_players/2 - a1 - a2)
            self.player.belief1 = a1
            self.player.belief2 = a2
            self.player.belief3 = a3



class BeliefWaitPage(WaitPage):
# class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        if not ('belief_elicitation' in self.session.config):
            return False
        else:
            return (self.player.interaction_number == 1) & (self.player.round_in_interaction == 1) & self.session.config[
                'belief_elicitation']

    def after_all_players_arrive(self):
        players = self.subsession.get_players()
        num11 = sum([(p.action == 'L')&(p.id_in_group==2) for p in players])
        num12 = sum([(p.action == 'M')&(p.id_in_group==2) for p in players])
        num13 = sum([(p.action == 'R')&(p.id_in_group==2) for p in players])
        num21 = sum([(p.action == 'U')&(p.id_in_group==1) for p in players])
        num22 = sum([(p.action == 'M')&(p.id_in_group==1) for p in players])
        num23 = sum([(p.action == 'D')&(p.id_in_group==1) for p in players])
        print('Actual numbers: %d,%d,%d; %d,%d,%d'%(num11,num12,num13,num21,num22,num23))

        for p in players:
            if p.id_in_group == 1:
                p.participant.vars['num1'] = num11
                p.participant.vars['num2'] = num12
                p.participant.vars['num3'] = num13
                p.participant.vars['belief1'] = p.belief1
                p.participant.vars['belief2'] = p.belief2
                p.participant.vars['belief3'] = p.belief3
                p.participant.vars['real_payoff_guess'] = (((p.belief1==num11) + (p.belief2==num12) + (p.belief3==num13))
                                                       *Constants.prize_per_guess)

            else:
                p.participant.vars['num1'] = num21
                p.participant.vars['num2'] = num22
                p.participant.vars['num3'] = num23
                p.participant.vars['belief1'] = p.belief1
                p.participant.vars['belief2'] = p.belief2
                p.participant.vars['belief3'] = p.belief3
                p.participant.vars['real_payoff_guess'] = (((p.belief1==num21) + (p.belief2==num22) + (p.belief3==num23))
                                                       *Constants.prize_per_guess)


class Results(BasePage):
    timeout_seconds = 10
    # def get_timeout_seconds(self):
    #     if self.player.treatment == 'reputation':
    #         return None
    #     else:
    #         return 30


class ResultsWaitPage(BaseWaitPage):
# class ResultsWaitPage(WaitPage):
    template_name = 'asymmetric_PD/ResultsWaitPage.html'
    wait_for_all_groups = True

    def is_displayed(self):
        return self.player.interaction_number < 3


class Continuation(BasePage):
    timeout_seconds = 5

    def is_displayed(self):
        print('Continuation: player.round_number %d, subsession.round_number %d, interaction_number %d, round_in_interaction %d'%(
            self.player.round_number,self.subsession.round_number,self.player.interaction_number,self.player.round_in_interaction ))
        return self.player.round_in_interaction != Constants.interaction_length[self.player.interaction_number]

    def extra_vars_for_template(self):
        return {
            'number_generated': Constants.number_sequence[self.player.round_number-1],
        }


class InteractionResults(BasePage):
    timeout_seconds = 30

    def is_displayed(self):
        print('InteractionResults: player.round_number %d, subsession.round_number %d, interaction_number %d, round_in_interaction %d'%(
            self.player.round_number,self.subsession.round_number,self.player.interaction_number,self.player.round_in_interaction ))
        return self.player.round_in_interaction == Constants.interaction_length[self.player.interaction_number]

    def extra_vars_for_template(self):
        return {
            'number_generated': Constants.number_sequence[self.player.round_number-1],
        }


class InteractionWaitPage(BaseWaitPage):
    template_name = 'asymmetric_PD/InteractionWaitPage.html'
    wait_for_all_groups = True

    def is_displayed(self):
        return self.player.round_in_interaction == Constants.interaction_length[self.player.interaction_number]

    def after_all_players_arrive(self):
        if self.round_number == Constants.num_rounds:
            for p in self.subsession.get_players():
                p.participant.vars['payoff_PD'] = sum([this_player.payoff for this_player in p.in_all_rounds()])
                p.participant.vars['real_payoff_PD'] = (p.participant.vars['payoff_PD']
                                                       * self.session.config['real_world_currency_per_point'])
                if ('belief_elicitation' in self.session.config):
                    if self.session.config['belief_elicitation']:
                        p.payoff += (p.participant.vars['real_payoff_guess']
                                 / self.session.config['real_world_currency_per_point'])



    def extra_vars_for_template(self):
        return {
            'number_generated': Constants.number_sequence[self.player.round_number-1],
        }

page_sequence = [
    Waiting,
    Introduction,
    Decision1,
    Decision2,
    PracticeWaitPage,
    DecisionWaitPage,
    BeliefStartPage,
    Belief,
    BeliefWaitPage,
    Results,
    ResultsWaitPage,
    Continuation,
    InteractionResults,
    InteractionWaitPage,
]
