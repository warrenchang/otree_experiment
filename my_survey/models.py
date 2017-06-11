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
            ('gender', {
                'text': 'What is  your gender.',
                'field': models.CharField(choices=GENDER_CHOICES),
            }),
        ]
    },
    {
        'page_title': 'Survey Questions - Page 2',
        'survey_fields': [
            ('religion', {   # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'What religion are you?',   # survey question
                'field':  models.CharField(choices=['Muslim',  'Christian', 'Buddhism','Hindu',
                                                    'None','Other','Rather not to say'
                                                    ]),
            }),
        ]
    },
    {
        'page_title': 'Survey Questions - Page 3',
        'survey_fields': [
            ('school_year', {   # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Which year are you at the university?',   # survey question
                'field':  models.CharField(choices=[ '1st year', '2nd year', '3rd year', '4th or more', 'Graduate student'
                                                     ]),
            }),
        ]
    },
    # {
    #     'page_title': 'Survey Questions - Page 4',
    #     'survey_fields': [
    #         ('importance_self',
    #          {  # field name (which will also end up in your "Player" class and hence in your output data)
    #              'text': 'When making your choice in Part I, how important it is to consider how this choice may affect your earnings in this interaction?',
    #              # survey question
    #              'field': models.PositiveIntegerField(
    #                  choices=[
    #                      [1, '1. Very unimportant'],
    #                      [2, '2. Moderately unimportant'],
    #                      [3, '3. Neutral'],
    #                      [4, '4. Moderately important'],
    #                      [5, '5. Very important']
    #                  ]),
    #          }),
    #         ('importance_other',
    #          {  # field name (which will also end up in your "Player" class and hence in your output data)
    #              'text': "When making your choice in Part I, how important it is to consider how this choice may affect the other person's earnings in this interaction?",
    #              # survey question
    #              'field': models.PositiveIntegerField(
    #                  choices=[
    #                      [1, '1. Very unimportant'],
    #                      [2, '2. Moderately unimportant'],
    #                      [3, '3. Neutral'],
    #                      [4, '4. Moderately important'],
    #                      [5, '5. Very important']
    #                  ]),
    #          }),
    #         ('importance_total',
    #          {  # field name (which will also end up in your "Player" class and hence in your output data)
    #              'text': 'When making your choice in Part I, how important it is to consider how this choice may lead to higher total earnings for you and the other person in this interaction?',
    #              # survey question
    #              'field': models.PositiveIntegerField(
    #                  choices=[
    #                      [1, '1. Very unimportant'],
    #                      [2, '2. Moderately unimportant'],
    #                      [3, '3. Neutral'],
    #                      [4, '4. Moderately important'],
    #                      [5, '5. Very important']
    #                  ]),
    #          }),
    #     ]
    # },
    {
        'page_title': 'Survey Questions - Page 4',
        'survey_fields': [
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
            ('strategy1', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Describe your strategy for Part I: How did you make the choice? Did you base your choice on the signal you received? How did you choose the message to send? How did you base your choice on the messages you sent or received.',
            # survey question
                'field': models.TextField(),
            }),
            ('strategy_again1',
             {  # field name (which will also end up in your "Player" class and hence in your output data)
                 'text': 'What would you do differently if you can do Part I again?',
                 'field': models.TextField(),
             }),

        ]
    },
    {
        'page_title': 'Survey Questions - Page 4',
        'survey_fields': [
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
            ('strategy1', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Describe your strategy for Part I: How did you make the choice? Did you base your choice on the signal you received or the other person receive?',
                # survey question
                'field': models.TextField(),
            }),
            ('strategy_again1',
             {  # field name (which will also end up in your "Player" class and hence in your output data)
                 'text': 'What would you do differently if you can do Part I again?',
                 'field': models.TextField(),
             }),

        ]
    },
    {
        'page_title': 'Survey Questions - Page 5',
        'survey_fields': [
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
            ('strategy2', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'Describe your strategy for Part II. How did you make your decision?',
                'field': models.TextField(),
            }),
            ('strategy_again2',
             {  # field name (which will also end up in your "Player" class and hence in your output data)
                 'text': 'What would you do differently if you can do Part II again?',
                 'field': models.TextField(),
             }),

        ]
    },
    {
        'page_title': 'Survey Questions - Page 6',
        'survey_fields': [
            ('difficulty',
             {  # field name (which will also end up in your "Player" class and hence in your output data)
                 'text': 'Do you consider the first two parts of the experiment easy to understand and follow?',
                 'field': models.PositiveIntegerField(
                     choices=[
                         [1, '1. Very easy'],
                         [2, '2. Easy'],
                         [3, '3. Moderate'],
                         [4, '4. Difficult'],
                         [5, '5. Very difficult']
                     ]),
             }),
            ('experiment_like', {  # field name (which will also end up in your "Player" class and hence in your output data)
                'text': 'What you like/dislike about the experiment? Which part is hard to follow?',
                'field': models.TextField(),
            }),

        ]
    },
)

# now dynamically create the Player class from the survey definitions
Player = create_player_model_for_survey('my_survey.models', SURVEY_DEFINITIONS)
