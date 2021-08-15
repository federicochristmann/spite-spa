from ._builtin import Page


class Survey(Page):

    form_model = 'player'
    form_fields = ['name', 'age', 'gender', 'phone', 'bachelor']


class SurveyNotBachelor(Page):
    def is_displayed(self):
        return self.player.bachelor == 0

    form_model = 'player'
    form_fields = ['solidarity', 'envy', 'overbidding']


class SurveyBachelor(Page):
    def is_displayed(self):
        return self.player.bachelor == 1

    form_model = 'player'
    form_fields = ['quantitative_training']


class SurveyNotQuantitativeTraining(Page):
    def is_displayed(self):
        return self.player.quantitative_training == 0

    form_model = 'player'
    form_fields = ['solidarity', 'envy', 'overbidding']


class SurveyQuantitativeTraining(Page):
    def is_displayed(self):
        return self.player.quantitative_training == 1

    form_model = 'player'
    form_fields = ['economics']


class SurveyNotEconomics(Page):
    def is_displayed(self):
        return self.player.economics == 0

    form_model = 'player'
    form_fields = ['solidarity', 'envy', 'overbidding']


class SurveyEconomics(Page):
    def is_displayed(self):
        return self.player.economics == 1

    form_model = 'player'
    form_fields = ['economics_level', 'solidarity', 'envy', 'overbidding']


page_sequence = [
    Survey,
    SurveyNotBachelor,
    SurveyBachelor,
    SurveyNotQuantitativeTraining,
    SurveyQuantitativeTraining,
    SurveyNotEconomics,
    SurveyEconomics
    ]
