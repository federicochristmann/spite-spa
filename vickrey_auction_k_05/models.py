from otree.api import *
import random

author = 'Federico Christmann'

doc = '''In this Second price auction, 2 players bid for an object with private values. Each
player can buy a costly signal about their opponent value which is true w.p. K=0.5'''


class Constants(BaseConstants):
    name_in_url = 'second-price-auction'
    players_per_group = 2
    num_rounds = 20
    zero = cu(0)
    min_value = cu(0)
    max_value = cu(100)
    min_cost = cu(5)
    max_cost = cu(25)


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
            if p.signal_purchase == 1:
                p.payoff = - p.signal_cost
                if p.is_winner:
                    p.payoff = (p.private_value - self.second_highest_bid - p.signal_cost)
            else:
                p.payoff = cu(0)
                if p.is_winner:
                    p.payoff = (p.private_value - self.second_highest_bid)


class Player(BasePlayer):
    private_value = models.CurrencyField(
        doc="How much the player values the item, generated randomly"
    )

    signal_cost = models.CurrencyField(
        doc="Cost of the signal of the rival's value, generated randomly"
    )

    signal_purchase = models.BooleanField(
        doc="Decision of buying a signal about the rival's value"
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
        doc="Indicates whether the player is the winner"
    )
