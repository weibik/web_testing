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
