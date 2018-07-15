#!/usr/bin/env python3
from weather import Weather, Unit

from sentinel import DataSource

class YahooWeather(DataSource):

  def __init__(self):
    self.weather = Weather(unit=Unit.FAHRENHEIT)
    self.lookup = self.weather.lookup_by_location(80031)
    self.condition = self.lookup.condition

  def report(self):
    return { 'temperature': self.temperature(), 'humidity': self.humidity() }

  def temperature(self):
    return int(self.condition.temp)

  def humidity(self):
    return int(self.lookup.atmosphere['humidity'])
