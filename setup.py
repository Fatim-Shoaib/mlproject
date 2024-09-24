from setuptools import find_packages, setup
from typing import List

# this means that the function is going to return a list
def get_requirements(filepath)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements = []
    with open(filepath, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

# this is basically the metadata of the package
setup(
    name='mlproject',
    version='0.0.1',
    author='Fatim',
    author_email='mfatim.shoaib@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn']
    install_requires=get_requirements('requirements.txt')
)