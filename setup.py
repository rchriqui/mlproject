from setuptools import find_packages, setup
from typing import list

def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements

    Args:
        file_path (str): _description_

    Returns:
        List[str]: _description_
    """
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

setup(
    name='mlproject',
    version='0.0.1',
    author='Robin',
    author_email='robin.chriqui.pro@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
    
)