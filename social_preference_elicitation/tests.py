from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        num_participants = len(self.subsession.get_players())
        yield(views.Waiting)
        yield (views.ModifiedUG,
               {
                   "UGchoice0": random.choice([False, True]),
                   "UGchoice1": random.choice([False, True]),
                   "UGchoice2": random.choice([False, True]),
                   "UGchoice3": random.choice([False, True]),
                   "UGchoice4": random.choice([False, True]),
                   "UGchoice5": random.choice([False, True]),
                   "UGchoice6": random.choice([False, True]),
                   "UGchoice7": random.choice([False, True]),
                   "UGchoice8": random.choice([False, True]),
                   "UGchoice9": random.choice([False, True]),
                   "UGchoice10": random.choice([False, True]),
                   "UGchoice11": random.choice([False, True]),
                   "UGchoice12": random.choice([False, True]),
                   "UGchoice13": random.choice([False, True]),
                   "UGchoice14": random.choice([False, True]),
                   "UGchoice15": random.choice([False, True]),
                   "UGchoice16": random.choice([False, True]),
                   "UGchoice17": random.choice([False, True]),
                   "UGchoice18": random.choice([False, True]),
                   "UGchoice19": random.choice([False, True]),
                   "UGchoice20": random.choice([False, True]),
               })
        yield(views.Waiting)
        yield (views.ModifiedDG,
               {
                   "DGchoice0": random.choice([False, True]),
                   "DGchoice1": random.choice([False, True]),
                   "DGchoice2": random.choice([False, True]),
                   "DGchoice3": random.choice([False, True]),
                   "DGchoice4": random.choice([False, True]),
                   "DGchoice5": random.choice([False, True]),
                   "DGchoice6": random.choice([False, True]),
                   "DGchoice7": random.choice([False, True]),
                   "DGchoice8": random.choice([False, True]),
                   "DGchoice9": random.choice([False, True]),
                   "DGchoice10": random.choice([False, True]),
                   "DGchoice11": random.choice([False, True]),
                   "DGchoice12": random.choice([False, True]),
                   "DGchoice13": random.choice([False, True]),
                   "DGchoice14": random.choice([False, True]),
                   "DGchoice15": random.choice([False, True]),
                   "DGchoice16": random.choice([False, True]),
                   "DGchoice17": random.choice([False, True]),
                   "DGchoice18": random.choice([False, True]),
                   "DGchoice19": random.choice([False, True]),
                   "DGchoice20": random.choice([False, True]),
               })
        yield(views.Waiting)
        UG_offer = random.choice(range(0,21))
        yield (views.UltimatumMAO,
               {
                   "UG_MAO": random.choice(range(0,21)),
               })
        yield (views.UltimatumOffer,
               {
                   "UG_offer": UG_offer,
                   "UG_kept": 20 - UG_offer,

               })