from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.player.id_in_group == 1:
            yield (views.Decision1, {"action1": random.choice(['U','M','D'])})
        else:
            yield (views.Decision2, {"action2": random.choice(['L','M','R'])})
        yield (views.Results)
        print('Test: player.round_number %d, subsession.round_number %d, interaction_number %d, round_in_interaction %d'%(
            self.player.round_number,self.subsession.round_number,self.player.interaction_number,self.player.round_in_interaction ))
        ## it seems that the round number in the test is added by previous number of "subsessions", so here -1
        ## I believe this is the bug of the bots test
        if ('belief_elicitation' in self.session.config):
            if (self.player.interaction_number == 1) & (self.player.round_in_interaction == 1) & self.session.config['belief_elicitation']:
                a1 = round(random.random() * 5, 1)
                a2 = round(random.random() * 5, 1)
                a3 = 10 - a1 - a2
                yield (views.Belief, {"belief1": a1, "belief2": a2, "belief3": a3})
        num_previous_parts = 1
        round_in_interaction = Constants.round_in_interactions[self.player.round_number-1 - num_previous_parts]
        interaction_number = Constants.interactions[self.player.round_number-1 - num_previous_parts]
        if round_in_interaction == Constants.interaction_length[interaction_number]:
            yield (views.InteractionResults)
        else:
            yield (views.Continuation)

