#!/usr/bin/env python3

from context import terrarium
from terrarium.data_sources.yahoo_weather import YahooWeather

from weather.objects.weather_obj import *

import unittest

class TestYahooWeather(unittest.TestCase):

  def setUp(self):
      self.report = YahooWeather()

  def testTemperature(self):
    """Is temperature an integer?"""
    self.assertTrue(type(self.report.temperature()) is int)

  def testHumidity(self):
    """Is humidity an integer and a valid percentage?"""
    humidity = self.report.humidity()
    self.assertTrue(type(humidity) is int)
    self.assertTrue(0 <= humidity <= 100)


if __name__ == '__main__':
    unittest.main()