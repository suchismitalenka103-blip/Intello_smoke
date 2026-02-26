import os
import platform
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from testdata.logindata import LoginData
prefs = {
    "profile.managed_default_content_settings.images": 2,  # Disable images
    "profile.default_content_setting_values.media_stream_mic": 1,  # Allow mic
    "profile.default_content_setting_values.notifications": 2  # This sets the disk cache to use 0 bytes
}

# options = webdriver.ChromeOptions()
# options.add_argument('ignore-certificate-errors')
# options.add_experimental_option("prefs", prefs)
# options.add_argument('--disable-cache')
# options.add_argument('--disable-application-cache')
# options.add_argument("--disable-save-password-bubble")
# options.add_argument("--incognito")
# options.add_argument("--allow-insecure-localhost")
# prefs = {"profile.managed_default_content_settings.javascript": 1}
# options.add_experimental_option("prefs", prefs)
# options.add_argument("--allow-file-access-from-files")
# options.add_argument("--disable-web-security")
# options.add_argument("--allow-running-insecure-content")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--allow-file-access-from-files")
# options.add_argument("--disable-web-security")
# options.add_argument("--allow-file-access")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-features=IsolateOrigins,site-per-process")
# options.page_load_strategy = "none"
driver = None
# locators
detail_button = "details-button"
proceed_link = "proceed-link"
user_name = "loginId"
user_pass = "loginPword"
login_btn = "//button[normalize-space()='Login']"
chrome_args = [
    "--headless",  # Runs Chrome in headless mode (no GUI)
    "--no-sandbox",  # Required in many CI environments
    "--disable-gpu",  # Disable GPU acceleration
    "--disable-dev-shm-usage",  # Use /tmp instead of /dev/shm
    "--disable-extensions",  # Disable all extensions
    "--disable-popup-blocking",  # Disable popups
    "--ignore-certificate-errors",  # Ignore SSL errors
    "--disable-features=PasswordManagerUI,PasswordCheck",  # Disable password manager
    "--disable-background-networking",
    "--disable-sync",
    "--disable-translate",
    "--disable-background-timer-throttling",
    "--disable-client-side-phishing-detection",
    "--no-first-run",
    "--disable-blink-features=AutomationControlled",
]

@pytest.fixture(autouse=True)
def setup(request):
    global driver
    options = Options()
    for arg in chrome_args:
        options.add_argument(arg)
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.managed_default_content_settings.images": 1,
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.notifications": 2
    }

    # options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-cache")
    # options.add_argument("--disable-application-cache")
    # # options.add_argument("--incognito")
    # options.add_argument("--disable-features=PasswordManagerUI,PasswordCheck")
    # options.add_argument("--disable-save-password-bubble")
    # options.add_argument("--use-fake-ui-for-media-stream")
    # options.add_argument("user-data-dir=C:\\temp\\selenium_profile")
    # options.add_argument("--guest")
    # options.add_argument("--allow-insecure-localhost")
    # options.add_experimental_option("prefs", prefs)
    # prefs = {"profile.managed_default_content_settings.javascript": 1}
    # options.add_experimental_option("prefs", prefs)
    # options.add_argument("--allow-file-access-from-files")
    # options.add_argument("--disable-web-security")
    # options.add_argument("--allow-running-insecure-content")
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--allow-file-access-from-files")
    # options.add_argument("--disable-web-security")
    # options.add_argument("--allow-file-access")
    # options.add_argument("--disable-features=IsolateOrigins,site-per-process")
    # options.page_load_strategy = "none"
    # options = Options()

    driver = webdriver.Chrome(options=options)


    driver.maximize_window()
    request.cls.driver = driver
    # width = 1024
    # height = 768
    # driver.set_window_size(width, height)
    yield
    driver.quit()


def delete_cache(driver):
    driver.execute_script("window.open('');")  # Open new tab
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])  # Switch to new tab
    driver.get('chrome://settings/clearBrowserData')  # Navigate to clear browser data settings

    # Wait for the settings to load
    time.sleep(2)

    # Use ActionChains to send the right key combinations
    actions = ActionChains(driver)
    # Focus on the basic tab
    actions.send_keys(Keys.TAB * 3 + Keys.ENTER)
    # Select all time range and press tab to go to clear data button
    actions.send_keys(Keys.DOWN * 3 + Keys.TAB)
    actions.perform()

    # Confirm the action to clear data
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    time.sleep(10)  # Wait for the cache to be cleared
    driver.close()  # Close the settings tab
    driver.switch_to.window(driver.window_handles[0])  # Switch back to the original tab


# Example usage:
# driver = webdriver.Chrome()
# driver.get("https://www.example.com")
#
# delete_cache(driver)

# Proceed with other actions after cache deletion
# ...