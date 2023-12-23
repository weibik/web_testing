# Automated Testing of "The Internet" with Python Selenium and Pytest

**Automated testing of various pages on "The Internet" using Python Selenium and Pytest. The purpose of this project is to demonstrate how to perform end-to-end testing of a website with Selenium and Pytest, and to serve as a reference for setting up a testing environment with Poetry.**

**Prerequisites**
- poetry

**How to install poetry on windows?**
1. Install poetry (on windows powershell)\
      (Invoke-WebRequest -Uri ht<span>tps://install.python-poetry.org -UseBasicParsing).Content | py -)
2. add path to the windows environmental variables:\
      %APPDATA%\Python\Scripts

**Installation:**
1. Clone the repository:
  https://github.com/weibik/web_testing.git
2. Navigate to project directory 
  cd web_testing
3. run tests
   **poetry run python main.py -{test_class} -n {number of parallel runs}**

**Available test classes:**
- add_remove  
- basic_auth  
- broken_img  
- challenging_dom  
- checkboxes  
- context_menu  
- digest_auth  
- disappearing_elements  
- drag_and_drop  
- drop_down_list  
- dynamic_content  
- dynamic_controls  
- dynamic_loading  
- entry_ad  
- exit_intent  
- file_download  
- file_upload  
- floating_menu  
- form_auth  
- frames  
- geolocation  
- horizontal_slider  
- hovers  
- infinite_scroll  
- input  
- jquery_ui  
- js_alert  
- js_error  
- key_presses  
- large_DOM  
- main_page  
- multiple_windows  
- notification_message  
- redirector  
- shadow_dom  
- shifting_content  
- sortable_data_res  
- typos  




Example: **poetry run python main.py -add_remove -n 3**


