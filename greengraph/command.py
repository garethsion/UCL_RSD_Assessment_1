from matplotlib import pyplot as plt
from argparse import ArgumentParser
from .graph import Greengraph

def process():
    parser = ArgumentParser(description = "Set desired source and destination locations, step size, and output type")
    parser.add_argument('--source', '-s')
    parser.add_argument('--destination', '-d')
    parser.add_argument('--step', '-p')
    parser.add_argument('--out', '-o')

    arguments = parser.parse_args()    

    mygraph=Greengraph(arguments.source, arguments.destination)
    data = mygraph.green_between(arguments.step) 
    
    fig = plt.plot(data)
    fig = plt.savefig(arguments.out)
    
if __name__ =="__main__":
    process()