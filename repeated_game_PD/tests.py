from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield (views.Decision, {"action": random.choice(['A','B'])})
        yield (views.Results)
        if (Constants.round_in_interactions[self.subsession.round_number-1] ==
                Constants.interaction_length[Constants.interactions[self.subsession.round_number - 1]-1]):
            yield (views.InteractionResults)

