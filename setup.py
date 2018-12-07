# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='trello-capture',
    version='1.0.1',
    description='Add cards to your Inbox from command line',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Ege Güneş',
    author_email='egegunes@gmail.com',
    license="GPLv3",
    url='https://github.com/egegunes/trello-capture',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "requests"
    ],
    entry_points={
        'console_scripts': ['capture=capture.capture:run']
    }
)
