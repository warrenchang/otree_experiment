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
    name_in_url = 'repeated_game_PD'
    players_per_group = 2

    interactions = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    ]
    round_in_interactions = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    ]
    interaction_length = [10, 10, 10]

    treatments = ['random', 'reputation', 'fixed']


    interactions = [
        1, 1, 1,
        2, 2, 2,
        3, 3, 3,
    ]
    round_in_interactions = [
        1, 2, 3,
        1, 2, 3,
        1, 2, 3,
    ]
    interaction_length = [3, 3, 3]

    num_rounds = sum(interaction_length) # change num_rounds for testing purpose, but need to make sure that number_sequence


    # payoff for the prisoner's dilemma
    R = 2
    S = -2
    T = 4
    P = 0

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

    instructions_template = 'repeated_game_PD/Instructions.html'
    history_template = 'repeated_game_PD/History.html'
    historyall_template = 'repeated_game_PD/HistoryAllRounds.html'
    otherhistory_template = 'repeated_game_PD/OtherHistory.html'


class Subsession(BaseSubsession):

    def before_session_starts(self):
        # this is run before the start of every round
        round_in_interaction = Constants.round_in_interactions[self.round_number-1]
        interaction_number = Constants.interactions[self.round_number-1]
        treatment = Constants.treatments[interaction_number-1]

        print((interaction_number,round_in_interaction,treatment))

        for p in self.get_players(): # set interaction number and round number
            p.interaction_number = interaction_number
            p.round_in_interaction = round_in_interaction
            p.treatment = treatment
            print((p.participant.id_in_session, p.interaction_number, p.round_in_interaction, p.treatment))

        if round_in_interaction == 1: # at the start of each interaction, reshuffle group
            self.group_randomly()
        elif treatment != 'fixed':
            self.group_randomly()
        else:  # otherwise, group structure is the same as in the previous round
            self.group_like_round(self.round_number-1)


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
    treatment = models.CharField()

    action = models.CharField(
        choices=['A', 'B'],
        doc="""This player's action""",
        widget=widgets.RadioSelect()
    )

    partner_id = models.PositiveIntegerField()
    other_action = models.CharField(choices=['A','B'])

    other_payoff = models.CurrencyField()
    cum_payoff = models.CurrencyField()

    def get_partner(self):
        return self.get_others_in_group()[0]

