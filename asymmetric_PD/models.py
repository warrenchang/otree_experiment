from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import math

author = 'Huanren Zhang'

doc = """
Infinitely repeated "Prisoner's Dilemma" with three possible actions. Subjects are divided into groups of 10 and
only interact with those in the same group.
"""


class Constants(BaseConstants):
    prize_per_guess = 2 # payment for each correct guess in real currency
    name_in_url = 'asymmetric_PD'
    players_per_group = 2
    cluster_size = 10 ## players only interact with those within the same cluster group

    number_sequence = [
                       10, 14,  8,  8, 12, 20, 14, 20,  4, 18, 15,  5,  9,  6, 11,  2,  4,
                       16,  1, 11, 20,  5,  5,  1, 18, 20, 11, 11, 15,  7, 20, 13, 11, 15,
                       10, 12, 17,  7, 11,  4,  1, 12,  9,  2,  7,  5,  7,  1,  5, 12, 20,
                       13, 10, 20]
    interactions = [
                     1,  1,  1,  1,  1,  1,  2,  2,  3,  3,  4,  4,  4,  4,  4,  4,  4,
                     4,  4,  4,  4,  5,  5,  5,  5,  6,  7,  7,  7,  7,  7,  8,  8,  8,
                     8,  8,  8,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,
                     10, 10, 10]
    round_in_interactions = [
                              1,  2,  3,  4,  5,  6,  1,  2,  1,  2,  1,  2,  3,  4,  5,  6,  7,
                              8,  9, 10, 11,  1,  2,  3,  4,  1,  1,  2,  3,  4,  5,  1,  2,  3,
                              4,  5,  6,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
                              1,  2,  3]
    interaction_length = [ 6,  2,  2, 11,  4,  1,  5,  6, 14,  3]

    ####################################
    # # parameter values for testing purpose, comment these for real experiment
    # number_sequence = [1, 17, 5, 4, 18, 19,]
    # interactions = [
    #     1, 1, 2, 2, 2, 3,
    # ]
    # round_in_interactions = [
    #     1, 2, 1, 2, 3, 1,
    # ]
    #
    # interaction_length = [2, 3, 1]
    # # parameter values for testing purpose, comment these for real experiment
    ####################################

    # interactions = [
    #     1, 1, 1,
    #     2, 2, 2,
    #     3, 3, 3,
    # ]
    # round_in_interactions = [
    #     1, 2, 3,
    #     1, 2, 3,
    #     1, 2, 3,
    # ]
    # interaction_length = [3, 3, 3]

    num_rounds = sum(interaction_length) # change num_rounds for testing purpose, but need to make sure that number_sequence
    P11 = 600;  P12 = 300; P13 = 0
    P21 = 800;  P22 = 475; P23 = 150
    P31 = 1000; P32 = 650; P33 = 300

    P11a = 900;  P12a = 450; P13a = 0
    P21a = 950;  P22a = 550; P23a = 150
    P31a = 1000; P32a = 650; P33a = 300

    payoff_matrix = {
        'ASYM': {
            1:    {
                'U': { 'L': P11a,  'M': P12a, 'R': P13a },
                'M': { 'L': P21a,  'M': P22a, 'R': P23a },
                'D': { 'L': P31a,  'M': P32a, 'R': P33a }
            },
            2: {
                'L': { 'U': P11,  'M': P12, 'D': P13},
                'M': { 'U': P21,  'M': P22, 'D': P23 },
                'R': { 'U': P31,  'M': P32, 'D': P33 }
            },
        },
        'SYM': {
            1: {
                'U': {'L': P11, 'M': P12, 'R': P13},
                'M': {'L': P21, 'M': P22, 'R': P23},
                'D': {'L': P31, 'M': P32, 'R': P33}
            },
            2: {
                'L': {'U': P11, 'M': P12, 'D': P13},
                'M': {'U': P21, 'M': P22, 'D': P23},
                'R': {'U': P31, 'M': P32, 'D': P33}
            },
        }
    }

    instructions_template = 'asymmetric_PD/Instructions.html'
    history_template = 'asymmetric_PD/History.html'
    historyall_template = 'asymmetric_PD/HistoryAllRounds.html'
    otherhistory_template = 'asymmetric_PD/OtherHistory.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        # this is run before the start of every round
        round_in_interaction = Constants.round_in_interactions[self.round_number-1]
        interaction_number = Constants.interactions[self.round_number-1]
        random_number = Constants.number_sequence[self.round_number-1]

        # print((interaction_number,round_in_interaction,treatment))
        for p in self.get_players(): # set interaction number and round number
            if 'treatment' in self.session.config:
                # demo mode
                p.treatment = self.session.config['treatment']
            else:
                # live experiment mode
                p.treatment = 'SYM'
            p.interaction_number = interaction_number
            p.random_number = random_number
            p.round_in_interaction = round_in_interaction
            print((p.participant.id_in_session, p.interaction_number, p.round_in_interaction, p.treatment))

        if round_in_interaction == 1: # at the start of each interaction, reshuffle group
            # self.group_randomly(fixed_id_in_group=True)
            # random shuffle B players to be re-matched with A players
            # note that players are only matched to those within the same group of 10, so we only
            # shuffle within the same group -- only change the 5 B players in each group to complete matching
            matrix = self.get_group_matrix()
            num_clusters = int(math.ceil(len(matrix)*2/Constants.cluster_size))
            shuffle_size = int(Constants.cluster_size/2)
            for i in range(num_clusters):
                if i != num_clusters -1:
                    l = [item[1] for item in matrix][i * shuffle_size:(i + 1) * shuffle_size]
                    random.shuffle(l)
                    for k in range(shuffle_size):
                        matrix[i * shuffle_size + k][1] = l[k]
                else:
                    csize = len(matrix[i * shuffle_size:])
                    l = [item[1] for item in matrix][i * shuffle_size:]
                    random.shuffle(l)
                    for k in range(csize):
                        matrix[i * shuffle_size + k][1] = l[k]
            self.set_group_matrix(matrix)
            print(matrix)

        else:  # otherwise, group structure is the same as in the previous round
            self.group_like_round(self.round_number-1)


