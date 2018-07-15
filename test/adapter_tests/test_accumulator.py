#!/usr/bin/env python3

from context import terrarium
from terrarium.adapters.accumulator import Accumulator

import unittest

class TestAccumulator(unittest.TestCase):
  def testAbstration(self):
    Accumulator()

  def testPublish(self):
    logger = Accumulator()
    logger.publish('test-data')
    self.assertEqual(len(logger.data), 1)


if __name__ == '__main__':
    unittest.main()