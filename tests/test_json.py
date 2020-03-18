import json
import unittest

from app.convert_alert import convert_sd_to_ms

class TestJSON(unittest.TestCase):
    
    def test_valid_input_sd_json(self):
        with open("tests/sd_valid_incident_closed.json") as json_valid, open('tests/teams_valid_incident_closed.json') as json_teams:
            incoming_json = json.load(json_valid)
            teams_valid_json = json.load(json_teams)
            teams_json = convert_sd_to_ms(incoming_json)
            
            self.assertEqual(teams_valid_json, teams_json)
