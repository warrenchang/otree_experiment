from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Huanren Zhang'

doc = """
Raven's progressive matrices test measuring cognitive ability
"""


class Constants(BaseConstants):
    name_in_url = 'ravens'
    players_per_group = None
    minutes_given = 10
    payment_per_question = 1
    payment_in_points = 3
    num_rounds = 12
    answer_keys = [4, 2, 2, 1, 2, 7, 3, 5, 2, 5, 6, 4]
    instructions_template = 'ravens/Instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        # this is run before the start of every round
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['payoff_ravens'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField(choices=[1,2,3,4,5,6,7,8])
    ans_correct = models.BooleanField()

