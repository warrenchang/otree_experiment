from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Huanren Zhang'

doc = """
Stag-hunt game to measure the tolerance of strategic uncertainty
"""

GENDER_CHOICES = (
    ('female', 'Female'),
    ('male', 'Male'),
    # ('no_answer', 'Prefer not to answer'),
)

class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    gender = models.CharField(choices=GENDER_CHOICES)

    CFC1 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="My behavior is only influenced by the immediate (i.e., a matter of days or weeks) outcomes of my actions"
    )
    CFC2 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="I think that sacrificing now is usually unnecessary since future outcomes can be dealt with at a later time."
                                       )
    CFC3 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="I only act to satisfy immediate concerns, figuring that I will take care of future problems that may occur at a later date."
                                       )
    CFC4 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="Since my day to day work has specific outcomes, it is more important to me than behavior that has distant outcomes."
                                       )
    CFC5 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                       widget=widgets.RadioSelectHorizontal(),
                                       verbose_name="When I make a decision, I think about how it might affect me in the future."
                                       )

    OCEAN1 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Extraverted, enthusiastic (外向的，有热情的)"
                                         )
    OCEAN2 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Critical, inclined to argue with others (善批判的，爱与人争论)"
                                         )
    OCEAN3 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Dependable, self-disciplined (让人觉得可靠，自律的)"
                                         )
    OCEAN4 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Anxious, easily upset. (易焦虑，易烦乱的)"
                                         )
    OCEAN5 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="A deep thinker, creative (有深刻思想，有创造力)"
                                         )
    OCEAN6 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Reserved, quiet (矜持的，安静的)"
                                         )
    OCEAN7 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Sympathetic, warm (有同情心，热心的)"
                                         )
    OCEAN8 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Disorganized, careless (不是很有条理，有点儿粗心的)"
                                         )
    OCEAN9 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Calm, emotionally stable (冷静的，情绪稳定的)"
                                         )
    OCEAN10 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelectHorizontal(),
                                         verbose_name="Conventional, preferring work that is routine (传统的，喜欢按部就班的工作)"
                                         )



