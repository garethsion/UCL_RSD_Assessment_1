from setuptools import setup, find_packages

setup(
    name = "greengraph",
    version = "0.1.0",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greengraph'],
    #install_requires = ['argparse']
    install_requires = ['numpy', 'geopy', 'matplotlib', 'requests', 'argparse']
)