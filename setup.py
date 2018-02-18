from setuptools import setup, find_packages


def requirements_from_file(requirements_path: str):
    """ Retrives install requires from requirements file
    """
    with open(requirements_path) as requirements:
        return requirements.readlines()


setup(
    name='cuve-order-service',
    description='CuVe Order Service',
    url='https://github.com/TheCuVe/order-service',
    version='0.0.1',

    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=['tests']),

    install_requires=requirements_from_file('./requirements.txt'),
    tests_requires=requirements_from_file('./requirements.dev.txt'),

    entry_points={
        'console_scripts': ['cuve.order = cuve.order_service.__main__:cli'],
    },
    namespace=['cuve'],
)
