import unittest
from tcxmodel import TrackPointModel
import re

class TestParseFilterFunction(unittest.TestCase):

    def test_parse_expression(self):
        list = TrackPointModel('22-09-2023 12:28:35.349 UTC', latitude=45.79340667, longitude=24.13245167, altitude=408.742, hartRate=103, distance=0.1000000014901161, sensorState='Present')
        pass