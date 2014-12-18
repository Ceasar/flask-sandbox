"""
Demonstrates the behavior of ``url_for()`` under different conditions.
"""
import unittest

from flask import Flask, url_for


class TestUrlFor(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_url_for(self):
        self.app.add_url_rule("/x", endpoint="x")

        with self.app.test_request_context('/'):
            assert url_for('x') == "/x"

    def test_url_for_external(self):
        self.app.add_url_rule("/x", endpoint="x")

        with self.app.test_request_context('/'):
            assert url_for('x', _external=True) == "http://localhost/x"

    def test_url_for_external_with_server_name(self):
        self.app.config['SERVER_NAME'] = 'localhost:5000'
        self.app.add_url_rule("/x", endpoint="x")

        with self.app.test_request_context('/'):
            assert url_for('x', _external=True) == "http://localhost:5000/x"

    def test_url_for_server_name(self):
        self.app.config['SERVER_NAME'] = 'localhost:5000'
        self.app.add_url_rule("/x", endpoint="x")

        with self.app.app_context():
            assert url_for('x') == "http://localhost:5000/x"

    def test_url_for_server_name_external(self):
        self.app.config['SERVER_NAME'] = 'localhost:5000'
        self.app.add_url_rule("/x", endpoint="x")

        with self.app.app_context():
            assert url_for('x', _external=True) == "http://localhost:5000/x"
