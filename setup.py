from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "Machine Learning"
VERSION = "0.0.1"
DESCRIPTION = "This is ML Project"
AUTHOR_NAME = "Naren"
AUTHOR_EMAIL = "narendra.m.savade@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    with open (REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
            
        return requirement_list

print(get_requirements_list())
setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements_list()
     )