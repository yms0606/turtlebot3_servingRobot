from setuptools import find_packages
from setuptools import setup

setup(
    name='serving_interface',
    version='0.0.0',
    packages=find_packages(
        include=('serving_interface', 'serving_interface.*')),
)
