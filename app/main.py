from flask import Flask, request
import requests
import json
import os

from app.convert_alert import convert_sd_to_ms
from app.exceptions import MissingTeamsWebhookConnector, AuthKeyNotValid

app = Flask(__name__)
ms_teams_webhook = os.getenv("MS_TEAMS_WEBHOOK", "none")
if ms_teams_webhook == "none":
    raise MissingTeamsWebhookConnector('Missing MS_TEAMS_WEBHOOK variable set.')


def send_to_teams(request):
    data = request.get_json(silent=True)
    args = request.args

    teams_card = convert_sd_to_ms(data)
    print(data)

    print(teams_card)

    if args['key'] == "94407572d3907543ba4a614b5e723ac2":
        r = requests.post(ms_teams_webhook, json=teams_card)
    else:
        raise AuthKeyNotValid("Please specify valid key in the request")

    print(f'Hook return code: {r.status_code}')

    return "OK"


if __name__ == '__main__':
    app.run()
