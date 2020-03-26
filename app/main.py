import requests

from flask import Flask

from convert_alert import convert_sd_to_ms
from config import *
from exceptions import MissingTeamsWebhookConnector

SD2TEAMS_MODE = os.getenv("SD2TEAMS_MODE", "Dev")

app = Flask(__name__)
if SD2TEAMS_MODE == "Prod":
    app.config.from_object('app.config.ProdConfig')
elif SD2TEAMS_MODE == "Test":
    app.config.from_object('app.config.Config')

teams_webhook = app.config['MS_TEAMS_WEBHOOK']
if teams_webhook == "none":
    raise MissingTeamsWebhookConnector("For real operation mode specify correct MS_TEAMS_WEBHOOK env variable.")


def send_to_teams(request):

    data = request.get_json(silent=True)
    teams_card = convert_sd_to_ms(data)

    app.logger.info("Got message from SD: %s", data)
    app.logger.info("Sending message to Teams: %s", teams_card)

    r = requests.post(teams_webhook, json=teams_card)

    app.logger.info('Hook return code: %s', r.status_code)

    return "OK"


if __name__ == '__main__':
    app.run()
