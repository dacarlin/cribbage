from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='cribbage',
    version='1.2.1',
    description='Cribbage for your command line',
    long_description=long_description,
    url='https://github.com/dacarlin/cribbage',
    author='Alex Carlin',
    author_email='alxcarln@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='cribbage cards card-games machine-learning ai',
    packages = ['cribbage'] ,
    install_requires=['pytest', 'numpy', 'tqdm'],
    entry_points={
        'console_scripts': [
            'cribbage=cribbage.main:main',
        ],
    },
)
