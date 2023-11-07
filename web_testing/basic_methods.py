from selenium.webdriver.remote.webelement import WebElement


def perform_checkbox_action(checkboxes: list[WebElement] | WebElement, action: str) -> None:
    """
    Checks or unchecks all provided fields in checkboxes.
    Args:
        checkboxes: Elements possible to check/uncheck
        action: Check/uncheck checkboxes

    Returns:

    """
    assert action in ["check", "uncheck"]
    for checkbox in checkboxes:
        if (not checkbox.is_selected() and action == "check") or (checkbox.is_selected() and action == "uncheck"):
            checkbox.click()
