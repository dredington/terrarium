#!/usr/bin/env python3
from weather import Weather, Unit

class TemperatureReport:

  def hello(self):
    return True

  def get_weather(self):
    weather = Weather(unit=Unit.FAHRENHEIT)
    lookup = weather.lookup_by_location(80031)
    condition = lookup.condition

    condition.text
    condition.temp

    return lookup