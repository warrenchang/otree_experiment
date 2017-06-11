from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from otreeutils.surveys import create_player_model_for_survey

author = 'Huanren Zhang'

doc = """
Survey questions
"""


class Constants(BaseConstants):
    name_in_url = 'my_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


GENDER_CHOICES = (
    ('female', 'Female'),
    ('male', 'Male'),
    # ('no_answer', 'Prefer not to answer'),
)

YESNO_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
)


# define survey questions per page
# for each page define a page title and a list of questions
# the questions have a field name, a question text (input label), and a field type (model field class)
SURVEY_DEFINITIONS = (
    {
        'page_title': 'Survey Questions - Page 1',
        'survey_fields': [
            ('CFC1', {
                'text': 'My behavior is only influenced by the immediate (i.e., a matter of days or weeks) outcomes of my actions.',
                'field': models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],widget=widgets.RadioSelectHorizontal()),
            }),
            ('CFC2', {
                'text': 'I think that sacrificing now is usually unnecessary since future outcomes can be dealt with at a later time.',
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                                     widget=widgets.RadioSelectHorizontal()),
            }),
            ('CFC3', {
                'text': 'I only act to satisfy immediate concerns, figuring that I will take care of future problems that may occur at a later date.',
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                                     widget=widgets.RadioSelectHorizontal()),
            }),
            ('CFC4', {
                'text': 'Since my day to day work has specific outcomes, it is more important to me than behavior that has distant outcomes.',
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                                     widget=widgets.RadioSelectHorizontal()),
            }),
            ('CFC5', {
                'text': 'When I make a decision, I think about how it might affect me in the future.',
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                                     widget=widgets.RadioSelectHorizontal()),
            }),
        ]
    },
    {
        'page_title': 'Survey Questions - Page 2',
        'survey_fields': [
            ('OCEAN1', {   # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Extraverted, enthusiastic (外向的，热情的)',   # survey question
                'field':  models.PositiveIntegerField(choices=[1,2,3,4,5,6,7],
                                                    widget=widgets.RadioSelectHorizontal()),
            }),
            ('OCEAN2', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Critical, inclined to argue with others (有些挑剔，爱与人争论)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),
            ('OCEAN3', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Dependable, self-disciplined. (然人觉得可靠，自律的)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),
            ('OCEAN4', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Anxious, easily upset. (易于紧张，易于烦乱的)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),
            ('OCEAN5', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'A deep thinker, creative (有深刻思想，有创造力)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),

        ]
    },
    {
        'page_title': 'Survey Questions - Page 2',
        'survey_fields': [
            ('OCEAN6', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Reserved, quiet (矜持的，安静的)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),
            ('OCEAN7', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Sympathetic, warm. （有同情心，热心的)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),
            ('OCEAN8', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Disorganized, careless. (不是很有条理，有点儿粗心的)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),
            ('OCEAN9', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Calm, emotionally stable (冷静的，情绪稳定的)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),
            ('OCEAN10', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Conventional, preferring work that is routine (传统的，喜欢按部就班的工作)',  # survey question
                'field': models.PositiveIntegerField(choices=[1, 2, 3, 4, 5, 6, 7],
                                          widget=widgets.RadioSelectHorizontal()),
            }),

        ]
    },
)

# now dynamically create the Player class from the survey definitions
Player = create_player_model_for_survey('my_survey.models', SURVEY_DEFINITIONS)
