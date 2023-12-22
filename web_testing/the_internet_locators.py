from selenium.webdriver.common.by import By


class TheInternetMainPageLocators:
    main_url = "https://the-internet.herokuapp.com/"
    ab_testing_page = (By.PARTIAL_LINK_TEXT, "A/B Testing")
    add_remove_page = (By.PARTIAL_LINK_TEXT, "Add/Remove Elements")
    basic_auth_page = (By.PARTIAL_LINK_TEXT, "Basic Auth")


class AddRemovePageLocators:
    main_url = "https://the-internet.herokuapp.com/add_remove_elements/"
    add_element_button_xpath = (By.XPATH, "//button[contains(text(),'Add Element')]")
    delete_button_xpath = (By.XPATH, "//button[contains(text(),'Delete')]")


class BasicAuthLocators:
    main_url = "https://the-internet.herokuapp.com/basic_auth"
    main_url_with_good_credentials = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
    main_url_with_wrong_credentials = "https://admin:user@the-internet.herokuapp.com/basic_auth"
    congratulations = (By.XPATH, "//*[contains(text(),'Congratulations')]")


class BrokenImagesLocators:
    main_url = "https://the-internet.herokuapp.com/broken_images"


class ChallengingDOMLocators:
    main_url = "https://the-internet.herokuapp.com/challenging_dom"


class CheckboxesLocators:
    main_url = "https://the-internet.herokuapp.com/checkboxes"
    checkbox = (By.XPATH, "//input[@type='checkbox']")


class ContextMenuLocators:
    main_url = "https://the-internet.herokuapp.com/context_menu"
    context_menu = (By.XPATH, "//*[@id='hot-spot]")


class DigestAuthenticationLocators:
    main_url = "https://the-internet.herokuapp.com/digest_auth"
    context_menu = ""


class DissapearingElementsLocators:
    main_url = "https://the-internet.herokuapp.com/disappearing_elements"
    home_button = (By.XPATH, "//a[contains(text(),'Home')]")


class DragAndDropLocators:
    main_url = "https://the-internet.herokuapp.com/drag_and_drop"
    draggable_a = (By.XPATH, "//div[@id='column-a']")
    draggable_b = (By.XPATH, "//div[@id='column-b']")


class DropDownListLocators:
    main_url = "https://the-internet.herokuapp.com/dropdown"
    drop_down_list = (By.ID, "dropdown")
    option_disabled = (By.XPATH, "//select[@id='dropdown']/option[@disabled='disabled']")
    option_one = (By.XPATH, "//select[@id='dropdown']/option[@value='1']")
    option_two = (By.XPATH, "//select[@id='dropdown']/option[@value='2']")


class DynamicContentLocators:
    main_url = "https://the-internet.herokuapp.com/dynamic_content"
    main_url_static = "https://the-internet.herokuapp.com/dynamic_content?with_content=static"
    row = (By.XPATH, "//div[@class='large-10 columns']")


class DynamicControlLocators:
    main_url = "https://the-internet.herokuapp.com/dynamic_controls"
    enable_disable_button = (By.XPATH, "//form[@id='input-example']/button[@onclick='swapInput()']")
    message = (By.XPATH, "//form[@id='input-example']/p[@id='message']")
    add_remove_button = (By.XPATH, "//form[@id='checkbox-example']/button[@onclick='swapCheckbox()']")
    checkbox = (By.XPATH, "//form[@id='checkbox-example']/div/input[@type='checkbox']")
    add_remove_message = (By.XPATH, "//form[@id='checkbox-example']/p[@id='message']")


class DynamicLoadingLocators:
    main_url = "https://the-internet.herokuapp.com/dynamic_loading"
    main_url_added_not_displayed = "https://the-internet.herokuapp.com/dynamic_loading/1"
    main_url_not_added = "https://the-internet.herokuapp.com/dynamic_loading/2"
    start_button = (By.XPATH, "//div[@id='start']/button[contains(text(), 'Start')]")
    loading = (By.XPATH, "//div[@id='loading']")
    hello_world_message = (By.XPATH, "//div[@id='finish']/h4[contains(text(), 'Hello World')]")


