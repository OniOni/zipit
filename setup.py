from setuptools import setup

setup(
    name='zipit',
    version='0.0.1',
    description='Very thin wrapper around zipapp that let\'s you package a python module and dependencies.',
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
