#!/usr/bin/python
from greengraph import Greengraph
from nose.tools import assert_equal
import yaml
import os
import numpy.testing as npt

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
            npt.assert_array_eual(my_graph.location_sequence(**fixture),result)