class EntryAdLocators:
    main_url = "https://the-internet.herokuapp.com/entry_ad"
    modal_window = (By.XPATH, "//div[@id='modal'")
    close_button = (By.XPATH, "//div[@class='modal']/p[contains(text(), 'Close')]")
    title = (By.XPATH, "//div[@class='example'/h3[contains(text(), 'Entry Ad')]")
    re_enable_button = (By.XPATH, "//div[@class='example']/p/a[@href id = 'restart-ad']")


class ExitIntentLocators:
    main_url = "https://the-internet.herokuapp.com/exit_intent"
    modal_window = (By.XPATH, "//div[@class='modal']")
    title = (By.XPATH, "//div[@class='example']/h3[contains(text(), 'Exit Intent')]")
    close_button = (By.XPATH, "//div[@class='modal-footer']p[contains(text(), 'Close')]")


class FileDownloadLocators:
    main_url = "https://the-internet.herokuapp.com/download"
    # Files in the website are changing. In case of practice, I've just chosen a few.
    logo_png = (By.XPATH, "//div[@class='example']/a[@href='download/Logo.png']")
    lambdaTest_txt = (By.XPATH, "//div[@class='example']/a[@href='download/LambdaTest.txt']")
    upload_txt = (By.XPATH, "//div[@class='example']/a[@href='download/upload.txt']")
    screenshot_png = (By.XPATH, "//div[@class='example']/a[@href='download/Zrzut ekranu 2023-11-15 084842.png']")
    firs_jpg = (By.XPATH, "//div[@class='example']/a[@href='download/1.jpg']")
    some_file_txt = (By.XPATH, "//div[@class='example']/a[@href='download/some-file.txt']")
    QC_pdf = (By.XPATH, "//div[@class='example']/a[@href='download/QC interview.pdf']")
    img_jpg = (By.XPATH, "//div[@class='example']/a[@href='download/IMG-20220115-WA0003.jpg']")
    script_xml = (By.XPATH, "//div[@class='example']/a[@href='download/5mb script.xml']")
    b10_docx = (By.XPATH, "//div[@class='example']/a[@href='download/b10 all test cases code.docx']")
    general_xpath = (By.XPATH, "//div[@class='example']/a[contains(@href, 'download')]")


class FileUploadLocators:
    main_url = "https://the-internet.herokuapp.com/upload"
    choose_file = (By.XPATH, "//form[@method='POST']/input[@id='file-upload']")
    upload_button = (By.XPATH, "//form[@method='POST']/input[@id='file-submit']")
    finish_msg = (By.XPATH, "//div[@class='example']/h3[contains(text(), 'File Uploaded!')]")


class FloatingMenuLocators:
    main_url = "https://the-internet.herokuapp.com/floating_menu"
    home_button = (By.XPATH, "//div[@id='menu']/ul/li/a[@href='#home']")
    news_button = (By.XPATH, "//div[@id='menu']/ul/li/a[@href='#news']")
    contact_button = (By.XPATH, "//div[@id='menu']/ul/li/a[@href='#contact']")
    about_button = (By.XPATH, "//div[@id='menu']/ul/li/a[@href='#about']")


class FormAuthLocators:
    main_url = "https://the-internet.herokuapp.com/login"
    loggin_button = (By.XPATH, "//button[@class='radius']/i[@class='fa fa-2x fa-sign-in']")
    user_name_field = (By.XPATH, "//div[@class='large-6 small-12 columns']/input[@name='username']")
    password_field = (By.XPATH, "//div[@class='large-6 small-12 columns']/input[@name='password']")
    valid_nickname = "tomsmith"
    invalid_nickname = "adamjoseph"
    valid_password = "SuperSecretPassword!"
    invalid_password = "hello1234"
    secure_area_message = (By.XPATH, "//i[@class='icon-lock']")
    logout_button = (By.XPATH, "//a[@class='button secondary radius']")
    invalid_auth_warning = (By.ID, "flash")


