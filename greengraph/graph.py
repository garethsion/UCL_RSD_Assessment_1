#!/usr/bin/env python
import numpy as np
import geopy
from .map import Map

class Greengraph(object):
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk")
        
    def geolocate(self, place):
        return self.geocoder.geocode(place, exactly_one=False)[0][1]
    
    def location_sequence(self, start,end,steps):
        # Raise an error if the input argument types do not match what is expected
        if type(start) != str:
            raise TypeError("Source should be a *string* value")
        if type(end) != str:
            raise TypeError("Destination should be a *string* value")
        
        # Raise an error if steps is not a number 
        if type(steps) != int & type(steps) != float:
            raise TypeError("Step size must be an *integer* or *floating point* value") 
        
        # Raise an error if steps is negative
        if steps < 0:
            raise ValueError("Step size must be positive")

        lats = np.linspace(start[0], end[0], steps)
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose()

    def green_between(self, steps):
        return [Map(*location).count_green()
                for location in self.location_sequence(
                    self.geolocate(self.start), 
                    self.geolocate(self.end),
                    steps)]
