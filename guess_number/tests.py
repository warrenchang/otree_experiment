from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        yield(views.Guess, {'guess':random.randint(0, 100)})
        yield(views.Results)
        if self.subsession.round_number == Constants.num_rounds:
            yield(views.Payment)

