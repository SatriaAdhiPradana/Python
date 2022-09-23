#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'face_recognition_models>=0.3.0',
    'Click>=6.0',
    'dlib>=19.7',
    'numpy',
    'Pillow'
]

test_requirements = [
    'tox',
    'flake8'
]

setup(
    name='face_recognition',
    version='1.4.0',
    description="Recognize faces from Python or from the command line",
    long_description=readme + '\n\n' + history,
    author="Satria Adhi Pradana",
    author_email='satriaadhipradana0@gmail.com',
    url='https://github.com/SatriaAdhiPradana/Python',
    packages=[
        'face_recognition',
    ],
    package_dir={'face_recognition': 'face_recognition'},
    package_data={
        'face_recognition': ['models/*.dat']
    },
    entry_points={
        'console_scripts': [
            'face_recognition=face_recognition.face_recognition_cli:main',
            'face_detection=face_recognition.face_detection_cli:main'
        ]
    test_suite='tests',
    tests_require=test_requirements
)
