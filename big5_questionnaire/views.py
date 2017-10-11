from . import models
from ._builtin import Page
from .models import Constants
import random


class StartPage(Page):
    pass

# class Page0(Page):
#     form_model = models.Player
#     form_fields = ['gender']
#     def before_next_page(self):
#         if self.timeout_happened:
#             self.player.gender = random.choice(['male','female'])

class Questions(Page):
    form_model = models.Player
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


class CFC(Page):
    form_model = models.Player
    form_fields = ['CFC{}'.format(i) for i in range(1,6)]

    def before_next_page(self):
        if self.timeout_happened:
            self.player.CFC1 = random.choice(range(1,8))
            self.player.CFC2 = random.choice(range(1,8))
            self.player.CFC3 = random.choice(range(1,8))
            self.player.CFC4 = random.choice(range(1,8))
            self.player.CFC5 = random.choice(range(1,8))


class OCEAN(Page):
    form_model = models.Player
    form_fields = ['OCEAN{}'.format(i) for i in range(1, 11)]

    def before_next_page(self):
        if self.timeout_happened:
            self.player.OCEAN1 = random.choice(range(1,8))
            self.player.OCEAN2 = random.choice(range(1,8))
            self.player.OCEAN3 = random.choice(range(1,8))
            self.player.OCEAN4 = random.choice(range(1,8))
            self.player.OCEAN5 = random.choice(range(1,8))
            self.player.OCEAN6 = random.choice(range(1,8))
            self.player.OCEAN7 = random.choice(range(1,8))
            self.player.OCEAN8 = random.choice(range(1,8))
            self.player.OCEAN9 = random.choice(range(1,8))
            self.player.OCEAN10 = random.choice(range(1,8))







page_sequence = [
    # StartPage,
    # Page0,
    Questions,
    CFC,
    OCEAN,
]
