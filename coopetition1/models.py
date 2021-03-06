from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Huanren Zhang'

doc = """
Coopetition game: trade-off between value co-creation and value appropriation
"""

def get_share(p1,p2):
    if p1==0 and p2 ==0:
        return 1/2
    else:
        return p1/(p1+p2)

class Constants(BaseConstants):
    name_in_url = 'coopetition1'
    instructions_template = 'coopetition1/Instructions.html'
    history_template = 'coopetition1/History.html'
    historyall_template = 'coopetition1/HistoryAllRounds.html'
    otherhistory_template = 'coopetition1/OtherHistory.html'

    # number of rounds in each interaction randomly selected for payments
    # set to non-positive number if all rounds are chosen for payments
    num_paying_rounds = 1

    players_per_group = 2

    interactions = [
        1, 1, 1, 1, 1, 1, 1, 1,
        2, 2, 2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3, 3, 3,
    ]
    round_in_interactions = [
        1, 2, 3, 4, 5, 6, 7, 8,
        1, 2, 3, 4, 5, 6, 7, 8,
        1, 2, 3, 4, 5, 6, 7, 8,
    ]
    interaction_length = [8, 8, 8]

    matching = ['fixed', 'fixed', 'random']
    symmetric = [1, 0, 0]

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
    #
    # interaction_length = [3, 3, 3]
    #
    #


    # interactions = [
    #     1, 1, 1,
    #     2, 2, 2,
    #     3, 3, 3,
    #     4, 4, 4,
    # ]
    # round_in_interactions = [
    #     1, 2, 3,
    #     1, 2, 3,
    #     1, 2, 3,
    #     1, 2, 3,
    # ]
    #
    # interaction_length = [3, 3, 3, 3]

    num_rounds = sum(interaction_length) # change num_rounds for testing purpose, but need to make sure that number_sequence

class Subsession(BaseSubsession):

    def creating_session(self):
        # this is run before the start of every round
        round_in_interaction = Constants.round_in_interactions[self.round_number-1]
        interaction_number = Constants.interactions[self.round_number-1]
        matching = Constants.matching[interaction_number-1]
        symmetric = Constants.symmetric[interaction_number-1]

        # print((interaction_number,round_in_interaction,treatment))

        # setting random paying rounds
        if Constants.num_paying_rounds > 0:
            if round_in_interaction == 1:
                self.session.vars['paying_rounds'] = random.sample(
                    range(1,Constants.interaction_length[interaction_number-1]+1),
                                              Constants.num_paying_rounds)

        if round_in_interaction == 1: # at the start of each interaction, reshuffle group
            self.group_randomly(fixed_id_in_group=True)
        elif matching != 'fixed':
            self.group_randomly(fixed_id_in_group=True)
        else:  # otherwise, group structure is the same as in the previous round
            self.group_like_round(self.round_number-1)

        for p in self.get_players(): # set interaction number and round number
            p.interaction_number = interaction_number
            p.round_in_interaction = round_in_interaction
            p.matching = matching
            p.symmetric = symmetric
            p.paying_round = 1
            p.role = p.id_in_group
            # print((p.participant.id_in_session, p.interaction_number, p.round_in_interaction, p.treatment))
            if Constants.num_paying_rounds > 0 and not (round_in_interaction in self.session.vars['paying_rounds']):
                p.paying_round = 0

        print('Session paying round',self.session.vars['paying_rounds'] )


class Group(BaseGroup):
    def interact(self):
        p1,p2 = self.get_players()
        p1.my_id = p1.participant.id_in_session
        p2.my_id = p2.participant.id_in_session
        p1.partner_id = p2.my_id
        p2.partner_id = p1.my_id

        # first calculate payoff
        p1.other_a1 = p2.a1
        p1.other_a2 = p2.a2
        p1.other_a3 = p2.a3
        p2.other_a1 = p1.a1
        p2.other_a2 = p1.a2
        p2.other_a3 = p1.a3

        p1.pie = round(p1.a1*p2.a1,2)
        p2.pie = p1.pie
        p1.pie_share = round(get_share(p1.a2,p2.a2),2)
        p2.pie_share = round(get_share(p2.a2,p1.a2),2)

        p1.P3_earnings = p1.a3
        p2.P3_earnings = p2.a3

        p1.potential_payoff = p1.pie*p1.pie_share + p1.P3_earnings
        p2.potential_payoff = p2.pie*p2.pie_share + p2.P3_earnings

        p1.other_payoff = p2.potential_payoff
        p2.other_payoff = p1.potential_payoff

        if p1.paying_round == 1:
            p1.payoff = p1.potential_payoff
            p2.payoff = p2.potential_payoff

        p1.cum_payoff = sum([p.payoff for p in p1.in_all_rounds()
                                      if p.interaction_number == p1.interaction_number])
        p2.cum_payoff = sum([p.payoff for p in p2.in_all_rounds()
                             if p.interaction_number == p1.interaction_number])
        # print((self.round_number,p1.payoff,p2.payoff))

        # update payoff for Part I in terms of real currency
        # p1.participant.vars['real_payoff_PartI'] = p1.cum_payoff * self.session.config['real_world_currency_per_point']
        # p2.participant.vars['real_payoff_PartI'] = p2.cum_payoff * self.session.config['real_world_currency_per_point']

        # print((p1.participant.id_in_session,p1.action,p1.payoff,p1.signal,p2.participant.id_in_session,p2.action,p2.payoff,p2.signal))


class Player(BasePlayer):
    my_id = models.PositiveIntegerField()
    matching = models.StringField()
    symmetric = models.PositiveIntegerField()
    interaction_number = models.PositiveIntegerField()
    round_in_interaction = models.PositiveIntegerField()
    paying_round = models.PositiveIntegerField()

    a1 = models.FloatField(min=0, max=20)
    a2 = models.FloatField(min=0, max=20)
    a3 = models.FloatField(min=0, max=20)
    pie = models.FloatField()
    pie_share = models.FloatField(min=0, max=1)
    P3_earnings = models.FloatField()
    potential_payoff = models.CurrencyField()
    cum_payoff = models.CurrencyField()

    partner_id = models.PositiveIntegerField()
    other_a1 = models.FloatField(min=0, max=20)
    other_a2 = models.FloatField(min=0, max=20)
    other_a3 = models.FloatField(min=0, max=20)
    other_payoff = models.CurrencyField()

    def get_partner(self):
        return self.get_others_in_group()[0]

