# import terrarium
# from terrarium import terrarium
from terrarium import temperature_report
from terrarium.temperature_report import TemperatureReport

import unittest

class TestTemperatureReport(unittest.TestCase):

  def setUp(self):
      self.report = TemperatureReport()

  def test(self):
    print("Runninng TestTemperatureReport test!!")
    self.assertTrue(self.report.hello())

if __name__ == '__main__':
    unittest.main()