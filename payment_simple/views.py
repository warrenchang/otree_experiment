from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import math


class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.participant
        print(self.participant.vars)
        return {
            'final_payment': self.participant.payoff_plus_participation_fee(),
            'participation_fee': self.session.config['participation_fee']
        }


page_sequence = [PaymentInfo]
