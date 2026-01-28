import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from datetime import timedelta
from selenium.webdriver.support.ui import WebDriverWait
import testdata
from Utils.utils import BaseClass
from pages.aeslogin import AesLogin
from pages.emaillogin import EmailLogin
from pages.login import Login
from pages.processcalling import Process_Calling
from testdata import logindata
from testdata.logindata import LoginData

# Agent to agent calling through process


class Agent_calling(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    # Locators for login
    page_heading = "//span[@class='lht_primary']"
    new_prof = "//span[@class='imoon icon-add']"
    login_username = "//input[@name='loginid']"
    login_password = "//input[@id='password']"
    login_click = "loginForm.Login"
    tel_register = "//div[@id='nav-telephone']//div[@class='terminal_register_boxin_header']"
    profile_div = "//app-agent-profile[@class='dash_profile']"
    extension_no = "//input[@placeholder='Terminal']"
    extension_name = "//input[@placeholder='Username']"
    extension_pass = "//input[@placeholder='Password']"
    extension_click = "//button[text()='Next']"
    terminal_check = f"//div[@class='terminal_extension_list']//a[normalize-space()='{LoginData.extn1}']"
    skip_btn = "//button[normalize-space()='Skip']"
    login_state = "//span[@class='LogIn profiler_btn_img']"
    camp_click = "//div[@class='interaction_indicators']"
    logged_in_state = "//span[@class='LogIn profiler_btn_img']//img[@alt='Profile']"
    dialog = "//ngb-modal-window[@role='dialog']"
    queue_join = f"(//div[contains(@class,'acs_content_grid_row')][.//div[@id='name' and normalize-space()='{LoginData.process_name}']]//app-switch//span[@class='slider'])[2]"
    process_join = f"//div[contains(@class,'acs_content_grid_row')][.//div[@id='name' and normalize-space()='{LoginData.process_name}']]//div[contains(@id,'Cheked')]//span[@class='slider']"
    unjoin_check = "//app-switch[@class='switch']//span[@class='slider']"
    unjoin = "//app-switch[@class='switch partial']"
    unjoin_check1 = "//app-switch[@class='switch partial']//span[@class='slider']"
    campaign_join = "//div[@id='Cheked0']//span[@class='slider']"
    toast = "//div[@class='ng-tns-c49-0 toast-message ng-star-inserted']"
    success_toast = "//div[contains(@class, 'toast-success')]"
    # success_toast = "//div[@class='ng-tns-c49-0 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-success toastr']"
    ready_state = "//span[normalize-space()='Ready']"
    ready_state_check = "//span[@class='profiler_btn_img Ready']"

    #Locators of agent transfer
    interaction_add = "//button[@id='newIntTrig1']"
    # interaction_add = "//span[@class='imoon icon-add ng-tns-c139-1']"
    dial_pad = "(//input[@placeholder='Enter Call Address'])[1]"
    dial_icon = "//button[@class='cridial_item_inputbtn me-1']"
    call_status_hover = "//div[@class='connected ng-star-inserted']"
    status_value = "(//div[@class='tooltip-inner'])[1]"
    agent_tab = '''(//li[@role='presentation']//a[contains(@class,'nav-link')])[2]'''
    agent_pannel = "//div[@class='item_blockin']"
    transfer = "(//button[@ngbtooltip='Transfer'])[2]"
    consult = "(//button[@ngbtooltip='Consult'])[2]"
    conference = "(//button[@ngbtooltip='Conference'])[2]"
    fly_note = '''(//textarea[@formcontrolname="agentNote"])[2]'''
    fly_note_check = "(//div[@class='anc_box ng-star-inserted'])//div[@class='col-9 px-2']//div[@class='anc_note_detail']//span"
    accept_btn = "//button[contains(text(),'Accept')]"
    hang_up = "//span[@class='imoon icon-call-end']"
    hold = "//button[@class='acts_btn p-0']"
    unhold = "//button[@class='acts_btn p-0 active']"
    inactive_hangup_btn = "//button[@type='button' and @ngbtooltip='Hangup' and contains(@class, 'intact_trig_btn') and @disabled]"
    hold_id = "//span[@class='imoon icon-hold']"
    submit_btn = "(//button[@type='submit'][normalize-space()='Submit'])[2]"
    consult_check = "//div[@class='agent_preview beta ng-star-inserted']//div[@class='agent_previewin']"
    # Locators for disposition
    disposition_click = "//span[normalize-space(text())='Answered']/parent::button"
    # disposition_click = "//button[@type='button']//span[@class='imoon icon-disposition']"
    dispostion_one = "//div[@class='intopt_schedulepad_body']//button[1]"
    # mark_done = "//button[.//span[contains(@class,'icon-markdone-close')]]"
    mark_done = "(//div[contains(@class,'int_opts')]//button[contains(@class,'int_opts_btn')])[1]"
    dispostion_tab = "//div[@class='intopt_schedulepad']"
    disp_ok_btn = "//button[@type='button'][normalize-space()='Ok']"
    consult_transfer_btn = "(//button[@ngbtooltip='Consult Transfer'])"
    consult_merge_btn = "//button[@ngbtooltip='Merge']"
    conference_txt = "(//span[contains(text(),'Conference')])[2]"

    # Locators for logout
    active_profile = "//span[@class='profiler_btn_img Ready']//img[@alt='Profile']"
    not_ready = "//span[normalize-space()='Break']"
    not_ready_reason = "//div[@id='Break']//ul[1]//li[1]"
    logout_btn = "//button[contains(text(),'Logout')]"
    logout_cause = "(//div[@class='reason_lists ng-star-inserted']//button)[1]"
    lg_out_btn = "(//span[text()='Logout'])"

    # For time manipulation
    current_time = datetime.now()
    past_time = current_time - timedelta(hours=1)
    time_stamp = current_time.strftime("%Y-%m-%d_%H_%M")
    print(past_time.strftime("%Y/%m/%d %H:%M:%S"))

    def agent2_login(self, log):
        try:
            time.sleep(2)
            # self.driver.execute_script("window.open()")
            # Switch to the newly opened tab
            self.driver.execute_script("window.open('about:blank', '_blank');")
            new_tab = self.driver.window_handles[-1]
            # self.driver.switch_to.window(self.driver.window_handles[1])
            # new_tab = self.driver.window_handles[-1]
            self.driver.switch_to.window(new_tab)
            time.sleep(1)
            # time.sleep(2)
            self.driver.get(LoginData.product_url)
            # action = ActionChains(self.driver)
            # action.send_keys(Keys.ENTER).perform()
            time.sleep(3)
            # self.driver.refresh()
            time.sleep(5)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, self.page_heading))
            )
            text1 = self.driver.find_element(By.XPATH, self.page_heading).text
            print(text1)
            assert text1 == 'Login'
            log.info("~Intello LogIn page Opened in different tab : Success")
        except:
            log.error("~Intello LogIn page Opened in different tab : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)Intello_login_page_open1.png")
        self.driver.implicitly_wait(30)
        time.sleep(10)
        # login of agent2
        try:
            WebDriverWait(self.driver, 30).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            self.driver.find_element(By.XPATH, self.new_prof).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.login_username).send_keys(LoginData.login_data1["username"])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.login_password).send_keys(LoginData.login_data1["password"])
            time.sleep(2)
            self.driver.find_element(By.ID, self.login_click).click()
            time.sleep(2)
            telreg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.tel_register))
            )
            assert telreg.is_displayed()
            log.info("~Agent (Call) LogIn in different tab : Success")
        except:
            log.error("~Agent (Call) LogIn in different tab : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)agent_login in different tab.png")
        try:
            WebDriverWait(self.driver, 50).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            time.sleep(4)
            self.driver.find_element(By.XPATH, self.extension_no).send_keys(LoginData.extn1)
            self.driver.find_element(By.XPATH, self.extension_name).send_keys(LoginData.extn1)
            self.driver.find_element(By.XPATH, self.extension_pass).send_keys(LoginData.extn1)
            self.driver.find_element(By.XPATH, self.extension_click).click()
            time.sleep(3)
            # self.driver.execute_script("alert('Hello, this is a JavaScript alert!');")
            # time.sleep(3)
            # a = self.driver.switchTo().alert()
            # a = Alert(self.driver)
            # a.accept()
            try:
                next = self.driver.find_element(By.XPATH, self.extension_click)
                if next.is_displayed():
                    next.click()
            except:
                print("Registered ")
            time.sleep(5)
            terminal = self.driver.find_element(By.XPATH, self.terminal_check)
            assert terminal.is_displayed()
            agent_state = self.driver.find_element(By.XPATH, self.login_state)
            assert agent_state.get_attribute("class") == "LogIn profiler_btn_img"
            log.info("~Agent2(Telephony channel) register in different tab : Success")
            # self.driver.camp_join(log)
        except:
            log.error("~Agent2(Telephony channel) register in different tab : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)telephone_register.png")
            self.driver.find_element(By.XPATH, self.skip_btn).click()
        # join process
        try:
            self.driver.find_element(By.XPATH, self.camp_click).click()
            time.sleep(3)
            unjoin_camp = self.driver.find_element(By.XPATH, self.unjoin_check)
            time.sleep(3)
            if unjoin_camp.is_displayed:
                time.sleep(2)
                # self.driver.find_element(By.XPATH, self.unjoin).click()
                # time.sleep(3)
                # self.driver.find_element(By.XPATH, self.campaign_join).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.queue_join).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.process_join).click()
                time.sleep(2)
            success = self.driver.find_element(By.XPATH, self.success_toast)
            assert success.is_displayed()
            log.info("~Agent process Join Un-join : Success")
        except:
            log.error("~Agent process Join Un-join : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)join_unjoin.png")
        self.driver.implicitly_wait(15)

        #agent ready
        try:
            btn = self.driver.find_element(By.XPATH, self.dialog)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.logged_in_state).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.ready_state).click()
            time.sleep(5)
            agent_ready = self.driver.find_element(By.XPATH, self.ready_state_check)
            assert agent_ready.is_displayed()
        except:
            print("Agent is unable to make ready")

    def markdone(self):
        try:
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            element1.click()
            wait = WebDriverWait(self.driver, 20)
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH,self.mark_done)))
            # btn = self.driver.find_element(By.XPATH, self.mark_done)
            btn.click()
            # self.driver.execute_script("arguments[0].click();", btn)
            # time.sleep(1)
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
        except Exception as e:
            print(f"Mark done process failed{e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}markdone.png")

    def agent_transfer(self, log):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(10)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                print("~Agent Dail an OutBound call from process : Success")
            self.driver.find_element(By.XPATH, self.agent_tab).click()
            time.sleep(2)
            # action = ActionChains(self.driver)
            # action.move_to_element(agent_pannel).perform()
            # time.sleep(2)
            self.driver.find_element(By.XPATH, self.agent_pannel).click()
            time.sleep(1)
            # action = ActionChains(self.driver)
            # action.move_to_element(pannel1).perform()
            # time.sleep(2)
            self.driver.find_element(By.XPATH, self.transfer).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.fly_note).send_keys(LoginData.transfer_note)
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.submit_btn).click()
            time.sleep(1)
            disp_tab = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            assert disp_tab.is_displayed()
            log.info("~Agent1 Transfer the call to agent2 in process : Success")
            self.markdone()
        except:
            log.error("~Agent to agent Transfer in process : FAIL")

        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.accept_btn).click()
            time.sleep(1)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                log.info("~Agent2 accept the transfer call : Success")
        except:
            log.error("~Agent2 accept the transfer call : FAIL")
        # check the fly note is appearing to agent 2
        try:
            note_check = self.driver.find_element(By.XPATH, self.fly_note_check).text
            time.sleep(1)
            print(note_check)
            assert note_check == LoginData.transfer_note
            log.info("~Transfer note is appearing to agent2 : Success")
        except:
            log.error("~Transfer note is appearing to agent2 : FAIL")

        #agent hang up
        try:
            self.driver.find_element(By.XPATH, self.hang_up).click()
            time.sleep(2)
            disp_tab = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            assert disp_tab.is_displayed()
            log.info("~Agent2 hang up the transfer call: Success")

        except:
            log.error("~Agent2 hang up the transfer call :FAIL")
        try:
            self.markdone()
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
            log.info("~Agent2 successfully mark done the transfer call : Success")
        except:
            log.error("~Agent2 successfully mark done the transfer call: FAIL")

    def logout(self, log):
        # logout
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
            log.info("~Logout : Success")
        except Exception as e:
            log.error("~Logout : Fail")
            print(f"logout fail{e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)logout.png")

    def agent_consult(self, log):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(6)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                print("~Agent Dail an OutBound call from process : Success")
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.agent_tab).click()
            time.sleep(2)
            # action = ActionChains(self.driver)
            # action.move_to_element(agent_pannel).perform()
            # time.sleep(2)
            self.driver.find_element(By.XPATH, self.agent_pannel).click()
            time.sleep(1)
            # action = ActionChains(self.driver)
            # action.move_to_element(pannel1).perform()
            # time.sleep(2)
            self.driver.find_element(By.XPATH, self.consult).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.fly_note).send_keys(LoginData.consult_transfer_note)
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.submit_btn).click()
            time.sleep(1)
            consult_call_check = self.driver.find_element(By.XPATH, self.consult_check)
            assert consult_call_check.is_displayed()
            # disp_tab = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            # assert disp_tab.is_displayed()
            print("~Agent1 consult the call to agent2 in process : Success")
        except:
            print("~Agent1 consult the call to agent2 in process : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent1 consult transfer the call to agent2 in process.png")

        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.accept_btn).click()
            time.sleep(1)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                print("~Agent2 accept the consult call : Success")
            # log.info("~Agent2 accept consult transfer the call to agent2 in process : Success")
            # self.markdone()
        except:
            print("~Agent2 accept the consult transfer call : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent2 accept the consult call.png")

    def consult_transfer(self,log):
        try:
            self.agent_consult(log)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.consult_transfer_btn).click()
            time.sleep(1)
            disp_tab = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            assert disp_tab.is_displayed()
            log.info("~Agent1 Consult Transfer the call to agent2 in process : Success")
            self.markdone()
        except:
            log.error("~Agent1 Consult Transfer the call to agent2 in process : Success")

        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            note_check = self.driver.find_element(By.XPATH, self.fly_note_check).text
            time.sleep(1)
            print(note_check)
            assert note_check == LoginData.consult_transfer_note
            log.info("~Consult Transfer note is appearing to agent2 : Success")
        except:
            log.error("~Consult Transfer note is appearing to agent2 : Success")
        try:
            self.driver.find_element(By.XPATH, self.hang_up).click()
            time.sleep(2)
            disp_tab = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            assert disp_tab.is_displayed()
            log.info("~Agent2 hang up the consult transfer call: Success")

        except:
            log.error("~Agent2 hang up the consult transfer call :FAIL")
        try:
            self.markdone()
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
            log.info("~Agent2 successfully mark done the consult transfer call : Success")
        except:
            log.error("~Agent2 successfully mark done the consult transfer call: FAIL")

    def agent_consult_merge(self,log):
        try:
            self.agent_consult(log)
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.accept_btn).click()
            time.sleep(1)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                log.info("~Agent2 accept the consult call : Success")
            # log.info("~Agent2 accept consult transfer the call to agent2 in process : Success")
            # self.markdone()
        except:
            log.error("~Agent2 accept the consult transfer call : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent2 accept the consult call.png")
        try:
            # self.agent_consult(log)
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.consult_merge_btn).click()
            time.sleep(1)
            # disp_tab = WebDriverWait(self.driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            # assert disp_tab.is_displayed()
            txt1 = self.driver.find_element(By.XPATH.conference_txt)
            assert txt1.is_diplayed()
            log.info("~Agent1 Consult conference the call to agent2 in process : Success")
            self.markdone()
        except:
            log.error("~Agent1 Consult conference the call to agent2 in process : Success")

        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            note_check = self.driver.find_element(By.XPATH, self.fly_note_check).text
            time.sleep(1)
            print(note_check)
            assert note_check == LoginData.consult_transfer_note
            log.info("~Consult conference note is appearing to agent2 : Success")
        except:
            log.error("~Consult conference note is appearing to agent2 : Success")
        try:
            self.driver.find_element(By.XPATH, self.hang_up).click()
            time.sleep(2)
            disp_tab = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            assert disp_tab.is_displayed()
            log.info("~Agent2 hang up the conference transfer call: Success")

        except:
            log.error("~Agent2 hang up the consult transfer call :FAIL")
        try:
            self.markdone()
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
            log.info("~Agent2 successfully mark done the consult transfer call : Success")
        except:
            log.error("~Agent2 successfully mark done the consult transfer call: FAIL")
        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.hang_up).click()
            time.sleep(2)
            disp_tab = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            assert disp_tab.is_displayed()
            self.markdone()
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
            log.info("~Agent1 successfully mark done the consult conference call : Success")
        except:
            log.error("~Agent2 successfully mark done the consult conference call: FAIL")

    def direct_conference(self,log):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(10)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                print("~Agent Dail an OutBound call from process : Success")
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.agent_tab).click()
            time.sleep(2)
            # action = ActionChains(self.driver)
            # action.move_to_element(agent_pannel).perform()
            # time.sleep(2)
            self.driver.find_element(By.XPATH, self.agent_pannel).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.conference).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.fly_note).send_keys(LoginData.conference_note)
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.submit_btn).click()
            time.sleep(1)
            txt1 = self.driver.find_element(By.XPATH.conference_txt)
            assert txt1.is_diplayed()
            log.info("~Agent1 conference the call to agent2 in process : Success")
        except:
            log.erro("~Agent1 conference the call to agent2 in process : Fail")
        # self.markdone()
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.accept_btn).click()
            time.sleep(1)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                log.info("~Agent2 accept the conference call : Success")
            log.info("~Agent2 accept conference the call to agent2 in process : Success")
        except:
            log.error("~Agent2 accept conference the call to agent2 in process : Fail")
        try:
            self.driver.find_element(By.XPATH, self.hang_up).click()
            time.sleep(2)
            disp_tab = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            assert disp_tab.is_displayed()
            log.info("~Agent2 hang up the conference call: Success")
            self.markdone()
        except:
            log.error("~Agent2 hang up the conference call: Fail")
        try:
            self.driver.switch_to.window(self.driver.window_handles[0])
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.hang_up).click()
            time.sleep(2)
            disp_tab = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            assert disp_tab.is_displayed()
            log.info("~Agent1 hang up the conference call: Success")
            self.markdone()
        except:
            log.error("~Agent1 hang up the conference call: Fail")

    def agent_activity(self):
        log = self.getLogger()
        try:
            login = Login(self.driver)
            login.login_task(log)
        except:
            print("Agent 1 login success")
        try:
            pc = Process_Calling(self.driver)
            pc.camp_join(log)
        except:
            print("Agent 1 join process")
        try:
            self.agent2_login(log)
        except:
            print("login fail")
        try:
            self.agent_transfer(log)
        except:
            print("Transfer fail")
        try:
            self.consult_transfer(log)
        except:
            print("Consult fail")
        try:
            self.agent_consult_merge(log)
        except:
            print("Consultmerge fail")
        try:
            self.direct_conference(log)
        except:
            print("Conference fail")
        try:
            self.logout(log)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.logout(log)
        except:
            print("logout fail")