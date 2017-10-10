from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.player.round_number==1:
            yield(views.Waiting)
        if self.player.round_in_interaction == 1:
            yield(views.Introduction)
        if self.player.id_in_group == 1:
            yield (views.Decision1, {"action1": random.choice(['U','M','D'])})
        else:
            yield (views.Decision2, {"action2": random.choice(['L','M','R'])})
        print('Test: player.round_number %d, subsession.round_number %d, interaction_number %d, round_in_interaction %d'%(
            self.player.round_number,self.subsession.round_number,self.player.interaction_number,self.player.round_in_interaction ))

        if ('belief_round' in self.session.config):
            if (self.player.interaction_number == 1) & (self.player.round_in_interaction == self.session.config['belief_round']):
                print('Now at belief elicitation')
                num_players = len(self.subsession.get_players())
                a1 = round(random.random() * int(num_players / 2))
                a2 = round(random.random() * int(num_players / 2 - a1))
                a3 = int(num_players / 2 - a1 - a2)
                yield (views.Belief, {"belief1": a1, "belief2": a2, "belief3": a3})
        yield (views.Results)
        ## it seems that the round number in the test is added by previous number of "subsessions", so here -1
        ## I believe this is the bug of the bots test
        # num_previous_parts =  self.session.config['parts_before_PD']
        # round_in_interaction = Constants.round_in_interactions[self.player.round_number-1 - num_previous_parts]
        # interaction_number = Constants.interactions[self.player.round_number-1 - num_previous_parts]
        round_in_interaction = Constants.round_in_interactions[self.player.round_number-1]
        interaction_number = Constants.interactions[self.player.round_number-1]
        if round_in_interaction == Constants.interaction_length[interaction_number]:
            yield (views.InteractionResults)
        else:
            yield (views.Continuation)