class FramesLocators:
    main_url = "https://the-internet.herokuapp.com/frames"
    nested_url = "https://the-internet.herokuapp.com/nested_frames"
    iframe_url = "https://the-internet.herokuapp.com/iframe"
    nested_frames_link = (By.XPATH, "//a[@href='/nested_frames']")
    iframe_link = (By.XPATH, "//a[@href='/iframe']")
    nested_left = (By.XPATH, "//frame[@name='frame-left']")
    nested_middle = (By.XPATH, "//frame[@name='frame-middle']")
    nested_right = (By.XPATH, "//frame[@name='frame-right']")
    nested_bottom = (By.XPATH, "//frame[@name='frame-bottom']")
    bottom_inside = (By.TAG_NAME, "body")
    iframe_welcome_screen = (By.XPATH, "//h3[contains(text(), 'An iFrame containing the TinyMCE WYSIWYG Editor')]")
    iframe_id = "mce_0_ifr"
    text_area = (By.CLASS_NAME, "mce-content-body")
    text_to_send = "TEXT FOR THE TEST"
    text_to_send_2 = " ADDED TEXT"
    inner_text_field = (By.XPATH, f"//span[contains(text(), '{text_to_send}')]")
    entered_text = (By.XPATH, "//em")
    file_button = (By.XPATH, "//span[contains(text(), 'File')]")
    new_document_option = (By.XPATH, "//div[contains(text(), 'New document')]")
    edit_button = (By.XPATH, "//span[contains(text(), 'Edit')]")
    undo_option = (By.XPATH, "//div[contains(text(), 'Undo')]")
    redo_option = (By.XPATH, "//div[contains(text(), 'Redo')]")
    format_button = (By.XPATH, "//span[contains(text(), 'Format')]")
    font_option = (By.XPATH, "//div[contains(text(), 'Fonts')]")
    tahoma_font = (By.XPATH, "//div[contains(text(), 'Tahoma')]")
    italic_option = (By.XPATH, "//div[@title='Italic']")


class GeolocationLocators:
    main_url = "https://the-internet.herokuapp.com/geolocation"
    title = (By.XPATH, "//h3[contains(text(), 'Geolocation')]")
    where_am_i_button = (By.XPATH, "//button[@onclick='getLocation()']")
    latitude = (By.XPATH, "//div[@id='lat-value']")
    longitude = (By.XPATH, "//div[@id='long-value']")
    see_it_on_google_href = (By.XPATH, "//a[contains(text(), 'See it on Google')]")


class HorizontalSliderLocators:
    main_url = "https://the-internet.herokuapp.com/horizontal_slider"
    title = (By.XPATH, "//h3[contains(text(), 'Horizontal Slider')]")
    slider = (By.XPATH, "//div[@class='sliderContainer']/input[@type='range']")
    slider_value = (By.ID, "range")


class HoversLocators:
    main_url = "https://the-internet.herokuapp.com/hovers"
    avatar = (By.XPATH, "//img[@alt='User Avatar']")
    hovered_part = (By.XPATH, "//div[@class='figcaption']/h5")


class InfiniteScrollLocators:
    main_url = "https://the-internet.herokuapp.com/infinite_scroll"
    scroll = (By.ID, "body")


class InputLocators:
    main_url = "https://the-internet.herokuapp.com/inputs"
    input_field = (By.XPATH, "//input[@type='number']")


class JQueryMenuLocators:
    main_url = "https://the-internet.herokuapp.com/jqueryui/menu"
    enabled = (By.LINK_TEXT, "Enabled")
    downloads = (By.LINK_TEXT, "Downloads")
    pdf = (By.LINK_TEXT, "PDF")


class JsAlertsLocators:
    main_url = "https://the-internet.herokuapp.com/javascript_alerts"
    alert_trigger = (By.XPATH, "//button[@onclick='jsAlert()']")
    confirm_trigger = (By.XPATH, "//button[@onclick='jsConfirm()']")
    prompt_trigger = (By.XPATH, "//button[@onclick='jsPrompt()']")
    result = (By.ID, "result")


