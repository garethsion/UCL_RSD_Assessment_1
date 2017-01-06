README
------
This repository contains code in answer to the first assessment for the Research Software 
Design module in Python at University College London. It involves the packaging and unit 
testing of sample code provided by Dr James Hetherington. 

Greengraph plots a graph denoting the green space between two locations, by pixelating 
satellite images from google earth and counting the number of green pixels. It takes user
inputs for the start and end locations, step size for plotting, and the name of the output file.

For information of how to use this repository, please refer to the USAGE file. 

The tree of this repository is shown below:

|   CITATION.md
|   LICENSE.md
|   README.md
|   setup.py
|   USAGE.md
|
|---greengraph
|   |   command.py
|   |   graph.py
|   |   map.py
|   |   __init__.py
|   |
|   |---test
|       |   test_graph.py
|       |   test_map.py
|       |   __init__.py
|       |
|       |---fixtures
|               journey.yaml
|               location_sequence.yaml
|               london_green.npy
|               london_sat.png
|
|---scripts
        greengraph

