from context import terrarium
from terrarium import TemperatureReport

from weather.objects.weather_obj import *

import unittest

class TestTemperatureReport(unittest.TestCase):

  def setUp(self):
      self.report = TemperatureReport()

  def test_simple(self):
    self.assertTrue(self.report.hello())

  def test_get_weather(self):
    weather = self.report.get_weather()
    condition = weather.condition
    self.assertTrue(type(weather) is WeatherObject)
    self.assertTrue(type(condition) is Condition)
    self.assertTrue(type(condition.temp) is str)

if __name__ == '__main__':
    unittest.main()