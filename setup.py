"""The module that implements PyPI settings.
"""

from setuptools import find_packages
from setuptools import setup

from apyscript import __version__

_DESCRIPTION: str = (
    'apyscript is a Python\'s frontend library to create '
    'html and js file, that has a ActionScript 3 (as3)-like interface.'
)

_LONG_DESCRIPTION: str = (
    'apyscript is a Python\'s frontend library to '
    'create html and js file, that has a ActionScript 3 '
    '(as3)-like interface.'
    ' For more details, please see Github repository:'
    ' https://github.com/simon-ritchie/apyscript'
)

setup(
    name='apyscript',
    version=__version__,
    url='https://github.com/simon-ritchie/apyscript',
    maintainer='simon-ritchie',
    maintainer_email='',
    description=_DESCRIPTION,
    long_description=_LONG_DESCRIPTION,
    packages=find_packages(
        exclude=('tests', 'tests.*', 'test_projects', 'test_projects.*')),
    install_requires=[
        'typing-extensions',
    ],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
