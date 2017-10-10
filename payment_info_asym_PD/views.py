from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import math


class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.participant
        print(self.participant.vars)
        if participant.vars['paying_game'] == 'MUG':
            paying_part = 'Part I'
        elif participant.vars['paying_game'] == 'MDG':
            paying_part = 'Part II'
        elif participant.vars['paying_game'] == 'UG':
            paying_part = 'Part III'

        if participant.vars['role_SP']==1:
            role_SP = 'Person A (Proposer)'
        else:
            role_SP = 'Person B (Receiver)'

        if participant.vars['decision_SP']==0:
            decision_SP = 'Left'
        else:
            decision_SP = 'Right'

        if ('belief_round' in self.session.config):
            if self.session.config['belief_round']>0: # when there is belief elicitation
                return {
                # 'redemption_code': participant.label or participant.code,
                    'total_payoff': math.ceil(self.participant.payoff_plus_participation_fee()),
                    'paying_part': paying_part,
                    'decision_number': self.participant.vars['decision_number'],
                    'decision_SP': decision_SP,
                    'UG_MAO': self.participant.vars['UG_MAO'],
                    'UG_offer': self.participant.vars['UG_offer'],
                    'role_SP': role_SP,
                    'payoff_SP': participant.vars['payoff_SP_in_points'],
                    'real_payoff_SP': participant.vars['real_payoff_SP'],
                    'payoff_PD': participant.vars['payoff_PD'],
                    'real_payoff_PD': participant.vars['payoff_PD'].to_real_world_currency(self.session),
                    # 'payoff_ravens': participant.vars['payoff_ravens'],
                    'real_payoff_guess':participant.vars['real_payoff_guess'],
                    'belief_round': self.session.config['belief_round'],
                    'num1': participant.vars['num1'],
                    'num2': participant.vars['num2'],
                    'num3': participant.vars['num3'],
                    'belief1': participant.vars['belief1'],
                    'belief2': participant.vars['belief2'],
                    'belief3': participant.vars['belief3'],
                    'participation_fee': self.session.config['participation_fee']
                }
        return {
            # 'redemption_code': participant.label or participant.code,
                'total_payoff': math.ceil(self.participant.payoff_plus_participation_fee()),
                'paying_part': paying_part,
                'decision_number': self.participant.vars['decision_number'],
                'decision_SP': decision_SP,
                'UG_MAO': self.participant.vars['UG_MAO'],
                'UG_offer': self.participant.vars['UG_offer'],
                'role_SP': role_SP,
                'payoff_SP': participant.vars['payoff_SP_in_points'],
                'real_payoff_SP': participant.vars['real_payoff_SP'],
                'payoff_PD': participant.vars['payoff_PD'],
                'real_payoff_PD': participant.vars['payoff_PD'].to_real_world_currency(self.session),
                # 'payoff_ravens': participant.vars['payoff_ravens'],
                'participation_fee': self.session.config['participation_fee']
            }

    def before_next_page(self):
        self.player.real_payoff_PD = self.participant.vars['payoff_PD'].to_real_world_currency(self.session)
        self.player.real_payoff_guess = self.participant.vars['real_payoff_guess']
        self.player.real_payoff_SP = self.participant.vars['real_payoff_SP']
        self.player.participation_fee = self.session.config['participation_fee']
        self.player.role_SP = self.participant.vars['role_SP']
        self.player.decision_SP = self.participant.vars['decision_SP']
        self.player.paying_part = self.participant.vars['paying_game']
        self.player.decision_number = self.participant.vars['decision_number']
        self.player.UG_MAO = self.participant.vars['UG_MAO']
        self.player.UG_offer = self.participant.vars['UG_offer']


class PaymentWaitPage(WaitPage):
    template_name = 'payment_info_asym_PD/PaymentWaitPage.html'

    def vars_for_template(self):
        participant = self.participant
        print(self.participant.vars)
        if participant.vars['paying_game'] == 'MUG':
            paying_part = 'Part I'
        elif participant.vars['paying_game'] == 'MDG':
            paying_part = 'Part II'
        elif participant.vars['paying_game'] == 'UG':
            paying_part = 'Part III'

        if participant.vars['role_SP']==1:
            role_SP = 'Person A (Proposer)'
        else:
            role_SP = 'Person B (Receiver)'

        if participant.vars['decision_SP']==0:
            decision_SP = 'Left'
        else:
            decision_SP = 'Right'

        if ('belief_round' in self.session.config):
            if self.session.config['belief_round']>0: # when there is belief elicitation
                return {
                # 'redemption_code': participant.label or participant.code,
                    'total_payoff': math.ceil(self.participant.payoff_plus_participation_fee()),
                    'paying_part': paying_part,
                    'decision_number': self.participant.vars['decision_number'],
                    'decision_SP': decision_SP,
                    'UG_MAO': self.participant.vars['UG_MAO'],
                    'UG_offer': self.participant.vars['UG_offer'],
                    'role_SP': role_SP,
                    'payoff_SP': participant.vars['payoff_SP_in_points'],
                    'real_payoff_SP': participant.vars['real_payoff_SP'],
                    'payoff_PD': participant.vars['payoff_PD'],
                    'real_payoff_PD': participant.vars['payoff_PD'].to_real_world_currency(self.session),
                    # 'payoff_ravens': participant.vars['payoff_ravens'],
                    'real_payoff_guess':participant.vars['real_payoff_guess'],
                    'belief_round': self.session.config['belief_round'],
                    'num1': participant.vars['num1'],
                    'num2': participant.vars['num2'],
                    'num3': participant.vars['num3'],
                    'belief1': participant.vars['belief1'],
                    'belief2': participant.vars['belief2'],
                    'belief3': participant.vars['belief3'],
                    'participation_fee': self.session.config['participation_fee']
                }
        return {
            # 'redemption_code': participant.label or participant.code,
                'total_payoff': math.ceil(self.participant.payoff_plus_participation_fee()),
                'paying_part': paying_part,
                'decision_number': self.participant.vars['decision_number'],
                'decision_SP': decision_SP,
                'UG_MAO': self.participant.vars['UG_MAO'],
                'UG_offer': self.participant.vars['UG_offer'],
                'role_SP': role_SP,
                'payoff_SP': participant.vars['payoff_SP_in_points'],
                'real_payoff_SP': participant.vars['real_payoff_SP'],
                'payoff_PD': participant.vars['payoff_PD'],
                'real_payoff_PD': participant.vars['payoff_PD'].to_real_world_currency(self.session),
                # 'payoff_ravens': participant.vars['payoff_ravens'],
                'participation_fee': self.session.config['participation_fee']
            }


page_sequence = [
    PaymentInfo,
    PaymentWaitPage
]
