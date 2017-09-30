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
            role_SP = 'Proposer'
        else:
            role_SP = 'Responder'

        if participant.vars['decision_SP']==0:
            decision_SP = 'Left'
        else:
            decision_SP = 'Right'

        return {
            # 'redemption_code': participant.label or participant.code,
            'total_payoff': math.ceil(self.participant.payoff_plus_participation_fee()),
            'paying_part': paying_part,
            'decision_number': self.participant.vars['decision_number'],
            'decision_SP': decision_SP,
            'UG_MAO': self.participant.vars['UG_MAO'],
            'UG_offer': self.participant.vars['UG_offer'],
            'role_SP': role_SP,
            'payoff_SP': participant.vars['payoff_SP'],
            'real_payoff_SP': participant.vars['real_payoff_SP'],
            'payoff_PD': participant.vars['payoff_PD'],
            'real_payoff_PD': participant.vars['payoff_PD'].to_real_world_currency(self.session),
            # 'payoff_ravens': participant.vars['payoff_ravens'],
            'participation_fee': self.session.config['participation_fee']
        }

page_sequence = [PaymentInfo]