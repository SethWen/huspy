import codecs
import sys
import unittest
import argparse

from setuptools import find_packages, setup, Command

import huspy as huspy


class RunTests(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        loader = unittest.TestLoader()
        tests = loader.discover('yapftests', pattern='*_test.py', top_level_dir='.')
        runner = unittest.TextTestRunner()
        results = runner.run(tests)
        sys.exit(0 if results.wasSuccessful() else 1)


setup(
    name='huspy',
    version=huspy.__version__,
    description='A formatter for Python code.',
    long_description='long description',
    license='Apache License, Version 2.0',
    author='Shawn',
    maintainer='SethWen',
    maintainer_email='coolrainerseth@gmail.com',
    packages=find_packages('.'),
    project_urls={
        'Source': 'https://github.com/SethWen/huspy',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
    entry_points={
        'console_scripts': [
            'huspy = huspy:main',
        ],
    },
    cmdclass={
        # 'test': RunTests,
    },
    extras_require={
        'pyproject': ['toml'],
    },
)
