from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class StartPage(Page):
     def is_displayed(self):
         return self.round_number == 1 and (not self.session.config['debug'])

     def before_next_page(self):
         print(('meeting_place:leaving_StartPage',self.participant.vars))


class Decision(Page):
    form_model = models.Player
    form_fields = ['time','place']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.choice = random.randint(1,5)


class DecisionWaitPage(WaitPage):
    template_name = 'meeting_place/DecisionWaitPage.html'
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        for g in self.subsession.get_groups():
            g.interact()
            print('players have interacted!')



class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds




page_sequence = [
    StartPage,
    Decision,
    DecisionWaitPage,
    Results,
]
