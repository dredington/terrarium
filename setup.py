from setuptools import setup

setup(
   name='terrarium',
   version='0.0.1',
   description='IoT Hub for monitoring Hydroponics',
   author='dredington',
   author_email='',
   packages=['terrarium'],
   install_requires=['weather-api'],
   scripts=['bin/test']
)