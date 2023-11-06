import argparse
import unittest

from web_testing.basic_tests import AddRemovePageTests, MainPageTests, BasicAuthTests, BrokenImageTests

test_suite = unittest.TestSuite()
test_classes = {
    'basic': MainPageTests,
    'add_remove': AddRemovePageTests,
    'basic_auth': BasicAuthTests,
    'broken_img': BrokenImageTests
}

parser = argparse.ArgumentParser(description='Run web tests with specific suite.')
for test_name in test_classes.keys():
    parser.add_argument(f'-{test_name}', action='store_true', help=f'Run {test_name.replace("_", " ").title()} Tests')
args = parser.parse_args()

for test_name, test_class in test_classes.items():
    if getattr(args, test_name):
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(test_class))

# Run the test suite
unittest.TextTestRunner().run(test_suite)
