import time
from datetime import timedelta, datetime

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.utils import BaseClass
from testdata.atomosdata import Data
from testdata.logindata import LoginData


class Atomos(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    #Locators login logout
    # LOCATORS COMMON
    user_name = "//input[@placeholder='Username']"
    password = "//input[@placeholder='Password']"
    login_btn = "//button[@id='saveButton']"

    # For time manipulation
    current_time = datetime.now()
    past_time = current_time - timedelta(hours=1)
    time_stamp = current_time.strftime("%Y-%m-%d_%H_%M")
    print(past_time.strftime("%Y/%m/%d %H:%M:%S"))

    # media locators
    media_play_view = "(//li[@id='Media Server']//div[contains(@class, 'col-md-2')])[5]"
    aes_start = '''//tr[td[2][contains(text(), 'AES')] and td[@ng-if="teleData.xsrvrStatus === 'InService'"]]'''
    crossx_start = '''//tr[td[2][contains(text(), 'CrossX')] and td[@ng-if="teleData.xsrvrStatus === 'InService'"]]'''
    chat_start = '''//tr[td[2][contains(text(), 'RUSC')] and td[@ng-if="teleData.xsrvrStatus === 'InService'"]]'''
    email_start = '''//tr[td[2][contains(text(), 'REMA')] and td[@ng-if="teleData.xsrvrStatus === 'InService'"]]'''
    email_stop = '''//tr[td[normalize-space(text())='REMA'] and .//span[@title='Start' and @ng-if="teleData.xsrvrStatus === 'Shutdown'"]]'''
    aes_stop = '''//tr[td[normalize-space(text())='AES'] and .//span[@title='Start' and @ng-if="teleData.xsrvrStatus === 'Shutdown'"]]'''
    crossx_stop = '''//tr[td[normalize-space(text())='CrossX'] and .//span[@title='Start' and @ng-if="teleData.xsrvrStatus === 'Shutdown'"]]'''
    media_start = "//span[@title='Start']//*[name()='svg']"
    chat_stop = '''//tr[td[normalize-space(text())='RUSC'] and .//span[@title='Start' and @ng-if="teleData.xsrvrStatus === 'Shutdown'"]]'''
    #Campaign
    campaign_play = "//li[@id='Campaign']//div[5]"
    search = "//input[@placeholder='Search by name']"
    campaign_check = "//table[@class='table table-striped no-padding custom_table margin_bottom_0 ng-isolate-scope']//tr/td[6]//i[1]"
    start = "//i[@title='Start']"
    stop = "//i[@title='Load']//*[name()='svg']"
    start_fn = "//i[@title='Load']"
    load_fn = "//i[@title='Start']"
    start_btn = "//button[normalize-space()='Start']"
    toast_msg = "//div[@class='toast-message']"
    camp_check = "//i[@class='right-menu cursor_pointer padding5']"

    def login(self, log):
    # login with valid creds
        try:
            time.sleep(1)
            self.driver.get(Data.product_url)
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.user_name).send_keys(Data.login_data['username'])
            self.driver.find_element(By.XPATH, self.password).send_keys(Data.login_data['password'])
            self.driver.find_element(By.XPATH, self.login_btn).click()
            time.sleep(5)
            url = self.driver.current_url
            assert url == Data.home_page
            print("~Admin Login with valid credentials : Pass")
        except:
            print("~Admin Login with valid credentials : Fail")
            self.driver.save_screenshot(
                f"..\\screenshot\\{self.time_stamp}Admin Login with valid credentials.png")

    def mediaserver(self, log):
        try:
            time.sleep(2)
            # self.driver.find_element(By.XPATH, self.media_play_view).click()
            btn1 = self.driver.find_element(By.XPATH, self.media_play_view)
            btn1.click()
            # self.driver.execute_script("arguments[0].click();", btn1)
            time.sleep(5)
            # time.sleep(1)
            start_aes = self.driver.find_element(By.XPATH, self.aes_start)
            # stop_aes = self.driver.find_element(By.XPATH, self.aes_stop)
            if start_aes.is_displayed():
                time.sleep(2)
                print("Aes Server is already started")
            # elif self.driver.find_element(By.XPATH, self.aes_stop).is_displayed():
            #     time.sleep(2)
            #     self.driver.find_element(By.XPATH, self.search).send_keys(Data.aes_server)
            #     time.sleep(1)
            #     self.driver.find_element(By.XPATH, self.start).click()
            #     toast = self.driver.find_element(By.XPATH, self.toast_msg)
            #     toast.is_displayed()
            #     print("Media server is started")
        except NoSuchElementException:
            stop_aes = self.driver.find_element(By.XPATH, self.aes_stop)
            if stop_aes.is_displayed():
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.search).send_keys(Data.aes_server)
                time.sleep(1)
                action = ActionChains(self.driver)
                action.send_keys(Keys.ENTER).perform()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.media_start).click()
                time.sleep(2)
                toast = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, self.toast_msg))
                )
                # toast = self.driver.find_element(By.XPATH, self.toast_msg)
                toast.is_displayed()
                print("Aes Media server is now started")

        try:
            # self.driver.find_element(By.XPATH, self.campaign_play).click()
            btn = self.driver.find_element(By.XPATH, self.campaign_play)
            # self.driver.execute_script("arguments[0].click();", btn)
            btn.click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.search).send_keys(Data.aes_campaign)
            time.sleep(1)
            action = ActionChains(self.driver)
            action.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            # check = self.driver.find_element(By.XPATH, self.campaign_check).get_title
            # print(check)
            # check = self.driver.find_element(By.XPATH, self.start)
            # check1 = self.driver.find_element(By.XPATH, self.stop)
            check = self.driver.find_element(By.XPATH, self.camp_check)
            check1 = check.get_attribute("title")
            print(check1)
            if check1 == "Stop":
                print("Aes Campaign is already started")
            elif self.driver.find_element(By.XPATH, self.stop).is_displayed():
                # print("fail")
                self.driver.find_element(By.XPATH, self.start_fn).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.load_fn).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.start_btn).click()
                time.sleep(2)
                toast = self.driver.find_element(By.XPATH, self.toast_msg)
                toast.is_displayed()
                print("Aes Campaign running now successfully")

        except:
            print("Aes Campaign running Fail")

    # crossx media server
    def crossx_check(self, log):
        try:
            self.driver.refresh()
            self.login(log)
            time.sleep(2)
            btn1 = self.driver.find_element(By.XPATH, self.media_play_view)
            btn1.click()
            time.sleep(5)
            start_crossx = self.driver.find_element(By.XPATH, self.crossx_start)
            if start_crossx.is_displayed():
                time.sleep(2)
                print("Crossx Server is already started")
        except NoSuchElementException:
            stop_crossx = self.driver.find_element(By.XPATH, self.crossx_stop)
            # print("fail media")
            if stop_crossx.is_displayed():
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.search).send_keys(Data.crossx_server)
                time.sleep(1)
                action = ActionChains(self.driver)
                action.send_keys(Keys.ENTER).perform()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.media_start).click()
                time.sleep(2)
                toast = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, self.toast_msg))
                )
                # toast = self.driver.find_element(By.XPATH, self.toast_msg)
                toast.is_displayed()
                print("Crossx Media server is now started")
        try:
            # self.driver.find_element(By.XPATH, self.campaign_play).click()
            btn = self.driver.find_element(By.XPATH, self.campaign_play)
            # self.driver.execute_script("arguments[0].click();", btn)
            btn.click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.search).send_keys(Data.crossx_campaign)
            time.sleep(1)
            action = ActionChains(self.driver)
            action.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            # check = self.driver.find_element(By.XPATH, self.campaign_check).get_title
            # print(check)
            # check = self.driver.find_element(By.XPATH, self.start)
            # check1 = self.driver.find_element(By.XPATH, self.stop)
            check = self.driver.find_element(By.XPATH, self.camp_check)
            check1 = check.get_attribute("title")
            print(check1)
            if check1 == "Stop":
                print("crossx Campaign is already started")
            elif self.driver.find_element(By.XPATH, self.stop).is_displayed():
                # print("fail")
                self.driver.find_element(By.XPATH, self.start_fn).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.load_fn).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.start_btn).click()
                time.sleep(2)
                toast = self.driver.find_element(By.XPATH, self.toast_msg)
                toast.is_displayed()
                print("crossx Campaign is running now successfully")
        except:
            print("Crossx campaign running Fail")

    def email_check(self, log):
        try:
            self.driver.refresh()
            self.login(log)
            time.sleep(2)
            btn1 = self.driver.find_element(By.XPATH, self.media_play_view)
            btn1.click()
            time.sleep(5)
            start_email = self.driver.find_element(By.XPATH, self.email_start)
            if start_email.is_displayed():
                time.sleep(2)
                print("Email Server is already started")
        except NoSuchElementException:
            stop_email = self.driver.find_element(By.XPATH, self.email_stop)
            # print("fail media")
            if stop_email.is_displayed():
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.search).send_keys(Data.email_server)
                time.sleep(1)
                action = ActionChains(self.driver)
                action.send_keys(Keys.ENTER).perform()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.media_start).click()
                time.sleep(2)
                toast = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, self.toast_msg))
                )
                # toast = self.driver.find_element(By.XPATH, self.toast_msg)
                toast.is_displayed()
                print("Email Media server is started now")
        try:
            # self.driver.find_element(By.XPATH, self.campaign_play).click()
            btn = self.driver.find_element(By.XPATH, self.campaign_play)
            # self.driver.execute_script("arguments[0].click();", btn)
            btn.click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.search).send_keys(Data.email_campaign)
            time.sleep(1)
            action = ActionChains(self.driver)
            action.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            # check = self.driver.find_element(By.XPATH, self.campaign_check).get_title
            # print(check)
            # check = self.driver.find_element(By.XPATH, self.start)
            # check1 = self.driver.find_element(By.XPATH, self.stop)
            check = self.driver.find_element(By.XPATH, self.camp_check)
            check1 = check.get_attribute("title")
            print(check1)
            if check1 == "Stop":
                print("Email Campaign is already started")
            else:
                self.driver.find_element(By.XPATH, self.start_fn).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.load_fn).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.start_btn).click()
                time.sleep(2)
                toast = self.driver.find_element(By.XPATH, self.toast_msg)
                toast.is_displayed()
                print("Email Campaign is running successfully now")
        except:
            print("Email campaign running Fail")

    def chat_check(self, log):
        try:
            self.driver.refresh()
            self.login(log)
            time.sleep(2)
            btn1 = self.driver.find_element(By.XPATH, self.media_play_view)
            btn1.click()
            time.sleep(5)
            start_chat = self.driver.find_element(By.XPATH, self.chat_start)
            if start_chat.is_displayed():
                time.sleep(2)
                print("Chat Server is already started")
        except NoSuchElementException:
            stop_chat = self.driver.find_element(By.XPATH, self.chat_stop)
            # print("fail media")
            if stop_chat.is_displayed():
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.search).send_keys(Data.chat_server)
                time.sleep(1)
                action = ActionChains(self.driver)
                action.send_keys(Keys.ENTER).perform()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.media_start).click()
                time.sleep(2)
                toast = WebDriverWait(self.driver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, self.toast_msg))
                )
                # toast = self.driver.find_element(By.XPATH, self.toast_msg)
                toast.is_displayed()
                print("Chat Media server is started now")
        try:
            # self.driver.find_element(By.XPATH, self.campaign_play).click()
            btn = self.driver.find_element(By.XPATH, self.campaign_play)
            # self.driver.execute_script("arguments[0].click();", btn)
            btn.click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.search).send_keys(Data.chat_campaign)
            time.sleep(1)
            action = ActionChains(self.driver)
            action.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            # check = self.driver.find_element(By.XPATH, self.campaign_check).get_title
            # print(check)
            # check = self.driver.find_element(By.XPATH, self.start)
            # check1 = self.driver.find_element(By.XPATH, self.stop)
            check = self.driver.find_element(By.XPATH, self.camp_check)
            check1 = check.get_attribute("title")
            print(check1)
            if check1 == "Stop":
                print("Chat Campaign is already started")
            else:
                # print("fail")
                self.driver.find_element(By.XPATH, self.start_fn).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.load_fn).click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, self.start_btn).click()
                time.sleep(2)
                toast = self.driver.find_element(By.XPATH, self.toast_msg)
                toast.is_displayed()
                print("chat Campaign is running now successfully")
        except:
            print("Chat campaign running Fail")

    def main_atomos(self):
        log = self.getLogger()
        self.login(log)
        try:
            self.mediaserver(log)
        except:
            print("Issue is in aes")
        try:
            self.crossx_check(log)
        except:
            print("Issue is in crossx")
        try:
            self.email_check(log)
        except:
            print("Issue is in email")
        try:
            self.chat_check(log)
        except:
            print("Issue is in chat")

