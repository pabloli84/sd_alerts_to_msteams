import requests
import os

from flask import Flask

from app.convert_alert import convert_sd_to_ms
from app.exceptions import MissingTeamsWebhookConnector

app = Flask(__name__)


def send_to_teams(request):
    ms_teams_webhook = os.getenv("MS_TEAMS_WEBHOOK", "none")

    if ms_teams_webhook == "none":
        raise MissingTeamsWebhookConnector('Missing MS_TEAMS_WEBHOOK variable set.')

    data = request.get_json(silent=True)

    teams_card = convert_sd_to_ms(data)

    app.logger.info("Got message from SD: %s", data)
    app.logger.info("Sending message to Teams: %s", teams_card)

    r = requests.post(ms_teams_webhook, json=teams_card)

    app.logger.info('Hook return code: %s', r.status_code)

    return "OK"


if __name__ == '__main__':
    app.run()
