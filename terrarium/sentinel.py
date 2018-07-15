#!/usr/bin/env python3
import abc

class DataSource(abc.ABC):
  @abc.abstractmethod
  def report(self):
    pass

class DataAdapter(abc.ABC):
  @abc.abstractmethod
  def publish(self, data):
    pass

class Sentinel:

  def __init__(self, dataSource, adapters):
    self.dataSource = dataSource
    self.adapters = adapters

  def execute(self):
    instance = self.dataSource()
    report = instance.report()

    for adapter in self.adapters:
      adapter.publish(report)

    return report