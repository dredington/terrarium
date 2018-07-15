#!/usr/bin/env python3
from context import terrarium
from terrarium.sentinel import DataSource, DataAdapter, Sentinel

import unittest
from unittest.mock import MagicMock

sampleData = { "temperature" : 68, "humidity": 32 }

class ConcreteDataSource(DataSource):
  def report(self):
    return sampleData

class ConcreteAdapter(DataAdapter):
  def __init__(self):
    self.reports = []

  def publish(self, data):
    self.reports.append(data)

class IncorrectDataSource(DataSource):
  pass

class TestAbstractClasses(unittest.TestCase):
  def testDataSourceAbstraction(self):
    self.failUnlessRaises(TypeError, IncorrectDataSource)

class TestSentinel(unittest.TestCase):
  def setUp(self):
    self.testAdapter = ConcreteAdapter()
    self.sentinel = Sentinel(ConcreteDataSource, [self.testAdapter])

  def testExecute(self):
    """#execute fetches data from the dataSource and forwards that data to adapters"""
    report = self.sentinel.execute()
    self.assertIsInstance(report, dict)
    self.assertEqual(report['temperature'], 68)

  def testAdapterUse(self):
    self.testAdapter.publish = MagicMock()
    self.sentinel.execute()
    self.testAdapter.publish.assert_called_with(sampleData)

if __name__ == '__main__':
    unittest.main()