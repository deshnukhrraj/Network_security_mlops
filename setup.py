''' setup.py file is an essential part of packaging and distributing python projects
It is used by setuptools to define configuration, dependencies, and metadata for the project '''


from setuptools import find_packages, setup # It helps to import packages and modules from the project directory
from typing import List  # Its used to specify the type of data that a function can accept or return


def get_requirements()->List[str]: # this function will return list of requirements
    requirements_list:List[str] = [] # it will read lines from the file
    try:
         with open("requirements.txt") as file:  # it will open the requirements.txt file
            lines=file.readlines() #process each line
            for line in lines:
                requirement=line.strip()
                if requirement and requirement != "-e .":
                    requirements_list.append(requirement)
    except FileNotFoundError:
           print("requirements.txt file not found") # it will print the error message if the file is not found  

 
setup(
    name="Network_Security",
    version="0.0.1",
    author="Raj"
    author_email="deshmukhraj9021@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),

    































































