from . import models
from ._builtin import Page
from .models import Constants
import random


class StartPage(Page):
    pass


class Page1(Page):
    form_model = 'player'
    form_fields = ['Q{}'.format(i) for i in range(1, 9)]

    def before_next_page(self):
        if self.timeout_happened:
            self.player.Q1 = random.choice(range(1,8))
            self.player.Q2 = random.choice(range(1,8))
            self.player.Q3 = random.choice(range(1,8))
            self.player.Q4 = random.choice(range(1,8))
            self.player.Q5 = random.choice(range(1,8))
            self.player.Q6 = random.choice(range(1,8))
            self.player.Q7 = random.choice(range(1,8))
            self.player.Q8 = random.choice(range(1,8))


page_sequence = [
    # StartPage,
    Page1,
]
