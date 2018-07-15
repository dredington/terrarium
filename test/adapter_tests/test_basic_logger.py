#!/usr/bin/env python3

from context import terrarium
from terrarium.adapters.basic_logger import BasicLogger

import unittest

class TestBasicLogger(unittest.TestCase):
  def testAbstration(self):
    BasicLogger()

  def testPublish(self):
    logger = BasicLogger()
    logger.publish('test-data')

if __name__ == '__main__':
    unittest.main()