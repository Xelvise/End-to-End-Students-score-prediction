# This is responsible for creating the ML application as a package
# setup.py is a script usually included in packages, and ensures the package is installed correctly

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

# '-e .' present in requirements.txt is used to map to setup.py, hence, the entire package gets built automatically

setup(
    # This is basically a metadata of the entire project
    name='ML Project',
    version='0.0.1',
    author='Elvis Gideon',
    author_email='elvisgideonuzuegbu@gmail.com',
    packages=find_packages(),
    install_requires=getrequirements('requirements.txt')
)