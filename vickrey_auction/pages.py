from ._builtin import Page, WaitPage


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    timeout_seconds = 7.5*60


class Signal(Page):
    form_model = 'player'
    form_fields = ['signal_purchase']

    timeout_seconds = 50


class Bid(Page):
    form_model = 'player'
    form_fields = ['bid_amount']

    timeout_seconds = 50


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    timeout_seconds = 40


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
    form_fields = ['name', 'age', 'gender', 'phone', 'bachelor']


class SurveyNotBachelor(Page):
    def is_displayed(self):
        player = self.player
        return player.bachelor == 0

    form_model = 'player'
    form_fields = ['solidarity', 'envy', 'overbidding']


class SurveyBachelor(Page):
    def is_displayed(self):
        player = self.player
        return player.bachelor == 1

    form_model = 'player'
    form_fields = ['quantitative_training']


class SurveyNotQuantitativeTraining(Page):
    def is_displayed(self):
        player = self.player
        return player.quantitative_training == 0

    form_model = 'player'
    form_fields = ['solidarity', 'envy', 'overbidding']


class SurveyQuantitativeTraining(Page):
    def is_displayed(self):
        player = self.player
        return player.quantitative_training == 1

    form_model = 'player'
    form_fields = ['economics']


class SurveyNotEconomics(Page):
    def is_displayed(self):
        player = self.player
        return player.economics == 0

    form_model = 'player'
    form_fields = ['solidarity', 'envy', 'overbidding']


class SurveyEconomics(Page):
    def is_displayed(self):
        player = self.player
        return player.economics == 1

    form_model = 'player'
    form_fields = ['economics_level', 'solidarity', 'envy', 'overbidding']





page_sequence = [
    Instructions,
    Signal,
    Bid,
    ResultsWaitPage,
    Results,
    TotalResults,
    Survey,
    SurveyNotBachelor,
    SurveyBachelor,
    SurveyNotQuantitativeTraining,
    SurveyQuantitativeTraining,
    SurveyNotEconomics,
    SurveyEconomics
    ]