class Group(BaseGroup):
    action1 = models.CharField(
        choices=['U', 'M' ,'D'],
        doc="""Row layer's action""",
        widget=widgets.RadioSelect()
    )
    action2 = models.CharField(
        choices= ['L', 'M' ,'R'],
        doc="""Column player's action""",
        widget=widgets.RadioSelectHorizontal()
    )

    def interact(self):
        p1,p2 = self.get_players()
        p1.my_id = p1.participant.id_in_session
        p2.my_id = p2.participant.id_in_session
        p1.partner_id = p2.my_id
        p2.partner_id = p1.my_id

        # first calculate payoff
        if p1.interaction_number == 0: ## practice match, play with the computer with random choices
            p1.other_action = random.choice(['L', 'M', 'R'])
            p2.other_action = random.choice(['U', 'M', 'D'])
        else:
            p1.other_action = p2.action
            p2.other_action = p1.action

        p1.potential_payoff = (Constants.payoff_matrix[p1.treatment][1][p1.action][p1.other_action])
        p2.potential_payoff = (Constants.payoff_matrix[p2.treatment][2][p2.action][p2.other_action])

        if p1.interaction_number == 0: ## practice match, play with the computer with random choices
            p1.other_payoff = (Constants.payoff_matrix[p1.treatment][2][p1.other_action][p1.action])
            p2.other_payoff = (Constants.payoff_matrix[p2.treatment][1][p2.other_action][p2.action])
        else:
            p1.other_payoff = p2.potential_payoff
            p2.other_payoff = p1.potential_payoff
            p1.payoff = p1.potential_payoff
            p2.payoff = p2.potential_payoff

        # print((self.round_number,p1.payoff,p2.payoff))

        p1.cum_payoff = sum([p.potential_payoff for p in p1.in_all_rounds()
                             if p.interaction_number == p1.interaction_number])
        p2.cum_payoff = sum([p.potential_payoff for p in p2.in_all_rounds()
                             if p.interaction_number == p1.interaction_number])
        # print((p1.participant.id_in_session,p1.action,p1.payoff,p1.signal,p2.participant.id_in_session,p2.action,p2.payoff,p2.signal))


class Player(BasePlayer):
    my_id = models.PositiveIntegerField()
    interaction_number = models.IntegerField()
    round_in_interaction = models.PositiveIntegerField()
    treatment = models.CharField()
    action = models.CharField()
    other_action = models.CharField()
    belief1 = models.IntegerField()
    belief2 = models.IntegerField()
    belief3 = models.IntegerField()

    partner_id = models.PositiveIntegerField()
    potential_payoff = models.CurrencyField()
    other_payoff = models.CurrencyField()
    cum_payoff = models.CurrencyField()
    random_number = models.PositiveIntegerField() # the random number generated by the computer to determine the match length

    def get_partner(self):
        return self.get_others_in_group()[0]

    def practice(self):
        """Practice with random decisions made by the computer"""
        self.my_id = self.participant.id_in_session

        # first calculate payoff
        if self.id_in_group == 1:
            self.other_action = random.choice(['L', 'M', 'R'])
            self.potential_payoff = (Constants.payoff_matrix[self.treatment][1][self.action][self.other_action])
            self.other_payoff = (Constants.payoff_matrix[self.treatment][2][self.other_action][self.action])
        else:
            self.other_action = random.choice(['U', 'M', 'D'])
            self.potential_payoff = (Constants.payoff_matrix[self.treatment][2][self.action][self.other_action])
            self.other_payoff = (Constants.payoff_matrix[self.treatment][1][self.other_action][self.action])

        # print((self.round_number,p1.payoff,p2.payoff))
        self.cum_payoff = sum([p.potential_payoff for p in self.in_all_rounds()
                             if p.interaction_number == self.interaction_number])

