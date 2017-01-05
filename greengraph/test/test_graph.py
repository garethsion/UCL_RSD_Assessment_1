#!/usr/bin/python
from greengraph import Greengraph
from nose.tools import assert_equal
import yaml
import os
import numpy.testing as npt 
from mock import Mock, patch

def test_geolocate():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures', 'journey.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            result = Greengraph(**fixture)
            assert_equal(result.start, fixture['start'])
            assert_equal(result.end, fixture['end'])
            assert_equal(result.geocoder.domain, "maps.google.co.uk")

def test_location_sequence():
    with open(os.path.join(os.path.dirname(__file__),
                            'fixtures', 'location_sequence.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
        for fixture in fixtures:
            my_graph = Greengraph('London', 'Cardiff')
            result = fixture.pop('result')
            npt.assert_array_equal(my_graph.location_sequence(**fixture), result, 
                    "Error in location_sequence")

def test_green_between():
    directory = os.path.join(os.path.dirname(__file__), 'fixtures', 'london_sat.png')
    mock_start = open(directory, 'rb')
    mock_end = open(directory, 'rb')
    london_greenness = 108032

    with patch('requests.get', return_value=Mock(content=mock_start.read())) as mock_get:
        result = Greengraph('Cardiff', 'London')
        mock_green = result.green_between(2)
        npt.assert_array_almost_equal(mock_green, [london_greenness, london_greenness], decimal=2)
