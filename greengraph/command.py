#!/usr/bin/env python
from matplotlib import pyplot as plt
from argparse import ArgumentParser
from .graph import Greengraph

def process():
    parser = ArgumentParser(description = "Generate a graph showing the ammount " +  
            "of green space between two geographical locations by determining" + 
            " the number of green pixels in a satellite image")
    parser.add_argument('--start', '-s', default="London", required=False, 
            help='Starting location')
    parser.add_argument('--end', '-d', default="Cardiff", required=False, 
            help='End Location')
    parser.add_argument('--steps', '-p', default="50", required=False,
            help='Number of steps between the start and end locations')
    parser.add_argument('--out', '-o', default="graph.png", required=False, 
            help='Output file name')   

    arguments = parser.parse_args()    
    
    mygraph=Greengraph(arguments.start, arguments.end)
    data = mygraph.green_between(arguments.steps) 
    
    fig = plt.plot(data)
    fig = plt.savefig(arguments.out)
    
if __name__ =="__main__":
    process()
