from setuptools import setup, find_packages 
from typing import List


def get_requirements()->List[str]:
    reuirements_list=List[str]=[]
    return reuirements_list
setup(
    name="sensorlive",
    version="0.0.1",    
    author="Ayush Sinha",
    author_email="ayushsinha148@gmail.com",
    description="A package for sensor live data processing",
    packages=find_packages(),
    install_requires=get_requirements()
)
