from . import models
from ._builtin import Page
from .models import Constants
import random


class StartPage(Page):
    pass

class Page0(Page):
    form_model = models.Player
    form_fields = ['gender']


class Page1(Page):
    form_model = models.Player
    form_fields = ['CFC{}'.format(i) for i in range(1, 6)]


class Page2(Page):
    form_model = models.Player
    form_fields = ['OCEAN{}'.format(i) for i in range(1, 11)]


page_sequence = [
    StartPage,
    Page0,
    Page1,
    Page2,
]
