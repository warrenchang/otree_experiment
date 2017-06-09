from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Huanren Zhang'

doc = """
This is an infinitely repeated "Prisoner's Dilemma" with private monitoring.
"""


class Constants(BaseConstants):
    name_in_url = 'prisoners_dilemma'
    players_per_group = 2

    num_rounds = 10  # change num_rounds for testing purpose, but need to make sure that number_sequence

    instructions_template = 'prisoners_dilemma/Instructions.html'

    # payoff for the prisoner's dilemma
    R = 130
    T = 150
    S = 5
    P = 30

    payoff_matrix = {
        'A':
            {
                'A': R,
                'B': S
            },
        'B':
            {
                'A': T,
                'B': P
            }
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def interact(self):
        p1,p2 = self.get_players()
        p1.my_id = p1.participant.id_in_session
        p2.my_id = p2.participant.id_in_session
        p1.partner_id = p2.my_id
        p2.partner_id = p1.my_id

        # first calculate payoff
        p1.other_action = p2.action
        p2.other_action = p1.action
        p1.payoff = (Constants.payoff_matrix[p1.action][p1.other_action])
        p2.payoff = (Constants.payoff_matrix[p2.action][p2.other_action])
        p1.other_payoff = p2.payoff
        p2.other_payoff = p1.payoff

        # print((self.round_number,p1.payoff,p2.payoff))

        p1.cum_payoff = sum([p.payoff for p in p1.in_all_rounds()])
        p2.cum_payoff = sum([p.payoff for p in p2.in_all_rounds()])

        # update payoff for Part I in terms of real currency
        p1.participant.vars['real_payoff_PartI'] = p1.cum_payoff * self.session.config['real_world_currency_per_point']
        p2.participant.vars['real_payoff_PartI'] = p2.cum_payoff * self.session.config['real_world_currency_per_point']

        # print((p1.participant.id_in_session,p1.action,p1.payoff,p1.signal,p2.participant.id_in_session,p2.action,p2.payoff,p2.signal))


class Player(BasePlayer):
    my_id = models.PositiveIntegerField()
    interaction_number = models.PositiveIntegerField()
    round_in_interaction = models.PositiveIntegerField()

    action = models.CharField(
        choices=['A', 'B'],
        doc="""This player's action""",
        widget=widgets.RadioSelect()
    )

    partner_id = models.PositiveIntegerField()
    other_action = models.CharField(choices=['A','B'])

    cum_payoff = models.CurrencyField()

    def get_partner(self):
        return self.get_others_in_group()[0]

