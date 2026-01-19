import time
import os
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from datetime import timedelta

from Utils.utils import BaseClass
from testdata.logindata import LoginData


class ChatLogin(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    # Locators for agent login
    login_username = "LoginForm.username"
    login_password = "loginForm.password"
    login_click = "loginForm.Login"
    chat_register = "//div[@class='modal-content']//div[@class='terminal_register_boxin_header']"
    extension_no = "//input[@placeholder='Extension']"
    extension_name = "//input[@placeholder='Username']"
    extension_pass = "//input[@placeholder='Password']"
    extension_click = "//button[text()='Next']"
    chat_terminal_check = f"//div[@class='terminal_extension_list']//a[normalize-space()='{LoginData.chat_extn}']"
    toast = "//div[@class='ng-tns-c49-0 toast-message ng-star-inserted']"
    login_state = "//div[@class='LoggedIn status']"
    skip_btn = "//button[normalize-space()='Skip']"
    camp_click = "//div[@class='interaction_indicators']"
    unjoin_check = "//app-switch[@class='switch']//span[@class='slider']"
    unjoin = "//app-switch[@class='switch partial']"
    campaign_join = "//div[@id='Cheked0']//span[@class='slider']"
    logged_in_state = "//span[@class='LoggedIn profiler_btn_img']//img[@alt='Profile']"
    dialog = "//ngb-modal-window[@role='dialog']"
    # unjoin = "//app-switch[@class='switch partial']"
    # campaign_join = "//app-switch[@class='d-flex justify-content-end']//span[@class='slider']"
    success_toast = "//div[contains(@class, 'toast-success')]"
    ready_state = "//span[normalize-space()='Ready']"
    ready_state_check = "//span[@class='profiler_btn_img Ready']"

    # Locators for chat interaction
    accept_btn = "//button[normalize-space()='Accept']"
    chat_header = "//div[@class='chat_boxin_headerin']"
    chat_textbox = "//div[@role='textbox']"
    send_icon = "//span[@class='imoon icon-send']"
    text1 = "//span[@class='message_text ng-star-inserted']"
    hangup = "//span[@class='imoon icon-exit']"
    minimize_icon = "//span[@class='imoon icon-window-minimize']"
    sentiment = "//div[@class='sentiment_box']"
    scroll_page = "//div[@class='interaction_widgetsin']"
    sentiment_iframe = "(//iframe[1])[8]"
    exapand_icon = "//button[@class='misb_actions_btn']//span[@class='imoon icon-expand']"

    # Locators for disposition
    disposition_click = "//div[@class='dropdown-toggle blupper_wave cursor_pointer ng-star-inserted']"
    # disposition_click = "/button[@type='button']//span[@class='imoon icon-disposition']"
    dispostion_one = "(//button[@class='isml_tab_btn ng-star-inserted'])[1]"
    mark_done = "//div[@class='blupper_wave cursor_pointer ng-star-inserted']"
    dispostion_tab = "//div[@class='intopt_schedulepad']"
    disp_ok_btn = "//button[@type='button'][normalize-space()='Ok']"

    # Locators for logout
    active_profile = "//span[@class='profiler_btn_img Ready']//img[@alt='Profile']"
    not_ready = "//span[normalize-space()='NotReady']"
    not_ready_reason = "//div[@id='NotReady']//ul[1]//li[1]"
    logout_btn = "//button[contains(text(),'Logout')]"
    logout_cause = "(//div[@class='reason_lists ng-star-inserted']//button)[1]"
    lg_out_btn = "(//span[text()='Logout'])[2]"
    msg_box = "//div[@class='details']//span"

    # Locators for chat client
    client_textbox = "//input[@id='msg']"
    client_inputname = "//input[@id='name']"
    invite_btn = "//label[normalize-space()='Invite']"
    client_chat_send_btn = "//button[normalize-space()='SEND']"

    # Chat type
    postivie_chat = "Good"
    negative1 = "Fraud company"
    negative2 = "Worst"

    # assert for sentiment
    # neutral = "//div[@class='smiley_square neutral'] "
    sentiment_text = '''//div[@id="root"]//div[@class="realtime-sentiment"]//div[@class="sentiment_sense"]//span[contains(@class, "sense_state") and contains(@class, "text-capitalize")]'''
    sentiment_title = '''//span[@title="Session Start Time" and @class="start-time"]'''
    neutral = "//div[@class='realtime-sentiment']//div[@class='smiley_square neutral' and @title='Neutral']"
    positive = "//div[@id='root']//div[@class='sentiment_boxin']//div[@class='smiley_square positive']"
    negative = "//div[@class='realtime-sentiment']//div[@class='smiley_square negative' and @title='Negative']"

    # For time manipulation
    current_time = datetime.now()
    past_time = current_time - timedelta(hours=1)
    time_stamp = current_time.strftime("%Y-%m-%d_%H_%M")
    print(past_time.strftime("%Y/%m/%d %H:%M:%S"))

    # Locators for chat receive
    chat_get = "//div//div//span[@class='msg']"

    def chat_login(self, log):
        try:
            self.driver.get(LoginData.product_url)
            time.sleep(5)
            print("~Intello LogIn page Opened : Success")
        except:
            log.error("~Intello LogIn page Opened : FAIL")

        try:
            self.driver.find_element(By.ID, self.login_username).send_keys(LoginData.chat_login_data)
            time.sleep(2)
            self.driver.find_element(By.ID, self.login_password).send_keys(LoginData.chat_login_data)
            time.sleep(2)
            self.driver.find_element(By.ID, self.login_click).click()
            time.sleep(2)
            chatreg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.chat_register))
            )
            assert chatreg.is_displayed()
            log.info("~Agent (Chat) LogIn : Success")
        except:
            log.error("~Agent (Chat) LogIn : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat agent_login.png")

        try:
            time.sleep(4)
            self.driver.find_element(By.XPATH, self.extension_no).send_keys(LoginData.chat_extn)
            self.driver.find_element(By.XPATH, self.extension_name).send_keys(LoginData.chat_extn)
            self.driver.find_element(By.XPATH, self.extension_pass).send_keys(LoginData.chat_extn)
            self.driver.find_element(By.XPATH, self.extension_click).click()
            time.sleep(3)
            terminal = self.driver.find_element(By.XPATH, self.chat_terminal_check)
            time.sleep(4)
            assert terminal.is_displayed()
            agent_state = self.driver.find_element(By.XPATH, self.login_state)
            assert agent_state.get_attribute("class") == "LoggedIn status"
            log.info("~Agent(Chat channel) register : Success")
        except:
            log.error("~Agent(Chat channel) register : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat_register.png")
            self.driver.find_element(By.XPATH, self.skip_btn).click()

        try:
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.camp_click).click()
            time.sleep(2)
            unjoin_camp = self.driver.find_element(By.XPATH, self.unjoin_check)
            time.sleep(3)
            if unjoin_camp.is_displayed:
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.campaign_join).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.unjoin).click()
                time.sleep(6)
                self.driver.find_element(By.XPATH, self.campaign_join).click()
                time.sleep(2)
            success = self.driver.find_element(By.XPATH, self.success_toast)
            assert success.is_displayed()
            log.info("~Agent Campaign Join Un-join : Success")
        except:
            log.error("~Agent Campaign Join Un-join : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat_camp_join un_join.png")

        try:
            time.sleep(2)
            btn = self.driver.find_element(By.XPATH, self.dialog)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.logged_in_state).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.ready_state).click()
            time.sleep(2)
            agent_ready = self.driver.find_element(By.XPATH, self.ready_state_check)
            assert agent_ready.is_displayed()
            log.info("~Agent State change to Ready : Success")
        except:
            log.error("~Agent State change to Ready : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat agent State change to Ready.png")

    def chat_find(self, log):
        try:
            time.sleep(2)
            self.driver.execute_script("window.open()")
            # Switch to the newly opened tab
            self.driver.switch_to.window(self.driver.window_handles[1])
            # Navigate to new URL in new tab
            base_dir = Path(__file__).parent
            file_path = (base_dir / ".." / "testdata" / "testing-html.html").resolve()

            url = file_path.as_uri()  # <-- safely converts to file:/// format

            self.driver.get(url)
            try:
                wait = WebDriverWait(self.driver, 15)  # wait up to 15 seconds
                chat_icon = wait.until(
                    EC.presence_of_element_located((By.ID, "cd"))  # "cd" is the script ID
                )
                if chat_icon.is_enabled():
                    print("Chat icon is enabled!")
                else:
                    print("Chat icon is present but not enabled.")
            except:
                print("Chat icon not found or not loaded.")
            # self.driver.get(LoginData.chat_client_url)
            # time.sleep(10)
            # self.driver.find_element(By.XPATH, "//input[@id='address']").send_keys("BBSR")
            self.driver.find_element(By.XPATH, self.client_inputname).send_keys(LoginData.chat_name)
            # self.driver.find_element(By.XPATH, "//input[@id='cdn']").send_keys("DebitCard")
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.invite_btn).click()
            # self.driver.find_element(By.XPATH, "//label[normalize-space()='Invite']").click()
            # log.info("Request sent by Chat Client : Success")
            time.sleep(5)

            # Switch to original tab
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(1)
        except:
            log.error("~Agent chat client interaction : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat agent chat client interaction.png")

        try:
            accept = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, self.accept_btn)))
            accept.click()
            time.sleep(2)
            chat_header = self.driver.find_element(By.XPATH, self.chat_header)
            assert chat_header.is_displayed()
            log.info("~Agent accepts chat : Success")
        except:
            log.error("~Agent accepts chat : FAIL")
            # log.error("End chat ignore")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent accepts chat.png")

        try:
            self.driver.find_element(By.XPATH, self.chat_textbox).send_keys("Hy")
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.send_icon).click()
            time.sleep(2)
            text_check = self.driver.find_element(By.XPATH, self.text1).text
            assert text_check == "Hy"
            log.info("~Agent send chat reply : Success")
        except:
            log.error("~Agent send chat reply : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent send chat reply.png")
        # chat sentiment for positive chat
        try:
            self.driver.find_element(By.XPATH, self.minimize_icon).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_textbox).send_keys(self.postivie_chat)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_chat_send_btn).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            # self.driver.find_element(By.XPATH, self.minimize_icon).click()
            time.sleep(2)
            get = self.driver.find_element(By.XPATH, self.chat_get).text
            time.sleep(10)
            print(get)
            assert get == self.postivie_chat
            self.driver.find_element(By.XPATH, self.msg_box).click()
            time.sleep(2)
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.sentiment_iframe))
            )
            time.sleep(2)
            self.driver.switch_to.frame(iframe)
            time.sleep(2)
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.sentiment_text))
            )
            element = element1.text
            assert element == "Positive"
            log.info("~Positive chat sentiment is displaying : Success")
        except:
            log.error("~Positive chat sentiment is displaying : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Positive chat sentiment is displaying.png")
        # chat sentiment for neutral chat
        try:
            time.sleep(3)
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_textbox).send_keys(self.negative1)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_chat_send_btn).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            # self.driver.find_element(By.XPATH, self.minimize_icon).click()
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.msg_box).click()
            time.sleep(2)
            get = self.driver.find_element(By.XPATH, self.chat_get).text
            print(get)
            assert get == self.negative1
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.msg_box).click()
            time.sleep(10)
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.sentiment_iframe))
            )
            self.driver.switch_to.frame(iframe)
            element = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, self.sentiment_text))
            )
            sentiment_state = self.driver.execute_script('return arguments[0].textContent;', element).strip().lower()
            assert sentiment_state == "neutral"
            element = WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.XPATH, self.sentiment_title))
            )
            element_title = element.text
            print(element_title)
            assert element_title != '00:00'
            log.info("~Neutral chat sentiment is displaying : Success")

        except:
            log.error("~Neutral chat sentiment is displaying : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Neutral chat sentiment is displaying.png")

        # chat sentiment for neutral chat
        try:
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_textbox).send_keys(self.negative2)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_chat_send_btn).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.msg_box).click()
            time.sleep(10)
            get = self.driver.find_element(By.XPATH, self.chat_get).text
            print(get)
            assert get == self.negative2
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.msg_box).click()
            time.sleep(2)
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.sentiment_iframe))
            )
            self.driver.switch_to.frame(iframe)
            element = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, self.sentiment_text))
            )
            # sentiment_state = element.text.strip().lower()
            sentiment_state = self.driver.execute_script('return arguments[0].textContent;', element).strip().lower()
            assert sentiment_state == "negative"
            log.info("~Negative chat sentiment is displaying : Success")
        except:
            log.error("~Negative chat sentiment is displaying : FAIL")
            self.driver.save_screenshot(
                f"..\\screenshot\\{self.time_stamp}Negative chat sentiment is displaying.png")

        try:
            # time.sleep(2)
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.exapand_icon).click()
            time.sleep(2)
            btn = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, self.hangup))
            )
            btn.click()
            time.sleep(2)
            disp_tab = self.driver.find_element(By.XPATH, self.disposition_click)
            assert disp_tab.is_displayed()
            log.info("~Agent hang up chat : Success")
        except:
            log.error("~Agent hang up chat : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent hang up chat.png")
        try:
            self.driver.find_element(By.XPATH, self.disposition_click).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dispostion_one).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.mark_done).click()
            log.info("~Agent Disposition and Mark-Done : Success")
            log.info("End chat ignore")
        except:
            log.error("~Agent Disposition and Mark-Done : FAIL")
            # log.error("End chat ignore")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat agent Disposition and Mark-Done.png")

        try:
            time.sleep(7)
            self.driver.find_element(By.XPATH, self.active_profile).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.not_ready).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.not_ready_reason).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.logout_btn).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.logout_cause).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.lg_out_btn).click()
            time.sleep(7)
            log.info("End chat ignore")
        except:
            log.error("End chat ignore")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(chat)Logout.png")

    def chat_log_op(self):
        log = self.getLogger()
        # try:
        #     self.chat_login(log)
        # except:
        #     print("chat login fail")
        # try:
        self.chat_find(log)
        # except:
        #     print("chat interaction fail")
        log.info("End chat ignore")
