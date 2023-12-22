import argparse

import pytest

test_classes = {
    "add_remove": "add_remove_page",
    "basic_auth": "basic_auth",
    "broken_img": "broken_img",
    "challenging_dom": "challenging_DOM",
    "checkboxes": "checkboxes",
    "context_menu": "context_menu",
    "digest_auth": "digest_auth",
    "dissapearing_elements": "dissapearing_elements",
    "drag_and_drop": "drag_and_drop",
    "drop_down_list": "drop_down_list",
    "dynamic_content": "dynamic_content",
    "dynamic_controls": "dynamic_controls",
    "dynamic_loading": "dynamic_loading",
    "entry_ad": "entry_ad",
    "exit_intent": "exit_intent",
    "file_download": "file_download",
    "file_upload": "file_upload",
    "floating_menu": "floating_menu",
    "form_auth": "form_auth",
    "frames": "frames",
    "geolocation": "geolocation",
    "horizontal_slider": "horizontal_slider",
    "hovers": "hovers",
    "infinite_scroll": "infinite_scroll",
    "input": "input",
    "jquery_ui": "jquery_ui",
    "js_alert": "js_alert",
    "js_error": "js_error",
    "key_presses": "key_presses",
    "large_DOM": "large_DOM",
    "main_page": "main_page",
    "multiple_windows": "multiple_windows",
    "notification_message": "notification_message",
    "redirector": "redirector",
    "shadow_dom": "shadow_dom",
    "shifting_content": "shifting_content",
    "sortable_data_res": "sortable_data_res",
    "typos": "typos"
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
