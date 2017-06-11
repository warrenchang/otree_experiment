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
    name_in_url = 'big5_survey'
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
            ('gender', {
                'text': 'What is  your gender.',
                'field': models.CharField(choices=GENDER_CHOICES),
            }),
            ('satisfaction1',
             {  # field name (which will also end up in your "Player" class and hence in your output data)
                 'text': 'On a scale from 1 to 5, please indicate, overall, how dissatisfied/satisfied you are with the outcomes of Part I',
                 # survey question
                 'field': models.PositiveIntegerField(
                     choices=[
                         [1, '1. Very dissatisfied'],
                         [2, '2. Moderately dissatisfied'],
                         [3, '3. Neutral'],
                         [4, '4. Moderately satisfied'],
                         [5, '5. Very satisfied']
                     ]),
             }),
            ('satisfaction2',
             {  # field name (which will also end up in your "Player" class and hence in your output data)
                 'text': 'On a scale from 1 to 5, please indicate, overall, how dissatisfied/satisfied you are with the outcomes of Part II',
                 # survey question
                 'field': models.PositiveIntegerField(
                     choices=[
                         [1, '1. Very dissatisfied'],
                         [2, '2. Moderately dissatisfied'],
                         [3, '3. Neutral'],
                         [4, '4. Moderately satisfied'],
                         [5, '5. Very satisfied']
                     ]),
             }),
        ]
    },
)

# now dynamically create the Player class from the survey definitions
Player = create_player_model_for_survey('big5_survey.models', SURVEY_DEFINITIONS)
