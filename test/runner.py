import unittest
import coverage

# Import dependencies
from weather import Weather, Unit

cov = coverage.Coverage()
cov.start()

# Import test modules
import test_sentinel

# Data Sources
import data_source_tests.test_yahoo_weather

# # Adapters
import adapter_tests.test_basic_logger
import adapter_tests.test_accumulator

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_sentinel))
suite.addTests(loader.loadTestsFromModule(data_source_tests.test_yahoo_weather))
suite.addTests(loader.loadTestsFromModule(adapter_tests.test_basic_logger))
suite.addTests(loader.loadTestsFromModule(adapter_tests.test_accumulator))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

cov.stop()
cov.save()

cov.html_report()