from context import terrarium
from terrarium.temperature_report import TemperatureReport

from weather.objects.weather_obj import *

import unittest


class TestTemperatureReport(unittest.TestCase):

  def setUp(self):
      self.report = TemperatureReport()

  def test_temperature(self):
    """Is temperature an integer?"""
    self.assertTrue(type(self.report.temperature()) is int)

  def test_humidity(self):
    """Is humidity an integer and a valid percentage?"""
    humidity = self.report.humidity()
    self.assertTrue(type(humidity) is int)
    self.assertTrue(0 <= humidity <= 100)


if __name__ == '__main__':
    unittest.main()