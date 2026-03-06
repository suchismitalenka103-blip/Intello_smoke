import time
import os
from pathlib import Path

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
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
        self.wait = WebDriverWait(driver, 20)

    # Locators for agent login
    page_heading = "//span[@class='lht_primary']"
    login_username = "//input[@name='loginid']"
    login_password = "//input[@id='password']"
    login_click = "loginForm.Login"
    new_prof = "//span[@class='imoon icon-add']"
    chat_register = "//div[@class='modal-content']//div[@class='terminal_register_boxin_header']"
    extension_no = "//input[@placeholder='Terminal']"
    extension_name = "//input[@placeholder='Username']"
    extension_pass = "//input[@placeholder='Password']"
    extension_click = "//button[text()='Next']"
    chat_terminal_check = f"//div[@class='terminal_extension_list']//a[normalize-space()='{LoginData.chat_extn1}']"
    toast = "//div[@class='ng-tns-c49-0 toast-message ng-star-inserted']"
    login_state = "//span[@class='LogIn profiler_btn_img']"
    skip_btn = "//button[normalize-space()='Skip']"
    camp_click = "//div[@class='interaction_indicators']"
    queue_join = f"(//div[contains(@class,'acs_content_grid_row')][.//div[@id='name' and normalize-space()='{LoginData.process_name}']]//app-switch//span[@class='slider'])[2]"
    process_join = f"//div[contains(@class,'acs_content_grid_row')][.//div[@id='name' and normalize-space()='{LoginData.process_name}']]//div[contains(@id,'Cheked')]//span[@class='slider']"
    logged_in_state = "//span[@class='LogIn profiler_btn_img']//img[@alt='Profile']"
    dialog = "//ngb-modal-window[@role='dialog']"
    # unjoin = "//app-switch[@class='switch partial']"
    # campaign_join = "//app-switch[@class='d-flex justify-content-end']//span[@class='slider']"
    success_toast = "//div[contains(@class, 'toast-success')]"
    ready_state = "//span[normalize-space()='Ready']"
    ready_state_check = "//span[@class='profiler_btn_img Ready']"

    # Locators for chat interaction
    accept_btn = "//button[normalize-space()='Accept']"
    chat_header = "//div[@class='chat_boxin_headerin white_card']"
    chat_textbox = "//div[@role='textbox']"
    send_icon = "//span[@class='imoon icon-send']"
    text1 = "//span[contains(@class,'message_text')]"
    images_attachment = "(//app-chat-message//img)[last()]"
    hangup = "//span[@class='imoon icon-exit']"
    client_textbox = "//textarea[@id='msgChat']"
    minimize_icon = "//span[@class='imoon icon-window-minimize']"
    sentiment = "//div[@class='inside_circle']"
    sentiment_text = "//div[@class='tooltip-inner']"
    scroll_page = "//div[@class='interaction_widgetsin']"
    sentiment_iframe = "(//iframe[1])[8]"
    exapand_icon = "//button[@class='misb_actions_btn']//span[@class='imoon icon-expand']"

    # Locators for disposition
    disposition_click = "//span[normalize-space(text())='Answered']/parent::button"
    # disposition_click = "/button[@type='button']//span[@class='imoon icon-disposition']"
    dispostion_one = "(//button[@class='isml_tab_btn ng-star-inserted'])[1]"
    mark_done = "(//div[contains(@class,'int_opts')]//button[contains(@class,'int_opts_btn')])[1]"
    dispostion_tab = "//div[@class='intopt_schedulepad']"
    disp_ok_btn = "//button[@type='button'][normalize-space()='Ok']"

    # Locators for logout
    active_profile = "//span[@class='profiler_btn_img Ready']//img[@alt='Profile']"
    not_ready = "//span[normalize-space()='Break']"
    not_ready_reason = "//div[@id='Break']//ul[1]//li[1]"
    logout_btn = "//button[contains(text(),'Logout')]"
    logout_cause = "(//div[@class='reason_lists ng-star-inserted']//button)[1]"
    lg_out_btn = "(//span[text()='Logout'])"
    msg_box = "//div[@class='details']//span"

    # Locators for chat client
    client_name = "ContactAddress_ParentAttribute"
    client_inputname = "//input[@type='text' and @id='ContactAddress']"
    web_send_btn = "//input[@type='submit' and @id ='chatSubmit']"
    chat_btn = "//div[@id='eastChat2']//button"
    invite_btn = "//label[normalize-space()='Invite']"
    client_chat_send_btn = '''//button[@title='Send' and @id="submitPreChatForm"]'''

    # agent note
    fly_note = '''(//textarea[@formcontrolname="agentNote"])[2]'''
    fly_note_check = "(//div[@class='anc_box ng-star-inserted'])//div[@class='col-9 px-2']//div[@class='anc_note_detail']//span"
    submit_btn = "(//button[@type='submit'][normalize-space()='Submit'])[2]"

    # Chat type
    postivie_chat = "Good"
    nuetral = "this product is ok"
    negative2 = "Worst"
    transfer_Chat = "Transfer the chat to your senior"

    # assert for sentiment
    # neutral = "//div[@class='smiley_square neutral'] "
    # sentiment_text = '''//div[@id="root"]//div[@class="realtime-sentiment"]//div[@class="sentiment_sense"]//span[contains(@class, "sense_state") and contains(@class, "text-capitalize")]'''
    sentiment_title = '''//span[@title="Session Start Time" and @class="start-time"]'''
    neutral = "//div[@class='realtime-sentiment']//div[@class='smiley_square neutral' and @title='Neutral']"
    positive = "//div[@id='root']//div[@class='sentiment_boxin']//div[@class='smiley_square positive']"
    negative = "//div[@class='realtime-sentiment']//div[@class='smiley_square negative' and @title='Negative']"
    message_rcv = '''//div[@class="msgtext"]'''
    latest_msg_web = '''(//div[@class="msgtext"])[2]'''
    image_verify = "//div[contains(@class,'file-preview-agent')]//img"
    attachment = "UploadAttachment"
    customer_attachment = "attachmentInput"

    # For time manipulation
    current_time = datetime.now()
    past_time = current_time - timedelta(hours=1)
    time_stamp = current_time.strftime("%Y-%m-%d_%H_%M")
    print(past_time.strftime("%Y/%m/%d %H:%M:%S"))

    #locators for transfer
    transfer_icon = "//button[@id='interactTelTransferTrig']"
    transfer_agent = "(//li[contains(@class,'tlu_user')]//span[contains(@class,'agent_name')])[1]"

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
            WebDriverWait(self.driver, 50).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            WebDriverWait(self.driver, 20).until(
                        EC.visibility_of_element_located((By.XPATH, self.login_username))
                    )
            self.driver.find_element(By.XPATH, self.login_username).send_keys(LoginData.chat_login_data)
            self.driver.find_element(By.XPATH, self.login_password).send_keys(LoginData.chat_login_data)
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
            assert agent_state.get_attribute("class") == "LogIn profiler_btn_img"
            log.info("~Agent(Chat channel) register : Success")
        except:
            log.error("~Agent(Chat channel) register : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat_register.png")
            self.driver.find_element(By.XPATH, self.skip_btn).click()

    def process_join_fn(self,log):
        try:
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.camp_click).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.queue_join).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.process_join).click()
            time.sleep(2)
            success = self.driver.find_element(By.XPATH, self.success_toast)
            assert success.is_displayed()
            # success = self.driver.find_element(By.XPATH, self.success_toast)
            # assert success.is_displayed()
            log.info("~Agent Campaign Join Un-join : Success")
        except:
            log.error("~Agent Campaign Join Un-join : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat_camp_join un_join.png")

    def agent_ready(self, log):

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

    def markdone(self):
        try:
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            element1.click()
            wait = WebDriverWait(self.driver, 20)
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, self.mark_done)))
            # btn.click()
            self.driver.execute_script("arguments[0].click();", btn)
            # time.sleep(1)
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
        except Exception as e:
            print(f"Mark done process failed{e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}markdone.png")

    def chat_find(self, log):
        try:
            time.sleep(2)
            self.driver.execute_script("window.open()")
            # Switch to the newly opened tab
            self.driver.switch_to.window(self.driver.window_handles[-1])
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
        except:
            print("Chat icon not found or not loaded.")

        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.XPATH, self.chat_btn).click()
            time.sleep(1)
            self.driver.switch_to.frame("chatIframe")
            # element = self.driver.find_element(By.XPATH, self.client_inputname)
            # self.driver.execute_script(
            #     LoginData.chat_name, element
            # )

            self.driver.find_element(By.XPATH, self.client_inputname).send_keys(LoginData.chat_name)
            # self.driver.find_element(By.XPATH, "//input[@id='cdn']").send_keys("DebitCard")
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.web_send_btn).click()
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

    def sentiment_check(self, log):
        try:
            self.driver.find_element(By.XPATH, self.chat_textbox).send_keys("Hy")
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.send_icon).click()
            time.sleep(2)
            messages = self.driver.find_elements(By.XPATH, self.text1)
            latest_message = messages[-1].text.strip()
            print(latest_message)
            assert latest_message == "Hy"
            log.info("~Agent send chat reply : Success")
        except:
            log.error("~Agent send chat reply : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent send chat reply.png")
        # chat sentiment for positive chat
        try:
            # self.driver.find_element(By.XPATH, self.minimize_icon).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(2)
            self.driver.switch_to.frame("chatIframe")
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.client_textbox).send_keys(self.postivie_chat)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_chat_send_btn).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            # self.driver.find_element(By.XPATH, self.minimize_icon).click()
            time.sleep(2)

            messages = self.driver.find_elements(By.XPATH, self.text1)
            time.sleep(2)
            latest_message = messages[-1].text.strip()
            print(latest_message)
            assert latest_message == self.postivie_chat
            # self.driver.find_element(By.XPATH, self.msg_box).click()
            # time.sleep(2)
            sentiment_element1 = self.driver.find_element(By.XPATH, self.sentiment)
            action = ActionChains(self.driver)
            action.move_to_element(sentiment_element1).perform()
            # time.sleep(2)
            tooltip = self.driver.find_element(By.XPATH,self.sentiment_text).text
            print(tooltip)
            # value = self.driver.find_element(By.XPATH, self.status_value).text
            # ActionChains(self.driver).move_to_element(self.sentiment).perform()
            assert 'Positive' in tooltip
            # element = element1.text
            # assert element == "Positive"
            log.info("~Positive chat sentiment is displaying : Success")

        except:
            log.error("~Positive chat sentiment is displaying : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Positive chat sentiment is displaying.png")
        #chat reply
        try:
            self.driver.find_element(By.XPATH, self.chat_textbox).send_keys("Thank you")
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.send_icon).click()
            time.sleep(2)
            messages = self.driver.find_elements(By.XPATH, self.text1)
            latest_message1 = messages[-1].text.strip()
            print(latest_message1)
            assert latest_message1 == "Thank you"
        except:
            print("fail")
        # chat sentiment for neutral chat
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(1)
            self.driver.switch_to.frame("chatIframe")
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.client_textbox).send_keys(self.nuetral)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_chat_send_btn).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            # self.driver.find_element(By.XPATH, self.minimize_icon).click()
            messages = self.driver.find_elements(By.XPATH, self.text1)
            time.sleep(2)
            latest_message = messages[-1].text.strip()
            print(latest_message)
            assert latest_message == self.nuetral
            sentiment_element = self.driver.find_element(By.XPATH, self.sentiment)
            action = ActionChains(self.driver)
            action.move_to_element(sentiment_element).perform()
            # time.sleep(2)
            tooltip1 = self.driver.find_element(By.XPATH, self.sentiment_text).text
            print(tooltip1)
            assert 'Neutral' in tooltip1
            log.info("~Neutral chat sentiment is displaying : Success")

        except:
            log.error("~Neutral chat sentiment is displaying : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Neutral chat sentiment is displaying.png")
        # chat reply
        try:
            self.driver.find_element(By.XPATH, self.chat_textbox).send_keys("Why it is ok ok")
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.send_icon).click()
            time.sleep(2)
            messages = self.driver.find_elements(By.XPATH, self.text1)
            latest_message2 = messages[-1].text.strip()
            print(latest_message2)
            assert latest_message2 == "Why it is ok ok"
        except:
            print("fail")

        # chat sentiment for negative chat
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(1)
            self.driver.switch_to.frame("chatIframe")
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.client_textbox).send_keys(self.negative2)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_chat_send_btn).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            # self.driver.find_element(By.XPATH, self.minimize_icon).click()
            messages = self.driver.find_elements(By.XPATH, self.text1)
            time.sleep(2)
            latest_message3 = messages[-1].text.strip()
            print(latest_message3)
            assert latest_message3 == self.negative2
            sentiment_element = self.driver.find_element(By.XPATH, self.sentiment)
            action = ActionChains(self.driver)
            action.move_to_element(sentiment_element).perform()
            # time.sleep(2)
            tooltip2 = self.driver.find_element(By.XPATH, self.sentiment_text).text
            print(tooltip2)
            assert 'Negative' in tooltip2
            log.info("~Negative chat sentiment is displaying : Success")
            # assert sentiment_state == "negative"
        except:
            log.error("~Negative chat sentiment is displaying : FAIL")
            self.driver.save_screenshot(
                f"..\\screenshot\\{self.time_stamp}Negative chat sentiment is displaying.png")

        try:
            # time.sleep(2)
            self.driver.switch_to.default_content()
            time.sleep(1)
            # self.driver.find_element(By.XPATH, self.exapand_icon).click()
            # time.sleep(2)
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
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            # time.sleep(1)
            element1.click()
            wait = WebDriverWait(self.driver, 20)
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH, self.mark_done)))
            # btn.click()
            self.driver.execute_script("arguments[0].click();", btn)
            # self.driver.find_element(By.XPATH, self.mark_done).click()
            time.sleep(1)
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
            log.info("~Agent Disposition and Mark-Done : Success")
        except:
            log.error("~Agent Disposition and Mark-Done : FAIL")
            # log.error("End chat ignore")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat agent Disposition and Mark-Done.png")

    def logout(self, log):
        try:
            time.sleep(8)
            element = self.driver.find_element(By.XPATH, self.active_profile)
            time.sleep(2)
            if element.is_displayed():
                element = self.driver.find_element(By.XPATH, self.active_profile).click()
                self.driver.find_element(By.XPATH, self.not_ready).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.not_ready_reason).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.logout_btn).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.logout_cause).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.lg_out_btn).click()
                time.sleep(3)
            else:
                element1 = self.driver.find_element(By.XPATH, self.logged_in_state)
                assert element1.is_displayed()
                self.driver.find_element(By.XPATH, self.logged_in_state).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.logout_btn).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.logout_cause).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.lg_out_btn).click()
                time.sleep(3)
            log.info("~Chat agent Logout : Success")
        except Exception as e:
            log.error("~Chat agent Logout : Fail")
            print(f"logout fail{e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Chat)logout.png")

    def agent_login_newtab(self, log):
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.execute_script("window.open('about:blank', '_blank');")
            new_tab = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_tab)
            self.driver.get(LoginData.product_url)
            # self.driver.switch_to.window(new_tab)
            time.sleep(1)
            time.sleep(5)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, self.page_heading))
            )
            text1 = self.driver.find_element(By.XPATH, self.page_heading).text
            print(text1)
            assert text1 == 'Login'
            # time.sleep(5)
            log.info("~Agent (Chat) LogIn in different tab : Success")
        except:
            log.error("~Agent (Chat) LogIn in different tab : FAIL")
        try:
            WebDriverWait(self.driver, 30).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            self.driver.find_element(By.XPATH, self.new_prof).click()
            time.sleep(1)
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.login_username))
            )
            self.driver.find_element(By.XPATH, self.login_username).send_keys(LoginData.chat_login_data1)
            # time.sleep(2)
            self.driver.find_element(By.XPATH, self.login_password).send_keys(LoginData.chat_login_data1)
            # time.sleep(2)
            self.driver.find_element(By.ID, self.login_click).click()
            # time.sleep(2)
            telreg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.chat_register))
            )
            assert telreg.is_displayed()
            log.info("~Agent (Chat) LogIn in different tab : Success")
        except:
            log.error("~Agent (Chat) LogIn in different tab : FAIL")

        try:
            time.sleep(4)
            self.driver.implicitly_wait(20)
            self.driver.find_element(By.XPATH, self.extension_no).send_keys(LoginData.chat_extn1)
            self.driver.find_element(By.XPATH, self.extension_name).send_keys(LoginData.chat_extn1)
            self.driver.find_element(By.XPATH, self.extension_pass).send_keys(LoginData.chat_extn1)
            self.driver.find_element(By.XPATH, self.extension_click).click()
            time.sleep(3)
            terminal = self.driver.find_element(By.XPATH, self.chat_terminal_check)
            time.sleep(4)
            assert terminal.is_displayed()
            agent_state = self.driver.find_element(By.XPATH, self.login_state)
            assert agent_state.get_attribute("class") == "LogIn profiler_btn_img"
        except:
            log.error("~Agent(chat channel) register in another tab : Fail")
            # log.error("End email ignore : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent(Email channel) register.png")
            self.driver.find_element(By.XPATH, self.skip_btn).click()

    def accept_op(self, log):
        try:
            # self.driver.switch_to.window(self.driver.window_handles[1])
            # self.process_join_fn(log)
            # self.agent_ready(log)
            self.driver.switch_to.window(self.driver.window_handles[1])
            accept = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, self.accept_btn)))
            assert accept.is_displayed()
            accept.click()
            log.info("~chat land : Success")
        except NoSuchElementException:
            log.error("~chat land : FAIL")
            # log.error("End email ignore")
        except Exception as e:
            print(f"chat land : {e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat land.png")
        except TimeoutException:
            log.error("~Email land : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}chat land.png")

    def chat_transfer_message(self, log):
        try:
            self.driver.find_element(By.XPATH, self.chat_textbox).send_keys("Hello, How may i assist you today")
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.send_icon).click()
            time.sleep(2)
            messages = self.driver.find_elements(By.XPATH, self.text1)
            latest_message = messages[-1].text.strip()
            print(latest_message)
            assert latest_message == "Hello, How may i assist you today"
            print("~Agent send chat reply : Success")
        except:
            print("~Agent send chat reply : Fail")
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.switch_to.frame("chatIframe")
            time.sleep(1)
            text1 = self.driver.find_element(By.XPATH, self.message_rcv).text
            assert text1 == "Hello, How may i assist you today"
            log.info("~Message received by customer: Success")
        except:
            log.error("~Message received by customer: FAIL")
        try:
            self.driver.find_element(By.XPATH, self.client_textbox).send_keys(self.transfer_Chat)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.client_chat_send_btn).click()
            time.sleep(2)
            text1 = self.driver.find_element(By.XPATH, self.latest_msg_web).text
            assert text1 == self.transfer_Chat
            log.info("~Message send by customer: Success")
        except:
            log.error("~Message send by customer: FAIL")

        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            base_dir = Path(__file__).parent
            file_path = (base_dir / ".." / "testdata" / "background.jpg").resolve()
            file_input = self.driver.find_element(By.ID, self.attachment)
            file_input.send_keys(str(file_path))
            log.info("~Image attachment send by agent: Success")
        except:
            log.error("~Image attachment send by agent: FAIL")

        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.switch_to.frame("chatIframe")
            time.sleep(1)
            image_verify1 = self.driver.find_element(By.XPATH, self.image_verify)
            assert image_verify1.is_displayed()
            log.info("~Image attachment receive by customer: Success")
        except:
            log.error("~Image attachment receive by customer: FAIL")

        try:
            base_dir = Path(__file__).parent
            file_path1 = (base_dir / ".." / "testdata" / "background.jpg").resolve()
            file_input1 = self.driver.find_element(By.ID, self.customer_attachment)
            file_input1.send_keys(str(file_path1))
            log.info("~Image attachment send by customer: Success")
        except:
            log.error("~Image attachment send by customer: FAIL")

        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            images = self.driver.find_element(By.XPATH, self.images_attachment)
            print("Latest image src:", images.get_attribute("src"))
            assert images.is_displayed()
            log.info("~Image attachment receive by agent: Success")
        except:
            log.error("~Image attachment receive by agent: FAIL")
        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            base_dir = Path(__file__).parent
            file_path = (base_dir / ".." / "testdata" / "file1.xlsx").resolve()
            file_input = self.driver.find_element(By.ID, self.attachment)
            file_input.send_keys(str(file_path))
            log.info("~Excel attachment send by agent: Success")
        except:
            log.error("~Excel attachment send by agent: FAIL")

    def transfer_chat(self, log):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(10)
            self.driver.find_element(By.XPATH, self.camp_click).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.queue_join).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.process_join).click()
            time.sleep(2)
            success = self.driver.find_element(By.XPATH, self.success_toast)
            assert success.is_displayed()
            log.info("~Process join in agent2 side : Success")
        except:
            log.error("~Process join in agent2 side : FAIL")
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
            log.info("~Agent2 State change to Ready : Success")
        except:
            log.error("~Agent2 State change to Ready : FAIL")
        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.driver.find_element(By.XPATH, self.transfer_icon).click()
            transfer_agent = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.transfer_agent)))
            transfer_agent.click()
            self.driver.find_element(By.XPATH, self.fly_note).send_keys(LoginData.chat_transfer_note)
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.submit_btn).click()
            time.sleep(1)
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            assert element1.is_displayed()
            log.info("~Chat Transfer : Success")
        except:
            log.error("~Chat Transfer : FAIL")
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            accept = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, self.accept_btn)))
            assert accept.is_displayed()
            accept.click()
            log.info("~Chat land to agent2 after Transfer : Success")
        except:
            log.error("~Chat land to agent2 after Transfer : FAIL")
        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            self.markdone()
            log.info("~Mark done after Transfer : Success")
        except:
            log.error("~Mark done after Transfer : FAIL")
    # def agent2_(self, log):

    #smoke test
    def chat_log_op(self):
        log = self.getLogger()
        try:
            self.chat_login(log)
        except:
            print("chat login fail")
        try:
            self.process_join_fn(log)
        except:
            print("process join fail")
        try:
            self.agent_ready(log)
        except:
            print("agent ready fail")
        try:
          self.chat_find(log)
        except:
            print("chat interaction fail")
        try:
            self.sentiment_check(log)
        except:
            print("sentiment check fail")
        # log.info("End chat ignore")
        # try:
        #     self.logout(log)
        # except:
        #     print("chat logout fail")
        try:
            self.agent_login_newtab(log)
        except:
            print("chat login in another tab")
        try:
          self.chat_find(log)
        except:
            print("chat interaction fail")
        try:
            self.chat_transfer_message(log)
        except:
            print("chat transfer message")
        try:
            self.transfer_chat(log)
        except:
            print("chat transfer fail")
