from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield (views.Page1, {
            "Q1": random.choice(range(1, 8)),
            "Q2": random.choice(range(1, 8)),
            "Q3": random.choice(range(1, 8)),
            "Q4": random.choice(range(1, 8)),
            "Q5": random.choice(range(1, 8)),
            "Q6": random.choice(range(1, 8)),
            "Q7": random.choice(range(1, 8)),
            "Q8": random.choice(range(1, 8)),
        })
        yield (views.Page2, {
            "OCEAN1": random.choice(range(1, 8)),
            "OCEAN2": random.choice(range(1, 8)),
            "OCEAN3": random.choice(range(1, 8)),
            "OCEAN4": random.choice(range(1, 8)),
            "OCEAN5": random.choice(range(1, 8)),
            "OCEAN6": random.choice(range(1, 8)),
            "OCEAN7": random.choice(range(1, 8)),
            "OCEAN8": random.choice(range(1, 8)),
            "OCEAN9": random.choice(range(1, 8)),
            "OCEAN10": random.choice(range(1, 8)),
        })

        yield (views.Page3, {
            "CFC1": random.choice(range(1, 8)),
            "CFC2": random.choice(range(1, 8)),
            "CFC3": random.choice(range(1, 8)),
            "CFC4": random.choice(range(1, 8)),
            "CFC5": random.choice(range(1, 8)),
        })

