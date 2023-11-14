import argparse

import pytest

test_classes = {
    'add_remove': "add_remove_page",
    'basic_auth': "basic_auth",
    'broken_img': "broken_img",
    "challenging_dom": "challenging_DOM",
    "checkboxes": "checkboxes",
    "context_menu": "context_menu",
    "digest_path": "digest_path",
    "dissapearing_elements": "dissapearing_elements",
    "drag_and_drop": "drag_and_drop",
    "dropdown_list": "dropdown_list",
    "dymaic": "dynamic_page",
    "main_page": "main_page"
}

parser = argparse.ArgumentParser(description='Run web tests with specific suite.')
for test_name in test_classes.keys():
    parser.add_argument(f'-{test_name}', action='store_true', help=f'Run {test_name.replace("_", " ").title()} Tests')
parser.add_argument('-n', '--processes', type=int, default=4, help='Number of parallel processes')
args = parser.parse_args()

pytest_args = []
for test_name, test_class in test_classes.items():
    if getattr(args, test_name):
        pytest_args.append(f"tests/test_{test_classes[test_name]}.py")

pytest.main(['-n', str(args.processes)] + pytest_args)
# poetry run python main.py -add_remove -n 3
