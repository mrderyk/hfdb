from setuptools import setup, find_packages

setup(
    name='hfdb',
    url='https://github.com/mrderyk/hfdb',
    author='Deryk DeGuzman',
    packages=find_packages(),
    install_requires=['peewee'],
    version='0.0.9',
    license='UNLICENSED',
    description='Hoops Fusion database modules',
)