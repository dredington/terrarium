#!/usr/bin/env python3

from sentinel import DataAdapter

class Accumulator(DataAdapter):
  def __init__(self):
    self.data = []

  def publish(self, data):
    self.data.append(data)