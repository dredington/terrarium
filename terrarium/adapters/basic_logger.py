#!/usr/bin/env python3

from sentinel import DataAdapter

class BasicLogger(DataAdapter):
  def publish(self, data):
    print("BasicLogger: %s" %(data))