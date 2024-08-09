from setuptools import find_packages, setup
from typing import List

requriment_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirements()->List[str]:
    with open(requriment_file_name) as requirement_file:
        requriment_list = requirement_file.readline()
    requriment_list = [requriment_name.replace("\n","") for requriment_name in  requriment_list]
    if REMOVE_PACKAGE in requriment_list:
        requriment_list.remove(REMOVE_PACKAGE)
    return requriment_list





setup(name='Question_answer_answer',
      version = '0.0.1',
      description = 'Question-Answer_generator',
      author='Utkarsh',
      packages=find_packages(),




      install_reqires = get_requirements()

      )