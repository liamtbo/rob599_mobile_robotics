from setuptools import find_packages
from setuptools import setup

setup(
    name='goal_target',
    version='0.0.0',
    packages=find_packages(
        include=('goal_target', 'goal_target.*')),
)
