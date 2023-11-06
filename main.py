import argparse
import unittest

from web_testing.basic_tests import AddRemovePageTests, MainPageTests

# Define the test suite
test_suite = unittest.TestSuite()

# Add your test cases to the suite based on the command-line arguments
parser = argparse.ArgumentParser(description='Run specific tests.')
parser.add_argument('-basic', action='store_true', help='Run basic tests')
parser.add_argument('-add_remove', action='store_true', help='Run AddRemovePageTests')

args = parser.parse_args()

if args.basic:
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(MainPageTests))

if args.add_remove:
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(AddRemovePageTests))

# Run the test suite
unittest.TextTestRunner().run(test_suite)
