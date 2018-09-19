from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.subsession.round_number == 1 and (not self.session.config['debug']):
            yield(pages.Introduction)
        yield (pages.Decision, {"action": random.choice(['A','B'])})
        if self.session.config['treatment'] == 'COM':
            yield (pages.Signal, {"message": random.choice(['a','b'])})
        yield (pages.Results)
        if Constants.number_sequence[self.subsession.round_number-1] > 9:
            yield (pages.InteractionResults)
        else:
            yield (pages.Continuation)

