from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        a1 = round(random.random() * 5, 1)
        a2 = round(random.random() * 5, 1)
        a3 = 10 - a1 - a2
        yield (pages.Decision, {"a1": a1, "a2":a2, "a3":a3})
        yield (pages.Results)
        if (Constants.round_in_interactions[self.subsession.round_number-1] ==
                Constants.interaction_length[Constants.interactions[self.subsession.round_number - 1]-1]):
            yield (pages.InteractionResults)
