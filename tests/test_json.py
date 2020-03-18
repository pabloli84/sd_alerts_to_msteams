import json
import unittest
from unittest.mock import Mock

from app.convert_alert import convert_sd_to_ms
from app import main

class TestJSON(unittest.TestCase):
    
    def test_valid_input_sd_json(self):
        with open("tests/sd_valid_incident_closed.json") as json_valid, open('tests/teams_valid_incident_closed.json') as json_teams:
            incoming_json = json.load(json_valid)
            teams_valid_json = json.load(json_teams)
            teams_json = convert_sd_to_ms(incoming_json)
            
            self.assertEqual(teams_valid_json, teams_json)


    def test_cf_with_valid_sd_json(self):
        with open("tests/sd_valid_incident_closed.json") as json_valid:
            incoming_json = json.load(json_valid)
            
            req = Mock(get_json=Mock(return_value=incoming_json), args=incoming_json)
            self.assertEqual(main.send_to_teams(req), "OK")