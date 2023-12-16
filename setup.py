from setuptools import setup, find_packages
from typing import List

def getrequirements(file_path: str) -> List[str]:
    '''
    this function returns a list of requirements from a file
    '''
    requirements = []
    with open(file_path, 'r') as f:
        for line in f:
            requirements.append(line.strip())
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Elvis Gideon',
    author_email='elvisgideonuzuegbu@gmail.com',
    packages=find_packages(),
    install_requires=getrequirements('requirements.txt')
)