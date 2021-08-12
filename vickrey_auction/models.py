from otree.api import *
import random

author = 'Federico Christmann'

doc = '''In this Second price auction, 2 players bid for an object with private values. Each
player can buy a costly signal about their opponent value.'''


class Constants(BaseConstants):
    name_in_url = 'Second-price-auction'
    players_per_group = 2
    num_rounds = 20
    min_value = cu(0)
    max_value = cu(100)
    min_cost = cu(5)
    max_cost = cu(25)
    instructions_template = 'vickrey_auction/Instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.private_value = random.randrange(Constants.min_value, Constants.max_value, 10)
        for p in self.get_players():
            p.signal_cost = random.randrange(Constants.min_cost, Constants.max_cost, 5)
        for p in self.get_players():
            p.signal_value = random.randrange(Constants.min_value, Constants.max_value, 10)
    # randomize to treatments
    #def creating_session(self):
    #    if self.round_number == 1:
    #        for group in self.get_players():
    #            group.treatment_K = random.choices(['0.5', '1'], cum_weights=[3, 4])
    #            print('set treatment to', group.treatment_K)


class Group(BaseGroup):
    highest_bid = models.CurrencyField()
    second_highest_bid = models.CurrencyField()

    def set_payoffs(self):
        players = self.get_players()
        bids = sorted([p.bid_amount for p in players], reverse=True)
        self.highest_bid = bids[0]
        self.second_highest_bid = bids[1]
        players_with_highest_bid = [
            p for p in players
            if p.bid_amount == self.highest_bid
            ]
        # if tie, winner is chosen at random
        winner = random.choice(players_with_highest_bid)
        winner.is_winner = True
        for p in players:
            p.payoff = cu(0)
            if p.is_winner:
                p.payoff = (p.private_value - self.second_highest_bid)


class Player(BasePlayer):
    # Second price auction
    private_value = models.CurrencyField(
        doc="How much the player values the item, generated randomly"
    )

    signal_cost = models.CurrencyField(
        doc="Cost of the signal of the rival's value, generated randomly"
    )

    signal_purchase = models.BooleanField(
        doc="Decision of buying a signal about the rival's value",
    )

    signal_value = models.CurrencyField(
        doc="Signal of the rival's value, which is true wp. K and random wp. 1-K"
    )

    bid_amount = models.CurrencyField(
        min=cu(0), max=cu(1000),
        doc="Amount that the player bids"
    )

    is_winner = models.BooleanField(
        initial=False,
        doc="""Indicates whether the player is the winner"""
    )

    #Survey
    name = models.StringField(
        doc='''What is your name?'''
    )

    age = models.IntegerField(
        doc='What is your age?',
        min=12, max=100
    )

    gender = models.StringField(
        choices=['Female', 'Male'],
        doc='What is your gender?',
        widget=widgets.RadioSelect
    )

    phone = models.IntegerField(
        doc='''Detail your phone number with the area code (it will be used to give the prize
        to the winner)''',
    )

    solidarity = models.StringField(
        choices=[[1, '1 Strongly disagree'], [2, '2 Mildy disagree'], [3, '3 Indifferent'], [4, '4 Mildly agree'], [5, '5 Strongly agree']],
        doc='''Indicate to what extent you agree or disagree with the following statement: 
        I do not care about how much money I have, what concerns me is that there are people who have less money than me''',
        widget=widgets.RadioSelectHorizontal
    )

    envy = models.IntegerField(
        choices=[[1, '1 Strongly disagree'], [2, '2 Mildy disagree'], [3, '3 Indifferent'], [4, '4 Mildly agree'], [5, '5 Strongly agree']],
        doc='''Indicate to what extent you agree or disagree with the following statement: 
        I do not care about how much money I have, what concerns me is that there are people who have more money than me''',
        widget=widgets.RadioSelectHorizontal
    )

    overbidding = models.StringField(
        doc='''Have you ever bid above your own value? If you did that, why?''',
    )

    bachelor = models.BooleanField(
        doc='''Have you ever studied a bachelor?''',
        widget=widgets.RadioSelect
    )

    quantitative_training = models.BooleanField(
        doc='''If so, did you have a quantitative training during the program (e.g. Chemistry, Engineering, Economics, 
        Maths, Physics)?''',
    )

    economics = models.IntegerField(
        choices=[[1, 'Female'], [2, 'Male']],
        doc='''If you have studied Economics, Which is your highest acquired level of studies?''',
        widget=widgets.RadioSelect
    )
