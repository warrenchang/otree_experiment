import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
    APPS_DEBUG = False
else:
    DEBUG = True
    APPS_DEBUG = True

# DEBUG = False
# APPS_DEBUG = False

# don't share this with anybody.
SECRET_KEY = 'xbsw&0b==_fg)5#4n)ckwgr1-na%c#z=pmt4+13yr!h-x&s=1p'


DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')
AUTH_LEVEL = 'STUDY'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
ADMIN_PASSWORD = 'econexperiment'


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
# REAL_WORLD_CURRENCY_CODE = 'USD'
REAL_WORLD_CURRENCY_CODE = 'RMB '
REAL_WORLD_CURRENCY_CODE = 'AED '
USE_POINTS = True
# POINTS_CUSTOM_NAME = 'tokens'
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 1

# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree','otreeutils']


# SENTRY_DSN = ''
SENTRY_DSN = 'http://08e879c62c554e08b7b637e7172b5ba7:daa025e5010e414f98c785f2c04a74f9@sentry.otree.org/150'

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

ROOMS = [
    {
        'name': 'ssel_b_side',
        'display_name': 'SSEL B01 - B24',
        'participant_label_file': '_rooms/ssel_b_side.txt',
    },
    {
        'name': '1',
        'display_name': 'Room 1',
        'participant_label_file': '_rooms/room1.txt',
    },
    {
        'name': '2',
        'display_name': 'Room 2',
        'participant_label_file': '_rooms/room2.txt',
    },
]


# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1/120,
    'participation_fee': 0,
    'debug': DEBUG,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
        'name': 'in_class',
        'display_name': "In class experiment",
        'num_demo_participants': 4,
        'real_world_currency_per_point': 1/8,
        'participation_fee': 0,
        'app_sequence': ['pure_coordination','meeting_place','guess_number','repeated_game_PD','coopetition',
                         'repeated_game_randpay','ravens', 'big5_questionnaire', 'payment_simple'
                         ],
    },
    {
        'name': 'in_class_test',
        'display_name': "In class experiment test",
        'num_demo_participants': 10,
        'real_world_currency_per_point': 1/8,
        'participation_fee': 0,
        'app_sequence': ['pure_coordination','meeting_place','guess_number','repeated_game_PD','coopetition',
                         'repeated_game_randpay','ravens', 'payment_simple'
                         ],
    },
    {
        'name': 'asymmetric_PD_test',
        'display_name': "Infinitely repeated asymmetric PD test",
        'num_demo_participants': 20,
        'treatment': 'ASYM',
        # 'debug': False,
        'real_world_currency_per_point': 1 / 40,
        'SP_money_per_point': 1,
        'participation_fee': 30,
        'app_sequence': ['social_preference_elicitation','asymmetric_PD'],
        # 'app_sequence': ['social_preference_elicitation','asymmetric_PD'],
    },
    {
        'name': 'asymmetric_PD_experiment',
        'display_name': "Infinitely repeated asymmetric PD",
        'num_demo_participants': 30,
        'treatment': 'ASYM',
        # 'debug': False,
        'real_world_currency_per_point': 1 / 40,
        'SP_money_per_point': 1,
        'participation_fee': 30,
        'app_sequence': ['social_preference_elicitation','asymmetric_PD','survey_asym_PD','survey_likert', 'payment_info_asym_PD'],
        # 'app_sequence': ['social_preference_elicitation','asymmetric_PD'],
    },
    {
        'name': 'social_preference_elicitation',
        'display_name': "Social Preference Elicitation",
        'num_demo_participants': 4,
        'real_world_currency_per_point': 1 / 8,
        'participation_fee': 0,
        'app_sequence': ['social_preference_elicitation'
                         ],
    },
    {
        'name': 'big5_questionnaire',
        'display_name': "Big5 Questionnaire",
        'num_demo_participants': 1,
        'real_world_currency_per_point': 1 / 8,
        'participation_fee': 0,
        'app_sequence': ['big5_questionnaire'
                         ],
    },
    {
        'name': 'beauty_contest',
        'display_name': "Beauty contest",
        'num_demo_participants': 4,
        'app_sequence': ['pure_coordination'],
    },
    {
        'name': 'meeting_time',
        'display_name': "Meeting time and place",
        'num_demo_participants': 2,
        'debug': DEBUG,
        'app_sequence': ['meeting_place'],
    },
    {
        'name': 'guess_number',
        'display_name': "Guess number",
        'num_demo_participants': 3,
        'debug': DEBUG,
        'app_sequence': ['guess_number'],
    },
    {
        'name': "simple_PD",
        'display_name': "Prisoner's Dilemma 3 treatments",
        'num_demo_participants': 4,
        'treatment': 'random',
        'debug': DEBUG,
        # 'num_rounds': 10,
        'app_sequence': ['repeated_game_PD'],
    },
    {
        'name': "coopetition",
        'display_name': "Coopetition",
        'num_demo_participants': 4,
        'treatment': 'random',
        'num_rounds': 10,
        'app_sequence': ['coopetition'],
    },
    {
        'name': "coordination_games",
        'display_name': "Coordination game 4 matches",
        'num_demo_participants': 4,
        'treatment': 'random',
        # 'num_rounds': 10,
        'app_sequence': ['repeated_game_randpay'],
    },
    {
        'name': 'Raven',
        'display_name': "Raven's progressive matrix",
        'num_demo_participants': 1,
        'app_sequence': ['ravens'],
    },
    {
        'name': 'my_questionnaire',
        'display_name': "Questionnaire",
        'num_demo_participants': 1,
        'debug': DEBUG,
        'app_sequence': ['big5_questionnaire'],
    },
    {
        'name': 'payment_info',
        'display_name': "Payment information",
        'num_demo_participants': 1,
        'debug': DEBUG,
        'app_sequence': ['payment_simple'],
    },
    {
        'name': 'my_survey',
        'display_name': "Survey questions",
        'num_demo_participants': 1,
        'debug': DEBUG,
        'app_sequence': ['my_survey'],
    },
    {
        'name': 'bret',
        'display_name': "Bomb Risk Elicitation Task",
        'num_demo_participants': 1,
        'debug': DEBUG,
        'app_sequence': ['bret'],
    },
    {
        'name': 'PD_communication',
        'display_name': "PD Private Monitoring with Communication",
        'num_demo_participants': 4,
        'treatment': 'COM',
        'debug': DEBUG,
        'continuation_probability': 0.6,
        'num_rounds': 76,
        'app_sequence': ['my_PD_quiz','my_PD_practice90','my_PD90','coordination','my_PD_survey','ravens','investment_task','payment_info'],
    },
    {
        'name': 'PD_public_d60',
        'display_name': "PD Public Monitoring 0.6",
        'num_demo_participants': 4,
        'treatment': 'PBL',
        'debug': DEBUG,
        'continuation_probability': 0.6,
        'num_rounds': 76,
        'app_sequence': ['my_PD_quiz', 'my_PD_practice90', 'my_PD90', 'coordination', 'my_PD_survey', 'ravens',
                         'investment_task', 'payment_info'],
    },
    {
        'name': 'PD_public_d90',
        'display_name': "PD Public Monitoring 0.9",
        'num_demo_participants': 4,
        'treatment': 'PBL',
        'debug': DEBUG,
        'continuation_probability': 0.9,
        'num_rounds': 99,
        'app_sequence': ['my_PD_quiz', 'my_PD_practice90', 'my_PD90', 'coordination', 'my_PD_survey', 'ravens',
                         'investment_task', 'payment_info'],
    },
    {
        'name': 'PD_COM_d90',
        'display_name': "PD Private Monitoring with communication 0.9 ",
        'num_demo_participants': 4,
        'treatment': 'COM',
        'debug': DEBUG,
        'continuation_probability': 0.9,
        'num_rounds': 99,
        'app_sequence': ['my_PD_quiz', 'my_PD_practice90', 'my_PD90', 'coordination', 'my_PD_survey', 'ravens',
                         'investment_task', 'payment_info'],
    },
    {
        'name': 'PD_COM_d90_test',
        'display_name': "PD Private Monitoring with communication 0.9 testing without survey",
        'num_demo_participants': 4,
        'treatment': 'COM',
        'debug': DEBUG,
        'continuation_probability': 0.9,
        'num_rounds': 99,
        'app_sequence': ['my_PD_quiz', 'my_PD_practice90', 'my_PD90', 'coordination', 'ravens',
                         'investment_task', 'payment_info'],
    },
    {
        'name': 'PD_public_d90_test',
        'display_name': "PD Public Monitoring 0.9 testing without survey",
        'num_demo_participants': 4,
        'treatment': 'PBL',
        'debug': DEBUG,
        'continuation_probability': 0.9,
        'num_rounds': 99,
        'app_sequence': ['my_PD_quiz', 'my_PD_practice90', 'my_PD90', 'guess_number', 'ravens',
                         'investment_task', 'payment_info'],
    },
    {
        'name': 'PD_COM_d60',
        'display_name': "PD Private Monitoring with communication 0.6 ",
        'num_demo_participants': 4,
        'treatment': 'COM',
        'debug': DEBUG,
        'continuation_probability': 0.6,
        'num_rounds': 76,
        'app_sequence': ['my_PD_quiz', 'my_PD_practice90', 'my_PD90', 'coordination', 'my_PD_survey', 'ravens',
                         'investment_task', 'payment_info'],
    },
    {
        'name': 'PD_test',
        'display_name': "Repeated prisoner's dilemma_test",
        'num_demo_participants': 12,
        'debug': DEBUG,
        'app_sequence': ['my_PD90' ],
    },
    {
        'name': 'PD_practice',
        'display_name': "Practice interaction for repeated prisoner's dilemma",
        'num_demo_participants': 1,
        'app_sequence': ['my_PD_practice90'],
    },
    {
        'name': 'PD_with_practice',
        'display_name': "Prisoner's Dilemma with practice interaction",
        'num_demo_participants': 4,
        'treatment': 'PBL',
        'debug': DEBUG,
        'app_sequence': ['my_PD_practice90','my_PD90'],
    },
    {
        'name': 'PD_quiz',
        'display_name': "Quiz questions for Prisoner's Dilemma",
        'num_demo_participants': 1,
        'treatment': 'PBL',
        'debug': DEBUG,
        'app_sequence': ['my_PD_quiz', 'my_PD_survey'],
    },

    {
        'name': 'Investment',
        'display_name': "Investment Task for risk preferences",
        'num_demo_participants': 1,
        'app_sequence': ['investment_task'],
    },
    {
        'name': 'Coordination_game',
        'display_name': "Coordination: payoff dominant or risk dominant",
        'num_demo_participants': 4,
        'debug': DEBUG,
        'app_sequence': ['coordination'],
    },
    # {
    #     'name': 'my_survey',
    #     'display_name': "Survey questions for Prisoner's Dilemma",
    #     'num_demo_participants': 1,
    #     'treatment': 'PBL',
    #     'app_sequence': ['my_PD_survey'],
    # },
    {
        'name': 'my_survey_COM',
        'display_name': "PD with communication Survey questions",
        'num_demo_participants': 1,
        'treatment': 'COM',
        'app_sequence': ['my_PD_survey'],
    },
]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
