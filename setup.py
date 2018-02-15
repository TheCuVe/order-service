from setuptools import setup, find_packages


def requirements_from_file(requirements_path: str):
    """ Retrives install requires from requirements file
    """
    with open(requirements_path) as requirements:
        return requirements.readlines()



setup(
    name='cuve',
    description='',
    url='',
    version='0.0.1',

    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    install_requires=requirements_from_file('./requirements.txt'),
    tests_requires=requirements_from_file('./requirements.dev.txt'),
    entry_points={
        'console_scripts': ['cuve = cuve.__main__:cli'],
    },
)
