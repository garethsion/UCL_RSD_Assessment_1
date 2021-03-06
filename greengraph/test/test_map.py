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

image_file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'london_sat.png')
array_file_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'london_green.npy')

def test_constructor():
   mock_london_image = open(image_file_path, 'rb')
   with patch('requests.get', return_value=Mock(content=mock_london_image.read())) as mock_get:
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

def test_green():
   mock_london_image = open(image_file_path, 'rb')
   test_green_array = np.load(array_file_path)

   with patch('requests.get', return_value=Mock(content=mock_london_image.read())) as mock_get:
        test_map = Map(lat, lon)
        np.testing.assert_array_equal(Map.green(test_map, threshold=1.1), 
                test_green_array, "green() in Map() does not match a known value")

def test_count_green():   
    london_greenness = np.sum(np.load(array_file_path))
    
    mock_london_image = open(os.path.join(os.path.dirname(__file__),
        'fixtures', 'london_sat.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_london_image.read())) as mock_get:
        test_map = Map(lat, lon)
        np.testing.assert_equal(Map.count_green(test_map, threshold=1.1), 
               london_greenness , "Error in Map class - count_green")
        
# Show Green is not used anywhere in the program. however, modifications needed to be made in map.py
# to allow for testing, including having self as an argument to the function, and changing array to 
# np.array. However, since show_green is not used in the program, the test has not been completed. 

# def test_show_green() 
