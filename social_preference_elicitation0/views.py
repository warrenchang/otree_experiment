from . import models
from ._builtin import Page, WaitPage
from ._builtin import Page
from .models import Constants
import random


class Waiting(Page):

    def vars_for_template(self):
        return {'debug_mode': self.session.config['debug']}



class Modified_UG(Page):
    form_model = models.Player
    form_fields = ['UGchoice{}'.format(i) for i in range(0, 21)]
    def vars_for_template(self):
        return {'choice_numbers': range(0, 21)}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.UGchoice0 = random.choice([0, 1])
            self.player.UGchoice1 = random.choice([0, 1])
            self.player.UGchoice2 = random.choice([0, 1])
            self.player.UGchoice3 = random.choice([0, 1])
            self.player.UGchoice4 = random.choice([0, 1])
            self.player.UGchoice5 = random.choice([0, 1])
            self.player.UGchoice6 = random.choice([0, 1])
            self.player.UGchoice7 = random.choice([0, 1])
            self.player.UGchoice8 = random.choice([0, 1])
            self.player.UGchoice9 = random.choice([0, 1])
            self.player.UGchoice10 = random.choice([0, 1])
            self.player.UGchoice11 = random.choice([0, 1])
            self.player.UGchoice12 = random.choice([0, 1])
            self.player.UGchoice13 = random.choice([0, 1])
            self.player.UGchoice14 = random.choice([0, 1])
            self.player.UGchoice15 = random.choice([0, 1])
            self.player.UGchoice16 = random.choice([0, 1])
            self.player.UGchoice17 = random.choice([0, 1])
            self.player.UGchoice18 = random.choice([0, 1])
            self.player.UGchoice19 = random.choice([0, 1])
            self.player.UGchoice20 = random.choice([0, 1])


class Modified_DG(Page):
    form_model = models.Player
    form_fields = ['DGchoice{}'.format(i) for i in range(0, 21)]
    def vars_for_template(self):
        return {'choice_numbers': range(0, 21)}

    def before_next_page(self):
        if self.timeout_happened:
            self.player.DGchoice0 = random.choice([0, 1])
            self.player.DGchoice1 = random.choice([0, 1])
            self.player.DGchoice2 = random.choice([0, 1])
            self.player.DGchoice3 = random.choice([0, 1])
            self.player.DGchoice4 = random.choice([0, 1])
            self.player.DGchoice5 = random.choice([0, 1])
            self.player.DGchoice6 = random.choice([0, 1])
            self.player.DGchoice7 = random.choice([0, 1])
            self.player.DGchoice8 = random.choice([0, 1])
            self.player.DGchoice9 = random.choice([0, 1])
            self.player.DGchoice10 = random.choice([0, 1])
            self.player.DGchoice11 = random.choice([0, 1])
            self.player.DGchoice12 = random.choice([0, 1])
            self.player.DGchoice13 = random.choice([0, 1])
            self.player.DGchoice14 = random.choice([0, 1])
            self.player.DGchoice15 = random.choice([0, 1])
            self.player.DGchoice16 = random.choice([0, 1])
            self.player.DGchoice17 = random.choice([0, 1])
            self.player.DGchoice18 = random.choice([0, 1])
            self.player.DGchoice19 = random.choice([0, 1])
            self.player.DGchoice20 = random.choice([0, 1])


class Ultimatum_offer(Page):
    form_model = models.Player
    form_fields = ['UG_offer','UG_kept']

    def error_message(self, values):
        if values["UG_offer"] + values["UG_kept"] != 20:
            return 'The sum must be 20.'

    def before_next_page(self):
        if self.timeout_happened:
            self.player.UG_offer = round(random.random()*20)
            self.player.UG_kept = 20 - self.player.UG_offer


class UG_wait(WaitPage):
    wait_for_all_groups = True
    pass


class Ultimatum_MAO(Page):
    form_model = models.Player
    form_fields = ['UG_MAO']
    def before_next_page(self):
        if self.timeout_happened:
            self.player.UG_MAO = round(random.random()*20)

class FinalWaitPage(WaitPage):
    # timeout_seconds = 30
    def after_all_players_arrive(self):
        #it only gets executed once
        self.group.interact()
        print('players have interacted!')


page_sequence = [
    Waiting,
    Modified_UG,
    Waiting,
    Modified_DG,
    Waiting,
    Ultimatum_MAO,
    UG_wait,
    Ultimatum_offer,
    FinalWaitPage,
]
