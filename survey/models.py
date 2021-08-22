from otree.api import *

author = 'Federico Christmann'

doc = '''Survey of player's characteristics.'''


class Constants(BaseConstants):
    name_in_url = 'Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(
        doc='''What is your name?'''
    )

    age = models.IntegerField(
        doc='What is your age?',
        min=12, max=100
    )

    gender = models.StringField(
        choices=[[1, 'Female'], [2, 'Male']],
        doc='What is your gender?',
        widget=widgets.RadioSelect
    )

    phone = models.IntegerField(
        doc='''Detail your phone number with the area code (it will be used to give the prize
        to the lottery winner)''',
    )

    bachelor = models.BooleanField(
        doc='''Have you ever studied a bachelor?''',
    )

    quantitative_training = models.BooleanField(
        doc='''If so, did you have a quantitative training during the program (e.g. Chemistry, Engineering, Economics, 
        Maths, Physics)?''',
    )

    economics = models.BooleanField(
        doc='''Have you ever studied Economics?''',
    )

    economics_level = models.StringField(
        choices=[[1, 'I have not finished my Bachelor'], [2, 'I have finished my Bachelor'],
                 [3, 'I have not finished my Master'], [4, 'I have finished my Master'],
                 [5, 'I have not finished my Ph.D.'], [6, 'I have finished my Ph.D.']],
        doc='''If you have studied Economics, Which is your highest acquired level of studies?''',
        widget=widgets.RadioSelect
    )

    solidarity = models.StringField(
        choices=[[5, 'Strongly agree'], [4, 'Mildy agree'], [3, 'Indifferent'], [2, 'Mildly disagree'], [1, 'Strongly disagree']],
        doc='''Indicate to what extent you agree or disagree with the following statement: 
        I do not care about how much money I have, what concerns me is that there are people who have less money than me''',
        widget=widgets.RadioSelect
    )

    envy = models.StringField(
        choices=[[5, 'Strongly agree'], [4, 'Mildy agree'], [3, 'Indifferent'], [2, 'Mildly disagree'], [1, 'Strongly disagree']],
        doc='''Indicate to what extent you agree or disagree with the following statement: 
        I do not care about how much money I have, what concerns me is that there are people who have more money than me''',
        widget=widgets.RadioSelect
    )

    overbidding = models.StringField(
        doc='''In the experiment, have you ever bid above your own value? If you did so, why?''',
    )
