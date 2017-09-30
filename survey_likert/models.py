from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Huanren Zhang'

doc = """
Questions that can be measures by a likert scale (1-7).
"""

GENDER_CHOICES = (
    ('female', 'Female'),
    ('male', 'Male'),
    # ('no_answer', 'Prefer not to answer'),
)

class Constants(BaseConstants):
    name_in_url = 'survey_likert'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    Q1 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name= "In general, I do not like it when others have more spending money than I have."
                                     )
    Q2 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name= "In general, I do not like it when I have more spending money than others."
                                     )
    Q3 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name= "In general, I like cooperating with others as long as we all benefit the same."
                                     )
    Q4 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name= "In general, I do not like cooperating with others if they benefit more."
                                     )
    Q5 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name= "In general, I do not like it when others do better than I do."
                                     )
    Q6 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name= "In general, I do not like it when I do better than others."
                                     )
    Q7 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name= "In general, I am happy if the spending money of another individual increases, even if this implies they have more spending money than I do, as long as my spending money does not decrease."
                                     )
    Q8 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                     verbose_name= "In general, I am happy if the spending money of another individual increases, as long as they do not have more spending money than I do and my spending money does not decrease."
                                     )
