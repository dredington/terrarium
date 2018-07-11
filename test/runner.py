import unittest
import coverage



# Import dependencies
from weather import Weather, Unit

cov = coverage.Coverage()
cov.start()

# Import test modules
import test_temperature_report

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_temperature_report))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

cov.stop()
cov.save()

cov.html_report()