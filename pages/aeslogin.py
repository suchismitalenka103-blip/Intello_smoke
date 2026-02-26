from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from datetime import timedelta
from Utils.utils import BaseClass
from testdata.logindata import LoginData
import time


class AesLogin(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    # Locators for Aes login
    login_username = "LoginForm.username"
    login_password = "loginForm.password"
    login_click = "loginForm.Login"
    tel_register = "//div[@id='nav-telephone']//div[@class='terminal_register_boxin_header']"
    extension_no = "//input[@placeholder='Extension']"
    extension_name = "//input[@placeholder='Username']"
    extension_pass = "//input[@placeholder='Password']"
    extension_click = "//button[text()='Next']"
    terminal_check =  f"//div[@class='terminal_extension_list']//a[normalize-space()='{LoginData.aes_extn}']"
    skip_btn = "//button[normalize-space()='Skip']"
    login_state = "//div[@class='LoggedIn status']"
    camp_click = "//div[@class='interaction_indicators']"
    unjoin_check = "//app-switch[@class='switch']//span[@class='slider']"
    logged_in_state = "//span[@class='LoggedIn profiler_btn_img']//img[@alt='Profile']"
    dialog = "//ngb-modal-window[@role='dialog']"
    unjoin = "//app-switch[@class='switch partial']"
    campaign_join = "//div[@id='Cheked0']//span[@class='slider']"
    toast = "//div[@class='ng-tns-c49-0 toast-message ng-star-inserted']"
    success_toast = "//div[contains(@class, 'toast-success')]"
    # camp_success = "//div[@aria-label=f'aes_login_data{'username'} Campaign joined']"
    # success_toast = "//div[@class='ng-tns-c49-0 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-success toastr']"
    ready_state = "//span[normalize-space()='Ready']"
    ready_state_check = "//span[@class='profiler_btn_img Ready']"

    # Locators for interaction
    interaction_add ="//span[@class='imoon icon-add ng-tns-c136-1']"
    dial_pad = "(//input[@placeholder='Enter Number'])[1]"
    dial_icon = "//button[@class='cridial_item_inputbtn me-1 ng-tns-c136-1']"
    call_status_hover = "//div[@class='connected ng-star-inserted']"
    status_value = "(//div[@class='tooltip-inner'])[1]"
    hang_up = "//span[@class='imoon icon-call-end']"
    hold_unhold = "//span[@class='imoon icon-hold']"
    inactive_hangup_btn = "//button[@type='button' and @ngbtooltip='Hangup' and contains(@class, 'intact_trig_btn') and @disabled]"
    hold_id = "//span[@class='imoon icon-hold']"
    un_hold = "//button[@class='intact_acts_btn active']"

    # Locators for consult
    consult_click = "//button[@ngbtooltip='Consult' and @id = 'interactTelTransferTrig']"
    # dial_pad_tab = "//button[@id='pills-consult-dialpad-tab']//span[@class='imoon icon-keypad']"
    dial_pad_tab = "//div[@class='intact_acts ng-star-inserted']//li[2]"
    # consult_call_btn = "//button[@class='dial_trigger_btn'and @ngbtooltip='Consult']"
    consult_call_btn = "//button[@class='dial_trigger_btn']//span[@class='imoon icon-telephone']"
    merge = "//button[@ngbtooltip='Merge']"
    consult_transfer = "//button[@ngbtooltip='Consult Transfer']"
    consult_conf = "//span[@class='int_text']"
    input_number = "(//input[@placeholder='Enter Phone Number'])[2]"
    consult_hang_up = "//button[@ngbtooltip='Hangup' and @class = 'intact_trig_btn hangup ng-star-inserted']"

    # transfer
    transfer_icon = "//div[@class='intact_acts']//button[@id='interactTelTransferTrig']//span[@class='imoon icon-transfer']"
    transfer_dial_pad = "//button[@id='pills-transfer-dialpad-tab']"
    input_transfer = "(//input[@id='transferNumberInput' and @type='text'])[1]"
    transfer_call = "//button[@class='dial_trigger_btn']//span[@class='imoon icon-telephone']"

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

    # For time manipulation
    current_time = datetime.now()
    past_time = current_time - timedelta(hours=1)
    time_stamp = current_time.strftime("%Y-%m-%d_%H_%M")
    print(past_time.strftime("%Y/%m/%d %H:%M:%S"))

    def aes_login(self, log):
        try:
            self.driver.get(LoginData.product_url)
            # self.driver.execute_script("window.open('https://qa.radius.visnet.in/intello4/login/QARADIUS')")
            # self.driver.execute_script("window.location = '{}'".format(LoginData.product_url))
            WebDriverWait(self.driver, 20)
            log.info("~LogIn page displayed : Success")
        except:
            log.error("~LogIn page displayed : Fail")
        try:
            self.driver.implicitly_wait(10)
            self.driver.find_element(By.ID, self.login_username).send_keys(LoginData.aes_login_data["username"])
            time.sleep(5)
            self.driver.find_element(By.ID, self.login_password).send_keys(LoginData.aes_login_data["password"])
            time.sleep(5)
            self.driver.find_element(By.ID, self.login_click).click()
            time.sleep(5)
            telreg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.tel_register))
            )
            assert telreg.is_displayed()
            log.info("~Agent (Telephony) LogIn : Success")
        except:
            log.error("~Agent (Telephony) LogIn : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Telephony_login.png")
        try:
            html_content = self.driver.page_source
            print(html_content)
            time.sleep(7)
            self.driver.find_element(By.XPATH, self.extension_no).send_keys(LoginData.aes_extn)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.extension_name).send_keys(LoginData.aes_extn)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.extension_pass).send_keys(LoginData.aes_psw)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.extension_click).click()
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".d-flex.align-items-center.dash_profile_in"))
            )
            # toast = WebDriverWait(self.driver, 30).until(
            #     EC.presence_of_element_located((By.XPATH, self.toast))).text
            # print(toast)
            # assert toast == "Telephone terminal registered"
            # time.sleep(4)
            time.sleep(5)
            terminal = self.driver.find_element(By.XPATH, self.terminal_check)
            assert terminal.is_displayed()
            agent_state = self.driver.find_element(By.XPATH, self.login_state)
            assert agent_state.get_attribute("class") == "LoggedIn status"
            log.info("~Agent(Telephony channel) register : Success")
        except:
            log.error("~Agent(Telephony channel) register : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Telephony channel register.png")
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
            log.error("~Agent Campaign Join Un-join : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Agent Campaign Join Un-join.png")

        try:
            time.sleep(2)
            btn = self.driver.find_element(By.XPATH, self.dialog)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.logged_in_state).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.ready_state).click()
            time.sleep(5)
            agent_ready = self.driver.find_element(By.XPATH, self.ready_state_check)
            assert agent_ready.is_displayed()
            log.info("~Agent State change to Ready : Success")
        except:
            log.error("~Agent State change to Ready : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Agent State change to Ready.png")
            self.driver.find_element(By.XPATH, self.logged_in_state).click()
            time.sleep(2)

        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(8)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                log.info("~Agent Dail an OutBound call : Success")
            else:
                log.error("~Call : Failed")
                self.driver.find_element(By.XPATH, self.dispostion_one).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.mark_done).click()
        except:
            log.error("~Call : Failed")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Agent Dail an OutBound call.png")

    def hold_action(self, log):
        try:
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.hold_unhold).click()
            time.sleep(2)
            hold_check = self.driver.find_element(By.XPATH, self.inactive_hangup_btn)
            assert hold_check.is_displayed()
            log.info("~Agent Hold/Un-hold : Success")
        except Exception as e:
            print('test failed', format(e))
            log.error("~Agent Hold/Un-hold : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Agent Hold/Un-hold.png")

    def consult(self, log):
        try:
            time.sleep(4)
            # self.driver.find_element(By.XPATH, self.hold_unhold).click()
            btn = self.driver.find_element(By.XPATH, self.un_hold)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(4)
            # self.driver.find_element(By.XPATH, self.consult_click).click()
            btn = self.driver.find_element(By.XPATH, self.consult_click)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_pad_tab).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.input_number).send_keys(LoginData.test_mobile_one)
            time.sleep(6)
            self.driver.find_element(By.XPATH, self.consult_call_btn).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.merge).click()
            time.sleep(5)
            text1 = self.driver.find_element(By.XPATH, self.consult_conf).text
            print(text1)
            assert text1 == "Conference"
            log.info("~Agent Consult-Conference : Success")
        except:
            log.error("~Agent Consult-Conference : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Agent Consult-Conference.png")
        try:
            self.driver.find_element(By.XPATH, self.consult_hang_up).click()
            time.sleep(4)
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            element1.click()
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.dispostion_one)))
            # element = WebDriverWait(self.driver, 20).until(
            #     EC.presence_of_element_located((By.XPATH, self.dispostion_one)))
            # element.click()
            self.driver.execute_script("arguments[0].click();", element)
            self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.mark_done).click()
            time.sleep(1)
            # self.driver.find_element(By.XPATH, self.mark_done).click()
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
            log.info("~Mark done process : Success")
        except:
            log.error("~Mark done process : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Markdone.png")
        # Consult transfer
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(10)
            btn = self.driver.find_element(By.XPATH, self.consult_click)
            self.driver.execute_script("arguments[0].click();", btn)
            # self.driver.find_element(By.XPATH, self.consult_click).click()
            time.sleep(4)
            self.driver.find_element(By.XPATH, self.dial_pad_tab).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.input_number).send_keys(LoginData.test_mobile_one)
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.consult_call_btn).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.consult_transfer).click()
            time.sleep(5)
            disp_tab = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            # element = WebDriverWait(self.driver, 40).until(
            #     EC.presence_of_element_located((By.XPATH, self.dispostion_tab)))
            # disp_tab = self.driver.find_element(By.XPATH, self.dispostion_tab)
            assert disp_tab.is_displayed()
            log.info("~Agent Consult-Transfer : Success")
            self.markdone()
            # self.driver.find_element(By.XPATH, self.dispostion_one).click()
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, self.mark_done).click()
        except:
            log.error("~Agent Consult-Transfer : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Agent Consult-Transfer.png")

    def transfer(self, log):
        # Transfer
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(3)
            btn = self.driver.find_element(By.XPATH, self.transfer_icon)
            self.driver.execute_script("arguments[0].click();", btn)
            # self.driver.find_element(By.XPATH, self.transfer_icon).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.transfer_dial_pad).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.input_transfer).send_keys(LoginData.test_mobile_one)
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.transfer_call).click()
            time.sleep(3)
            disp_tab = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            # element = WebDriverWait(self.driver, 180).until(
            #     EC.presence_of_element_located((By.XPATH, self.dispostion_tab)))
            # disp_tab = self.driver.find_element(By.XPATH, self.dispostion_tab)
            assert disp_tab.is_displayed()
            # disp_tab = self.driver.find_element(By.XPATH, self.dispostion_tab)
            # assert disp_tab.is_displayed()
            log.info("~Agent Transfer (single-step) : Success")
            time.sleep(2)
            self.markdone()
            # self.driver.find_element(By.XPATH, self.dispostion_one).click()
            # time.sleep(1)
            # self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, self.mark_done).click()
        except:
            log.error("~Agent Transfer (single-step) : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Transfer(single-step).png")
            log.error("End Aes")

        # logout
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
            time.sleep(3)
        except:
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Aes)Logout.png")
            log.error("End Aes")

    def markdone(self):
        try:
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            # element1.click()
            self.driver.execute_script("arguments[0].click();", element1)
            element2 = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.dispostion_one)))
            # element2 = self.driver.find_element(By.XPATH, self.dispostion_one)
            self.driver.execute_script("arguments[0].click();", element2)
            self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.mark_done).click()
            time.sleep(1)
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
        except:
            print("Mark done process : failed")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}markdone.png")

    # main method
    def aes_login_op(self):
        log = self.getLogger()
        try:
            self.aes_login(log)
            time.sleep(10)
        except:
            print("Aes login fail")
            time.sleep(10)
        try:
            self.hold_action(log)
        except:
            print("Aes call hold fail")
        try:
            self.consult(log)
        except:
            print("Aes consult call fail")
        try:
            self.transfer(log)
        except:
            print("Aes tranfer fail")
        log.info("End Aes")
