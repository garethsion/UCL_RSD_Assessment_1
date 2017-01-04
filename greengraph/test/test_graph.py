#!/usr/bin/python
from greengraph import Greengraph
from nose.tools import assert_raises

def test_location_sequence():
    """ Unit tests for location_sequence"""
    def test_location_sequence_fails_on_non_str_start():
        with assert_raises(TypeError) as exception:
             location_sequence(self, 1, 5)

    def test_location_sequence_fails_on_non_str_end(): 
        with test_assert_raises(TypeError) as exception:
            location_sequence(self, 1, 5)

    def test_location_sequence_fails_on_non_num_steps():
        with assert_raises(TypeError) as exception:
            location_sequence(self, 'London', 'Cambridge', 'Cardiff')

    def test_location_sequence_fails_on_non_pos_steps():
        with assert_raises(ValueError) as exception:
            location_sequence(self, 'London', 'Cambridge', -1)