class JsErrorLocators:
    main_url = "https://the-internet.herokuapp.com/javascript_error"


class KeyPressesLocators:
    main_url = "https://the-internet.herokuapp.com/key_presses"
    input_field = (By.ID, "target")
    result = (By.ID, "result")


class LargeDOMLocators:
    main_url = "https://the-internet.herokuapp.com/large"
    table = (By.ID, "large-table")


class MultipleWindowsLocators:
    main_url = "https://the-internet.herokuapp.com/windows"
    new_window_button = (By.XPATH, "//a[@href='/windows/new']")


class NotificationMessageLocators:
    main_url = "https://the-internet.herokuapp.com/notification_message_rendered"
    message = (By.XPATH, "//div[@id='flash']")
    reload_message_button = (By.XPATH, "//a[@href='/notification_message']")


class RedirectionLocators:
    main_url = "https://the-internet.herokuapp.com/redirector"
    redirect_button = (By.ID, "redirect")
    status_codes_url = "https://the-internet.herokuapp.com/status_codes"
    # status_codes_info = (By.LINK_TEXT, "http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml")
    status_codes_info = (By.XPATH, "//a[@href='http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml']")
    req_200 = (By.LINK_TEXT, "200")
    status_codes_200_title = (By.XPATH, "//p[contains(text(), 'This page returned a 200 status code.')]")
    req_301 = (By.LINK_TEXT, "301")
    status_codes_301_title = (By.XPATH, "//p[contains(text(), 'This page returned a 301 status code.')]")
    req_404 = (By.LINK_TEXT, "404")
    status_codes_404_title = (By.XPATH, "//p[contains(text(), 'This page returned a 404 status code.')]")
    req_500 = (By.LINK_TEXT, "500")
    status_codes_500_title = (By.XPATH, "//p[contains(text(), 'This page returned a 500 status code.')]")


class ShadowDOMLocators:
    main_url = "https://the-internet.herokuapp.com/shadowdom"
    paraps = (By.TAG_NAME, "my-paragraph")
    text_1 = (By.XPATH, "//*[@id='content']/my-paragraph[1]")
    text_2 = (By.XPATH, "//*[@id='content']/my-paragraph[2]")
    

class ShiftingContentLocators:
    main_url = "https://the-internet.herokuapp.com/shifting_content"
    menu_element_button = (By.LINK_TEXT, "Example 1: Menu Element")
    refresh_button = (By.XPATH, "//a[@href='/shifting_content/menu?mode=random&pixel_shift=100']")
    portfolio = (By.XPATH, "//a[@href='/portfolio/']")
    refreshed_menu_url = "https://the-internet.herokuapp.com/shifting_content/menu?mode=random&pixel_shift=100"
    image_button = (By.LINK_TEXT, "Example 2: An image")
    image = (By.XPATH, "//img[@class='shift']")
    refresh_image_button = (By.XPATH, "//a[@href='/shifting_content/image?mode=random&pixel_shift=100']")
    refreshed_img_url = "https://the-internet.herokuapp.com/shifting_content/image?mode=random&pixel_shift=100"
    list_button = (By.LINK_TEXT, "Example 3: List")
    list_page_title = (By.XPATH, "//div[@class='example']/h3")
    list_locator = (By.XPATH, "//div[@class='large-6 columns large-centered']")


class SlowResourcesLocators:
    main_url = "https://the-internet.herokuapp.com/slow"


class DataTablesLocators:
    main_url = "https://the-internet.herokuapp.com/tables"
    table_1 = (By.ID, "table1")
    table_2 = (By.ID, "table1")
    table_1_last_name = (By.XPATH, "//*[@id='table1']/thead/tr/th[1]")


class TyposLocators:
    main_url = "https://the-internet.herokuapp.com/typos"
    text = (By.XPATH, "//p")
