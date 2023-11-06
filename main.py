import argparse
import unittest

from web_testing.basic_tests import AddRemovePageTests, MainPageTests, BasicAuthTests, BrokenImageTests

# Define the test suite
test_suite = unittest.TestSuite()

# Add your test cases to the suite based on the command-line arguments
parser = argparse.ArgumentParser(description='Run web tests with specific suite.')
parser.add_argument('-basic', action='store_true', help='Run basic tests')
parser.add_argument('-add_remove', action='store_true', help='Run AddRemovePageTests')
parser.add_argument('-basic_auth', action='store_true', help='Run BasicAuthTests')
parser.add_argument('-broken_img', action='store_true', help='Run BrokenImageTests')

args = parser.parse_args()

if args.basic:
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(MainPageTests))

if args.add_remove:
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(AddRemovePageTests))

if args.basic_auth:
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(BasicAuthTests))

if args.broken_img:
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(BrokenImageTests))

# Run the test suite
unittest.TextTestRunner().run(test_suite)
