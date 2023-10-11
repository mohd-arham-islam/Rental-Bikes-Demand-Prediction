from setuptools import find_packages, setup

HYPHEN_E_DOT = '-e .'

def getRequirements(filePath):
    requirements = []

    '''
    readlines() method is used to read the requirements.txt file. Since at the end of each line, '\n' is also considered, we will replace the same with blanks.
    '''

    with open(filePath) as fileObj:
        requirements = fileObj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='Rental Bikes Demand Prediction',
    version='1.0',
    author='Arham',
    packages=find_packages(),
    install_requires=getRequirements('requirements.txt')
)
