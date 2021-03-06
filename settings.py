from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config["participation_fee"]

SESSION_CONFIG_DEFAULTS = {
    "real_world_currency_per_point": 0.00,
    "participation_fee": 0.00,
    "doc": "",
}

SESSION_CONFIGS = [
    {
        "name": "vickrey_auction_k_1",
        "display_name": "Second price auction K=1",
        "num_demo_participants": 2,
        "app_sequence": ["vickrey_auction_k_1", "survey"],
    },
    {
        "name": "vickrey_auction_k_05",
        "display_name": "Second price auction K=0.5",
        "num_demo_participants": 2,
        "app_sequence": ["vickrey_auction_k_05", "survey"],
    },
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = "en-us"

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = "USD"
USE_POINTS = True
POINTS_CUSTOM_NAME = "ECU"

ROOMS = [
    {
        "name": "va_k_1",
        "display_name": "Second price auction K=1",
    },
    {
        "name": "va_k_05",
        "display_name": "Second price auction K=0.5",
    },
]

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
AUTH_LEVEL = environ.get("OTREE_AUTH_LEVEL")

ADMIN_USERNAME = "Federico Christmann"
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")


# OTREE_PRODUCTION just controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') in {None, '', '0'}:
    DEBUG = True
else:
    DEBUG = False

DEMO_PAGE_INTRO_HTML = """Available games in this session."""

# don"t share this with anybody.
SECRET_KEY = "36373810"
