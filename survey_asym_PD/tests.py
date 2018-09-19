from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield(pages.SurveyPage1,
              {'age': 16, 'gender':'male', 'birth_place':'Middle East'}
              )
        yield(pages.SurveyPage2,
              {'religion': random.choice(['Muslim', 'Christian', 'Buddhism','Hindu',
                                                    'None','Other','Rather not to say'
                                                    ]),
               'religion_importance':random.choice([1,2,3,4])
               })
        yield(pages.SurveyPage3,
              {'school_year': random.choice([ '1', '2', '3', '4 or more', 'Graduate student']),
               'major': random.choice(['Economics', 'Management', 'Social Science', 'Science',
                                                   'Engineering', 'Art or Humanity'
                                                   ]),
               'gpa':random.choice([ 'Between 3.5-4', 'Between 3-3.49', 'Between 2.5-2.99',
                                                    'Between 2-2.49', 'Below 2'
                                                    ]),
              })
        yield(pages.SurveyPage4,
              {'strategy': 'Okay.', 'strategy_again':'Strategy'}
              )
        yield(pages.SurveyPage5,
              {'difficulty': 1, 'experiment_like':'What I like or dislike about the experiment'}
              )
