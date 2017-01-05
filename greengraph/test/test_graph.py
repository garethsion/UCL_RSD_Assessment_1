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
            answer = Greengraph(**fixture)
            assert_equal(answer.start, fixture['start'])
            assert_equal(answer.end, fixture['end'])
            assert_equal(answer.geocoder.domain, "maps.google.co.uk")
