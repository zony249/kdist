import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "kdist",
    version = "0.0.5",
    author = "Zony Yu",
    author_email = "zony249@gmail.com",
    description = ("Implements layer-isolated KD"), 
    license = "GPL-3",
    keywords = "Knowledge Distillation",
    url = "",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)