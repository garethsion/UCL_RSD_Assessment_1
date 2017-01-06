USAGE
=====

greengraph Generates a graph of the green space between two input locations, by logging the number of green pixels from a series of satellite images sourced from the google maps API

* To install the program withut using pip, clone the repository, navigate to the correct directotry in a command line terminal, and type:

		sudo python setup.py install

* Once the package has installed, it can be used from the command line with the following command:
	
		greengraph --start START --end END --steps STEPS --out OUTFILE.PNG

* Optional arguments:
	
	--help, -h		display the help message
	--start START		The starting location, which defaults to London
	--end END		The end location, which defaults to Cardiff
	--steps STEPS		Number of steps between the start and end locations. Defaults to 50
	--out OUT.png		Filename to save the plot to. This saves a png to file

