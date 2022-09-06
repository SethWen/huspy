from setuptools import find_packages, setup
from huspy import cli

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name='huspy',
    version=cli.__version__,
    description='A git hooks for Python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
    extras_require={
        'pyproject': ['toml'],
    },
)
