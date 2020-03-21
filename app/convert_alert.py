import time


alert_colors = {
    'open': '8C1A1A',
    'closed': '2DC72D'
}


def convert_sd_to_ms(data):

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(data['incident']['started_at'])) \
        if data['incident']['started_at'] else ""
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(data['incident']['ended_at'])) \
        if data['incident']['ended_at'] else ""

    teams_message = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": f"{alert_colors['open'] if data['incident']['state'] == 'open'else alert_colors['closed']}",
        "summary": data["incident"]["condition_name"],
        "sections": [{
            "activityTitle": data["incident"]["condition_name"],
            "activitySubtitle": f'[{data["incident"]["policy_name"]}]({data["incident"]["url"]})',
            "facts": [
                {
                    "name": "Summary",
                    "value": data["incident"]["summary"]
                },
                {
                    "name": "Started at",
                    "value": start_time
                },
                {
                    "name": "Stopped at",
                    "value": end_time
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