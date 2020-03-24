import time


alert_colors = {
    'open': '8C1A1A',
    'closed': '2DC72D'
}


def convert_sd_to_ms(data):

    inc_data = data['incident']

    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(inc_data.get('started_at'))) \
        if inc_data.get('started_at') else ""
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(inc_data.get('ended_at'))) \
        if inc_data.get('ended_at') else ""

    teams_message = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": f"{alert_colors['open'] if inc_data.get('state') == 'open'else alert_colors['closed']}",
        "summary": inc_data.get("condition_name"),
        "sections": [{
            "activityTitle": inc_data.get("condition_name"),
            "activitySubtitle": f'[{inc_data.get("policy_name")}]({inc_data.get("url")})',
            "facts": [
                {
                    "name": "Summary",
                    "value": inc_data.get("summary")
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
                    "value": inc_data.get("state")
                }
            ],
            "markdown": "true"
        }]
    }

    return teams_message