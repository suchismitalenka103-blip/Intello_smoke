import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome import webdriver
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
from testdata import logindata
from testdata.logindata import LoginData


class Process_Calling(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    # Locators for login
    page_heading = "//span[@class='lht_primary']"
    login_username = "//input[@name='loginid']"
    login_password = "//input[@id='password']"
    login_click = "loginForm.Login"
    tel_register = "//div[@id='nav-telephone']//div[@class='terminal_register_boxin_header']"
    profile_div = "//app-agent-profile[@class='dash_profile']"
    extension_no = "//input[@placeholder='Terminal']"
    extension_name = "//input[@placeholder='Username']"
    extension_pass = "//input[@placeholder='Password']"
    extension_click = "//button[text()='Next']"
    terminal_check =  f"//div[@class='terminal_extension_list']//a[normalize-space()='{LoginData.extn}']"
    skip_btn = "//button[normalize-space()='Skip']"
    login_state = "//span[@class='LogIn profiler_btn_img']"
    camp_click= "//div[@class='interaction_indicators']"
    queue_join = f"(//div[contains(@class,'acs_content_grid_row')][.//div[@id='name' and normalize-space()='{LoginData.process_name}']]//app-switch//span[@class='slider'])[2]"
    process_join = f"//div[contains(@class,'acs_content_grid_row')][.//div[@id='name' and normalize-space()='{LoginData.process_name}']]//div[contains(@id,'Cheked')]//span[@class='slider']"
    logged_in_state = "//span[@class='LogIn profiler_btn_img']//img[@alt='Profile']"
    break_loggedin = "//span[@class='profiler_btn_img LogIn']"
    dialog = "//ngb-modal-window[@role='dialog']"
    unjoin_check = "//app-switch[@class='switch']//span[@class='slider']"
    unjoin_check1 = "//app-switch[@class='switch partial']//span[@class='slider']"
    unjoin = "//app-switch[@class='switch partial']"
    campaign_join = "//div[@id='Cheked0']//span[@class='slider']"
    toast = "//div[@class='ng-tns-c49-0 toast-message ng-star-inserted']"
    success_toast = "//div[contains(@class, 'toast-success')]"
    # success_toast = "//div[@class='ng-tns-c49-0 ng-star-inserted ng-trigger ng-trigger-flyInOut ngx-toastr toast-success toastr']"
    ready_state = "//span[normalize-space()='Ready']"
    ready_state_check = "//span[@class='profiler_btn_img Ready']//img[@alt='Profile']"
    break_icon = "//span[@class='content']"
    break_reason = "(//button[@container='body'])[1]"
    break_state_check = "//span[@class='profiler_btn_img Break']"
    login_pop_up = "//button[normalize-space()='Login']"
    # Locators for interaction
    interaction_add = "//button[@id='newIntTrig1']"
    # interaction_add = "//span[@class='imoon icon-add ng-tns-c139-1']"
    dial_pad = "(//input[@placeholder='Enter Call Address'])[1]"
    dial_icon = "//button[@class='cridial_item_inputbtn me-1']"
    call_status_hover = "//div[@class='connected ng-star-inserted']"
    status_value = "(//div[@class='tooltip-inner'])[1]"
    hang_up = "//span[@class='imoon icon-call-end']"
    hold = "//button[@class='acts_btn p-0']"
    unhold = "//button[@class='acts_btn p-0 active']"
    inactive_hangup_btn = "//button[@type='button' and @ngbtooltip='Hangup' and contains(@class, 'intact_trig_btn') and @disabled]"
    hold_id = "//span[@class='imoon icon-hold']"

    # Locators for consult
    consult_click = "//button[@ngbtooltip='Consult' and @id = 'interactTelTransferTrig']"
    dial_pad_tab = "(//span[@class='imoon icon-keypad'])[2]"
    # consult_call_btn = "//input[@id='consultNumberInput']"
    consult_call_btn = "//span[@class='imoon icon-consult']"
    merge = "//button[@ngbtooltip='Merge']"
    consult_transfer = "//button[@ngbtooltip='Consult Transfer']"
    consult_conf = "(//span[contains(text(),'Conference')])[2]"
    input_number = "//input[@id='dialpadinput']"
    consult_hang_up = "//button[@ngbtooltip='Hangup' and @class = 'intact_trig_btn hangup ng-star-inserted']"

    # Locators for disposition
    disposition_click = "//span[normalize-space(text())='Answered']/parent::button"
    # disposition_click = "//button[@type='button']//span[@class='imoon icon-disposition']"
    dispostion_one = "//div[@class='intopt_schedulepad_body']//button[1]"
    mark_done = "(//div[contains(@class,'int_opts')]//button[contains(@class,'int_opts_btn')])[1]"
    dispostion_tab = "//div[@class='intopt_schedulepad']"
    disp_ok_btn = "//button[@type='button'][normalize-space()='Ok']"

    # transfer
    transfer_icon = "//span[@class='imoon icon-transfer']"
    transfer_dial_pad = "//button[@id='pills-transfer-dialpad-tab']"
    input_transfer = "//input[@id='transferNumberInput']"
    transfer_call = "//button[@class='dial_trigger_btn']//span[@class='imoon icon-telephone']"

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

    def camp_join(self, log):
        # camp join un join
        # try:
        #     # Login.login_task(log)
        #     WebDriverWait(self.driver, 20).until(
        #         EC.invisibility_of_element_located((By.XPATH, self.mark_done))
        #     )
        #     agent_ready = self.driver.find_element(By.XPATH, self.ready_state_check)
        #     if agent_ready.is_displayed():
        #         self.driver.find_element(By.XPATH, self.ready_state_check).click()
        #         time.sleep(2)
        #         self.driver.find_element(By.XPATH, self.break_icon).click()
        #         time.sleep(2)
        #         self.driver.find_element(By.XPATH, self.break_reason).click()
        #         time.sleep(1)
        #         self.driver.find_element(By.XPATH, self.login_pop_up).click()
        #         time.sleep(1)
        #         break_state_check1 = self.driver.find_element(By.XPATH, self.break_state_check)
        #         assert break_state_check1.is_displayed()
        #         log.info("~Agent state change from ready to break : Success")
        # except:
        #         log.info("~Agent is not joined any process : Success")
        #         log.error("~Agent state change from ready to break : FAIL")
            # a = Alert(self.driver)
            # a.accept()
            # WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.XPATH, "//div[@class='terminal_extension_list']")))
            # time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, self.camp_click).click()
            time.sleep(3)
            # unjoin_camp = self.driver.find_element(By.XPATH, self.unjoin_check1)
            # time.sleep(3)
            # if unjoin_camp.is_displayed:
            #     time.sleep(2)
            #     self.driver.find_element(By.XPATH, self.unjoin).click()
            # time.sleep(6)
            # self.driver.find_element(By.XPATH, self.campaign_join).click()
            # time.sleep(2)
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
            log.info("~Agent State change to Ready after joining process : Success")
        except:
            log.error("~Agent State change to Ready after joining process : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)state_change_ready.png")
            self.driver.find_element(By.XPATH, self.logged_in_state).click()
            time.sleep(2)

    def call_activity(self, log):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(10)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            if value == "Established":
                log.info("~Agent Dail an OutBound call from process : Success")
            else:
                print("Call : Failed")
                # log.error("End ignore")
                self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)outboundcall_process.png")
                self.driver.find_element(By.XPATH, self.dispostion_one).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.mark_done).click()
        except:
            log.error("~Outbound Call from process : Fail")
            # log.error("End ignore")

    def hold_action(self, log):
        try:
            self.driver.find_element(By.XPATH, self.hold).click()
            time.sleep(2)

            hold_check = self.driver.find_element(By.XPATH, self.inactive_hangup_btn)
            assert hold_check.is_displayed()
            log.info("~Agent Hold/Un-hold on process : Success")
        except Exception as e:
            print('test failed', format(e))
            log.error("~Agent Hold/Un-hold on process : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)hold/unhold_process.png")

    def consult(self, log):
        try:
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.unhold).click()
            time.sleep(5)
            # element = WebDriverWait(self.driver, 180).until(
            #     EC.element_to_be_clickable((By.NAME, self.consult_click)))
            # self.driver.execute_script("arguments[0].click();", element)
            # btn = self.driver.find_element(By.XPATH, self.consult_click)
            # self.driver.execute_script("arguments[0].click();", btn)

            # self.driver.find_element(By.XPATH, self.consult_click).click()
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, self.dial_pad_tab).click()
            # time.sleep(2)
            self.driver.find_element(By.XPATH, self.input_number).send_keys(LoginData.test_mobile_one)
            time.sleep(3)
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.consult_call_btn).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.merge).click()
            time.sleep(2)
            text1 = self.driver.find_element(By.XPATH, self.consult_conf)
            assert text1.is_displayed()
            log.info("~Agent Consult-Conference in process : Success")
        except:
            log.error("~Agent Consult-Conference in process : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)consult_conference_process.png")
        try:
            self.driver.find_element(By.XPATH, self.consult_hang_up).click()
            time.sleep(1)
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            element1.click()
            # element = WebDriverWait(self.driver, 30).until(
            #     EC.presence_of_element_located((By.XPATH, self.dispostion_one)))
            # element.click()
            # self.driver.execute_script("arguments[0].click();", element)
            # self.driver.find_element(By.XPATH, self.dispostion_one).click()
            # time.sleep(1)
            # self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.mark_done).click()
            time.sleep(1)
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
            log.info("~Mark done in process : Success")
        except:
            log.error("~Mark done in process : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Mark done process.png")
        # Consult transfer
        try:
            # WebDriverWait(self.driver, 20).until(
            #     EC.invisibility_of_element_located((By.XPATH, self.mark_done))
            # )
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(10)
            # btn = self.driver.find_element(By.XPATH, self.consult_click)
            # self.driver.execute_script("arguments[0].click();", btn)
            # time.sleep(5)
            # WebDriverWait(self.driver, 180).until(
            #     EC.visibility_of_element_located((By.NAME, self.consult_click)))
            # self.driver.find_element(By.XPATH, self.consult_click).click()
            time.sleep(2)
            # btn = self.driver.find_element(By.XPATH, self.consult_click)
            # self.driver.execute_script("arguments[0].click();", btn)
            # time.sleep(5)
            # self.driver.find_element(By.XPATH, self.dial_pad_tab).click()
            # time.sleep(5)
            self.driver.find_element(By.XPATH, self.input_number).send_keys(LoginData.test_mobile_one)
            time.sleep(5)
            btn = self.driver.find_element(By.XPATH, self.consult_call_btn)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(5)
            # self.driver.find_element(By.XPATH, self.consult_call_btn).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.consult_transfer).click()
            time.sleep(2)
            disp_tab = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            # element = WebDriverWait(self.driver, 20).until(
            #     EC.presence_of_element_located((By.XPATH, self.dispostion_one)))
            # element.click()
            # disp_tab = WebDriverWait(self.driver, 180).until(
            #     EC.visibility_of_element_located((By.NAME, self.dispostion_tab)))
            # # disp_tab = self.driver.find_element(By.XPATH, self.dispostion_tab)
            assert disp_tab.is_displayed()
            log.info("~Agent Consult-Transfer in process : Success")
            self.markdone()
            # self.driver.find_element(By.XPATH, self.dispostion_one).click()
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, self.mark_done).click()
        except:
            log.error("~Agent Consult-Transfer in process: Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)consult-transfer in process.png")

    def transfer(self, log):

        # Transfer
        try:
            WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located((By.XPATH, self.mark_done))
            )
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.interaction_add).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_pad).send_keys(LoginData.test_mobile_two)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.dial_icon).click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.input_number).send_keys(LoginData.test_mobile_one)
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.transfer_icon).click()
            time.sleep(5)
            disp_tab = WebDriverWait(self.driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, self.disposition_click)))
            # disp_tab = self.driver.find_element(By.XPATH, self.dispostion_tab)
            assert disp_tab.is_displayed()
            log.info("~Agent Transfer (single-step) in process : Success")
            time.sleep(3)
            self.markdone()
            # self.driver.find_element(By.XPATH, self.dispostion_one).click()
            # time.sleep(1)
            # self.driver.find_element(By.XPATH, self.disp_ok_btn).click()
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, self.mark_done).click()
        except:
            log.error("~Agent Transfer (single-step) in process : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(crossx)singletransfer.png")

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

    def markdone(self):
        try:
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            element1.click()
            wait = WebDriverWait(self.driver, 20)
            btn = wait.until(
                EC.element_to_be_clickable((By.XPATH,self.mark_done)))
            btn.click()
            # time.sleep(1)
            toast = self.driver.find_element(By.XPATH, self.success_toast)
            assert toast.is_displayed()
        except Exception as e:
            print(f"Mark done process failed{e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}markdone.png")

    def process_calling(self):
        log = self.getLogger()
        # try:
        #     # self.driver = driver
        #     # login = Login(self.driver)
        #     # login.login_task(log)
        # # self.login_task(log)
        # except:
        #     print("login fail")
        # try:
        #     self.camp_join(log)
        # except:
        #     print("camp join fail")
        # try:
        #     self.call_activity(log)
        # except:
        #     print("camp join fail")
        # try:
        #     self.hold_action(log)
        # except:
        #     print("Hold fail")
        # try:
        #     self.consult(log)
        # except:
        #     print("cosult call fail")
        # try:
        #     self.transfer(log)
        # except:
        #    print("transfer fail")
        # try:
        #     self.logout(log)
        # except:
        #     print("Logout fail")
        # log.info("End ignore")
        # aes = AesLogin(self.driver)
        # return aes

