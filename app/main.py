from flask import Flask
import requests
import os

from convert_alert import convert_sd_to_ms
from exceptions import MissingTeamsWebhookConnector, AuthKeyNotValid

app = Flask(__name__)
ms_teams_webhook = os.getenv("MS_TEAMS_WEBHOOK", "none")


def send_to_teams(request):
    if ms_teams_webhook == "none":
        raise MissingTeamsWebhookConnector('Missing MS_TEAMS_WEBHOOK variable set.')

    data = request.get_json(silent=True)

    teams_card = convert_sd_to_ms(data)
    print(data)

    print(teams_card)

    r = requests.post(ms_teams_webhook, json=teams_card)

    print(f'Hook return code: {r.status_code}')

    return "OK"


if __name__ == '__main__':
    app.run()
