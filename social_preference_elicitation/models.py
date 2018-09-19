from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import math

author = 'Huanren Zhang'

doc = """
Games used to estimate parameters of the Fehr-Schmidt model of inequality aversion """


class Constants(BaseConstants):
    name_in_url = 'sp'
    players_per_group = 2
    cluster_size = 10 ## players only interact with those within the same cluster group
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        # only one game is used for payment
        # first randomly determine which game is used for payment
        self.session.vars['paying_game'] = random.choice(['MUG', 'MDG', 'UG'])
        self.session.vars['decision_number'] = random.choice(range(21))

        players = self.get_players()
        for p in players:
            p.paying_game = self.session.vars['paying_game']
            p.decision_number = self.session.vars['decision_number']
            p.participant.vars['paying_game'] = p.paying_game
            p.participant.vars['decision_number'] = p.decision_number

        # at the start of each round, reshuffle group
        # note that players are only matched to those within the same group of 10, so we only
        # shuffle within the same group
        matrix = self.get_group_matrix()
        print(matrix)
        num_clusters = int(math.ceil(len(matrix)*2/Constants.cluster_size))
        flattened = [item for sublist in matrix for item in sublist]
        for i in range(num_clusters):
            if i != num_clusters - 1:
                l = flattened[i * Constants.cluster_size:(i + 1) * Constants.cluster_size]
                random.shuffle(l)
                flattened[i * Constants.cluster_size:(i + 1) * Constants.cluster_size] = l
            else:
                l = flattened[i * Constants.cluster_size:]
                random.shuffle(l)
                flattened[i * Constants.cluster_size:] = l
        matrix = list(map(list, zip(*[iter(flattened)] * 2)))
        print(matrix)
        self.set_group_matrix(matrix)


class Group(BaseGroup):
    def interact(self):
        p1, p2 = self.get_players()

        ## set the values for participants, used in the payment info
        p1.participant.vars['UG_MAO'] = 0
        p2.participant.vars['UG_MAO'] = 0
        p1.participant.vars['UG_offer'] = 0
        p2.participant.vars['UG_offer'] = 0
        if p1.paying_game == 'MUG':
            exec('p1.decision = p1.UGchoice%d'%p1.decision_number)
            p2.decision = p1.decision
            if p1.decision == 0:
                p1.payoff = 0
                p2.payoff = 0
            else:
                p1.payoff = p1.decision_number
                p2.payoff = 20 - p1.decision_number

        elif p1.paying_game == 'MDG':
            exec('p1.decision = p1.DGchoice%d' % p1.decision_number)
            p2.decision = p1.decision
            if p1.decision == 0:
                p1.payoff = 20
                p2.payoff = 0
            else:
                p1.payoff = p1.decision_number
                p2.payoff = p1.decision_number
        elif p1.paying_game == 'UG':
            p1.participant.vars['UG_MAO'] = p2.UG_MAO
            p2.participant.vars['UG_MAO'] = p2.UG_MAO
            p1.participant.vars['UG_offer'] = p1.UG_offer
            p2.participant.vars['UG_offer'] = p1.UG_offer
            if p1.UG_offer < p2.UG_MAO:
                p1.payoff = 0
                p2.payoff = 0
            else:
                p1.payoff = p1.UG_kept
                p2.payoff = p1.UG_offer

        p1.participant.vars['payoff_SP_in_points'] = p1.payoff
        p2.participant.vars['payoff_SP_in_points'] = p2.payoff
        p1.payoff = p1.payoff * self.session.config['SP_money_per_point'] / self.session.config['real_world_currency_per_point']
        p2.payoff = p2.payoff * self.session.config['SP_money_per_point'] / self.session.config['real_world_currency_per_point']
        p1.participant.vars['decision_SP'] = p1.decision
        p2.participant.vars['decision_SP'] = p1.decision
        p1.participant.vars['role_SP'] = p1.id_in_group
        p2.participant.vars['role_SP'] = p2.id_in_group
        p1.participant.vars['real_payoff_SP'] = p1.payoff.to_real_world_currency(self.session)
        p2.participant.vars['real_payoff_SP'] = p2.payoff.to_real_world_currency(self.session)


class Player(BasePlayer):
    paying_game = models.StringField()
    decision_number = models.IntegerField()
    decision = models.BooleanField()

    DGchoice0 = models.BooleanField()
    DGchoice1 = models.BooleanField()
    DGchoice2 = models.BooleanField()
    DGchoice3 = models.BooleanField()
    DGchoice4 = models.BooleanField()
    DGchoice5 = models.BooleanField()
    DGchoice6 = models.BooleanField()
    DGchoice7 = models.BooleanField()
    DGchoice8 = models.BooleanField()
    DGchoice9 = models.BooleanField()
    DGchoice10 = models.BooleanField()
    DGchoice11 = models.BooleanField()
    DGchoice12 = models.BooleanField()
    DGchoice13 = models.BooleanField()
    DGchoice14 = models.BooleanField()
    DGchoice15 = models.BooleanField()
    DGchoice16 = models.BooleanField()
    DGchoice17 = models.BooleanField()
    DGchoice18 = models.BooleanField()
    DGchoice19 = models.BooleanField()
    DGchoice20 = models.BooleanField()

    UGchoice0 = models.BooleanField()
    UGchoice1 = models.BooleanField()
    UGchoice2 = models.BooleanField()
    UGchoice3 = models.BooleanField()
    UGchoice4 = models.BooleanField()
    UGchoice5 = models.BooleanField()
    UGchoice6 = models.BooleanField()
    UGchoice7 = models.BooleanField()
    UGchoice8 = models.BooleanField()
    UGchoice9 = models.BooleanField()
    UGchoice10 = models.BooleanField()
    UGchoice11 = models.BooleanField()
    UGchoice12 = models.BooleanField()
    UGchoice13 = models.BooleanField()
    UGchoice14 = models.BooleanField()
    UGchoice15 = models.BooleanField()
    UGchoice16 = models.BooleanField()
    UGchoice17 = models.BooleanField()
    UGchoice18 = models.BooleanField()
    UGchoice19 = models.BooleanField()
    UGchoice20 = models.BooleanField()

    UG_offer = models.PositiveIntegerField(min=0, max=20)
    UG_kept = models.PositiveIntegerField(min=0, max=20)
    UG_MAO= models.PositiveIntegerField(min=0, max=20)


