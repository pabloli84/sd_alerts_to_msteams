# Standard library imports...
from http.server import BaseHTTPRequestHandler, HTTPServer

from threading import Thread
import os
# Third-party imports...
import requests

import json
import unittest
from unittest.mock import Mock

from convert_alert import convert_sd_to_ms
from main import send_to_teams

http_port = 6000


def run_mock_server():
    mock_server = HTTPServer(('localhost', http_port), MockServerRequestHandler)

    # Start running mock server in a separate thread.
    # Daemon threads automatically shut down when the main process exits.
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()


class TestJSON(unittest.TestCase):
    
    def test_valid_input_sd_json(self):
        with open("test_data/sd_valid_incident_closed.json") as json_valid, \
                open('test_data/teams_valid_incident_closed.json') as json_teams:
            incoming_json = json.load(json_valid)
            teams_valid_json = json.load(json_teams)
            teams_json = convert_sd_to_ms(incoming_json)
            
            self.assertEqual(teams_valid_json, teams_json)

    def test_cf_with_valid_sd_json(self):
        with open("test_data/sd_valid_incident_closed.json") as json_valid:
            incoming_json = json.load(json_valid)

            run_mock_server()

            req = Mock(get_json=Mock(return_value=incoming_json))
            self.assertEqual(send_to_teams(req), "OK")


class MockServerRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(requests.codes.ok)
        self.end_headers()

        return
