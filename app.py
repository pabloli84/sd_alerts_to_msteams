from flask import Flask, request
import requests
import json

app = Flask(__name__)
ms_teams_webhook = ""

def convert_sd_to_ms(data):
    teams_message = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": "0076D7",
        "summary": data["incident"]["condition_name"],
        "sections": [{
            "activityTitle": data["incident"]["condition_name"],
            "activitySubtitle": data["incident"]["policy_name"],
            "facts": [
                {
                    "name": "Summary",
                    "value": data["incident"]["summary"]
                },
                {
                    "name": "Started",
                    "value": data["incident"]["started_at"]
                },
                {
                    "name": "Status",
                    "value": data["incident"]["state"]
                }
            ],
            "markdown": "true"
        }]
    }

    return teams_message


@app.route('/', methods=['POST'])
def get_webhook():
    data = json.loads(request.data)
    teams_card = convert_sd_to_ms(data)
    print(data)

    print(teams_card)

    r = requests.post(ms_teams_webhook, json=teams_card)

    print(f'Hook return code: {r.status_code}')

    return "OK"


if __name__ == '__main__':
    app.run()
