#!/usr/bin/env python

from setuptools import setup, find_packages

# On the base of those posts : https://stackoverflow.com/questions/26900328/install-dependencies-from-setup-py 

import os

lib_folder = os.path.dirname(os.path.realpath(__file__))

requirement_path = f"{lib_folder}/requirements.txt"

install_requires = [] # Array used to loaded required libraries from th requirements.txt file

if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

setup(
 name='Todo-Decker-CDOF3',
 version='1.0',
 author='Mathys DECKER',
 license='MIT',
 long_description=open('README.md').read(),
 install_requires=install_requires
)