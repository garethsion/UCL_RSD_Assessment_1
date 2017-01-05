#!/usr/bin/env python
import os
from io import BytesIO
from matplotlib import image as img
import requests
from mock import Mock, patch
import geopy
import numpy as np
from greengraph.map import Map

# Global coordinates for London
lat = 51.5073509
lon = -0.1277583

def test_constructor():
    mock_image = open(os.path.join(os.path.dirname(__file__),
        'fixtures', 'london_sat.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = Map(lat, lon)
        mock_get.assert_called_with(
            'http://maps.googleapis.com/maps/api/staticmap?',
            params=dict(size    =   '400x400', 
                        zoom    =   10, 
                        center  =   '51.5073509,-0.1277583',
                        style   =   'feature:all|element:labels|visibility:off', 
                        sensor  =   'false', 
                        maptype =   'satellite')
            )

