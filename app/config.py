import os

from app.exceptions import MissingTeamsWebhookConnector


class Config(object):
    DEBUG = False
    MS_TEAMS_WEBHOOK = "http://localhost:6000/"


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    MS_TEAMS_WEBHOOK = os.getenv("MS_TEAMS_WEBHOOK", "none")
