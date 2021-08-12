from ._builtin import Page, WaitPage


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Signal(Page):
    form_model = 'player'
    form_fields = ['signal_purchase']


class Bid(Page):
    form_model = 'player'
    form_fields = ['bid_amount']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


class TotalResults(Page):
    def is_displayed(self):
        return self.round_number == 20

    def vars_for_template(self):
        total_payoff = sum([p.payoff for p in self.player.in_all_rounds()])

        return {
            "player_in_all_rounds": self.player.in_all_rounds(),
            "total_payoff": total_payoff,
        }


class Survey(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = 'player'
    form_fields = [
        'name', 'age', 'gender', 'phone', 'solidarity', 'envy', 'overbidding', 'bachelor', 'quantitative_training',
        'economics'
        ]


page_sequence = [
    Introduction,
    Signal,
    Bid,
    ResultsWaitPage,
    Results,
    TotalResults,
    Survey
    ]
