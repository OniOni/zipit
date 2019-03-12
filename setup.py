from setuptools import setup

with open('README.md') as f:
    long_description = '\n' + f.read()

setup(
    name='zipit',
    version='0.0.2',
    description='Very thin wrapper around zipapp that let\'s you package a python module and dependencies.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mathieu Sabourin',
    author_email='mathieu.c.sabourin@gmail.com',
    url='https://github.com/OniOni/zipit',
    packages=['zipit'],
    entry_points={
        'console_scripts': [
            'zipit=zipit.cli:main'
        ]
    }
)
