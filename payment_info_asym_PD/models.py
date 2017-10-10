from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random



author = 'Huanren Zhang'

doc = """
Payment information for the session
"""



class Constants(BaseConstants):
    name_in_url = 'payment_info_asym_PD'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):

    def before_session_starts(self):
        for p in self.get_players():
            p.payoff = 0





class Group(BaseGroup):
    pass


class Player(BasePlayer):
    final_payment  = models.CurrencyField()
    real_payoff_PD  = models.CurrencyField()
    real_payoff_guess  = models.CurrencyField()
    real_payoff_SP  = models.CurrencyField()
    participation_fee  = models.CurrencyField()
    role_SP = models.IntegerField()
    decision_SP = models.IntegerField()
    paying_game = models.CharField()
    decision_number = models.IntegerField()
    UG_MAO = models.IntegerField()
    UG_offer = models.IntegerField()



