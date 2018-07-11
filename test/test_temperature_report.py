from context import terrarium
from terrarium import TemperatureReport

from weather.objects.weather_obj import *

import unittest

class TestTemperatureReport(unittest.TestCase):

  def setUp(self):
      self.report = TemperatureReport()

  def test_temperature(self):
    self.assertTrue(type(self.report.temperature()) is int)

  def test_humidity(self):
    self.assertTrue(type(self.report.humidity()) is int)
    self.assertTrue(0 <= self.report.humidity() <= 100)

if __name__ == '__main__':
    unittest.main()