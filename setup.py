from setuptools import setup

install_requires = ['weather-api', 'coverage==4.4.2']

setup(
   name='terrarium',
   version='0.0.1',
   description='IoT Hub for monitoring Hydroponics',
   author='dredington',
   author_email='',
   packages=['terrarium'],
   install_requires=install_requires,
   scripts=['bin/launch']
)