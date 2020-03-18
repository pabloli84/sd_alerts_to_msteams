from flask import Flask, request
import requests
import json
import os

from .convert_alert import convert_sd_to_ms
from .exceptions import MissingTeamsWebhookConnector

app = Flask(__name__)
ms_teams_webhook = os.getenv("MS_TEAMS_WEBHOOK", "none")
if ms_teams_webhook == "none":
    raise MissingTeamsWebhookConnector('Missing MS_TEAMS_WEBHOOK variable set.')


# @app.route('/', methods=['POST'])
def send_to_teams(request):
    data = request.get_json(silent=True)
    teams_card = convert_sd_to_ms(data)
    print(data)

    print(teams_card)

    r = requests.post(ms_teams_webhook, json=teams_card)

    print(f'Hook return code: {r.status_code}')

    return "OK"


if __name__ == '__main__':
    app.run()
