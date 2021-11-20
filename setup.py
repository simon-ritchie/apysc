"""The module that implements PyPI settings.
"""

from setuptools import find_packages
from setuptools import setup

from apysc import __version__

_DESCRIPTION: str = (
    'apysc is a Python\'s frontend library to create '
    'html and js file, that has the ActionScript 3 (as3)-like interface.'
)

_LONG_DESCRIPTION: str = (
    'apysc is the Python\'s frontend library to '
    'create html and js file, that has a ActionScript 3 '
    '(as3)-like interface.'
    ' For more details, please see GitHub repository:'
    ' https://github.com/simon-ritchie/apysc'
)

setup(
    name='apysc',
    version=__version__,
    url='https://github.com/simon-ritchie/apysc',
    maintainer='simon-ritchie',
    maintainer_email='',
    description=_DESCRIPTION,
    long_description=_LONG_DESCRIPTION,
    packages=find_packages(
        exclude=('tests', 'tests.*', 'test_projects', 'test_projects.*')),
    install_requires=[
        'typing-extensions',
        'html-minifier',
    ],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
    ],
)
