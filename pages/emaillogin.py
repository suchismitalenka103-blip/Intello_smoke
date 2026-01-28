import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from datetime import timedelta

from pytest_check import check
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utils.utils import BaseClass
from testdata.logindata import LoginData
import time


class EmailLogin(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    # Locators for login
    page_heading = "//span[@class='lht_primary']"
    login_username = "//input[@name='loginid']"
    login_password = "//input[@id='password']"
    login_click = "loginForm.Login"
    email_register = "//div[@class='modal-content']//div[@class='terminal_register_boxin_header']"
    extension_no = "//input[@placeholder='Terminal']"
    extension_name = "//input[@placeholder='Username']"
    extension_pass = "//input[@placeholder='Password']"
    extension_click = "//button[text()='Next']"
    email_terminal_check = f"//div[@class='terminal_extension_list']//a[normalize-space()='{LoginData.email_extn}']"
    skip_btn = "//button[normalize-space()='Skip']"
    login_state = "//span[@class='LogIn profiler_btn_img']"
    camp_click = "//div[@class='interaction_indicators']"
    queue_join = f"(//div[contains(@class,'acs_content_grid_row')][.//div[@id='name' and normalize-space()='{LoginData.process_name}']]//app-switch//span[@class='slider'])[2]"
    process_join = f"//div[contains(@class,'acs_content_grid_row')][.//div[@id='name' and normalize-space()='{LoginData.process_name}']]//div[contains(@id,'Cheked')]//span[@class='slider']"
    unjoin_check = "//app-switch[@class='switch']//span[@class='slider']"
    unjoin = "//app-switch[@class='switch partial']"
    campaign_join = "//div[@id='Cheked0']//span[@class='slider']"
    logged_in_state = "//span[@class='LogIn profiler_btn_img']//img[@alt='Profile']"
    dialog = "//ngb-modal-window[@role='dialog']"
    # unjoin = "//app-switch[@class='switch partial']"
    # campaign_join = "//app-switch[@class='d-flex justify-content-end']//span[@class='slider']"
    toast = "//div[@class='ng-tns-c49-0 toast-message ng-star-inserted']"
    success_toast = "//div[contains(@class, 'toast-success')]"
    ready_state = "//span[normalize-space()='Ready']"
    ready_state_check = "//span[@class='profiler_btn_img Ready']"

    # Locators for interaction
    accept_btn = "(//button[normalize-space()='Accept'])[1]"
    call_status_hover = "//div[@class='connected ng-star-inserted']"
    status_value = "(//div[@class='tooltip-inner'])[1]"
    interaction_active = "//button[@class='tm_opts_btn int_btn active int_mail']//span[@class='int_btn_sts']"
    hang_up = "//button[@type='button' and  @ngbtooltip='HangUp']"

    # Locators for Forward and reply
    email_header = '''(//div[@class="shortmail_matter text-truncate pointer" and text()='This is an email with attachment sent from Python'])'''
    forward_icon = "(//span[@class='imoon icon-forward'])[2]"
    input_email_address = "//input[@placeholder='Recipients' and @type='text']"
    send_icon = "//span[@class='imoon icon-send']"
    reply_icon = "(//span[@class='imoon icon-reply'])[3]"
    reply_all_icon = "(//span[@class='imoon icon-reply-all'])[4]"
    text_area = "//div[@data-placeholder='Enter your text here']"

    # Locators for disposition
    disposition_click = "//span[normalize-space(text())='Answered']/parent::button"
    dispostion_one = "(//button[@class='isml_tab_btn ng-star-inserted'])[1]"
    child_dispostion = "//span[normalize-space()='Success_child_four']"
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

    # For time manipulation
    current_time = datetime.now()
    past_time = current_time - timedelta(hours=1)
    time_stamp = current_time.strftime("%Y-%m-%d_%H_%M")
    print(past_time.strftime("%Y/%m/%d %H:%M:%S"))

    def email_login(self, log):
        try:
            self.driver.get(LoginData.product_url)
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_all_elements_located((By.XPATH, self.page_heading))
            )
            text1 = self.driver.find_element(By.XPATH, self.page_heading).text
            print(text1)
            assert text1 == 'Login'
            # log.info("~Intello LogIn page Opened : Success")
            print("~Intello LogIn page Opened : Success")
        except:
            log.error("~Intello LogIn page Opened : Fail")

        try:
            WebDriverWait(self.driver, 50).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            WebDriverWait(self.driver, 50).until(
                EC.visibility_of_element_located((By.XPATH, self.login_username))
            )
            self.driver.find_element(By.XPATH, self.login_username).send_keys(LoginData.email_login_data)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.login_password).send_keys(LoginData.email_login_data)
            time.sleep(2)
            self.driver.find_element(By.ID, self.login_click).click()
            time.sleep(2)
            emailreg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.email_register))
            )
            assert emailreg.is_displayed()
            log.info("~Agent (Email) LogIn : Success")
        except:
            log.error("~Agent (Email) LogIn : Fail")

        try:
            time.sleep(4)
            self.driver.find_element(By.XPATH, self.extension_no).send_keys(LoginData.email_extn)
            self.driver.find_element(By.XPATH, self.extension_name).send_keys(LoginData.email_extn)
            self.driver.find_element(By.XPATH, self.extension_pass).send_keys(LoginData.email_extn)
            self.driver.find_element(By.XPATH, self.extension_click).click()
            time.sleep(3)
            # toast = WebDriverWait(self.driver, 30).until(
            #     EC.presence_of_element_located((By.XPATH, self.toast))).text
            # print(toast)
            # assert toast == "Email terminal registered"
            terminal = self.driver.find_element(By.XPATH, self.email_terminal_check)
            time.sleep(4)
            assert terminal.is_displayed()
            agent_state = self.driver.find_element(By.XPATH, self.login_state)
            assert agent_state.get_attribute("class") == "LogIn profiler_btn_img"
            log.info("~Agent(Email channel) register : Success")
        except:
            log.error("~Agent(Email channel) register : Fail")
            # log.error("End email ignore : FAIL")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent(Email channel) register.png")
            self.driver.find_element(By.XPATH, self.skip_btn).click()

    def process_join_m(self, log):
        try:
            time.sleep(3)
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.camp_click))
            )
            btn = self.driver.find_element(By.XPATH, self.camp_click)
            # time.sleep(2)
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.queue_join).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.process_join).click()
            time.sleep(2)
            success = self.driver.find_element(By.XPATH, self.success_toast)
            assert success.is_displayed()
            # success = self.driver.find_element(By.XPATH, self.success_toast)
            # assert success.is_displayed()
            log.info("~Agent Email Process Join : Success")

        except:
            log.error("~Agent Email Process Join : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}email_camp_join un_join.png")

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
            log.error("~Agent State change to Ready : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}email agent State change to Ready.png")
            self.driver.find_element(By.XPATH, self.logged_in_state).click()
            time.sleep(2)

    def mail_sender(self, log):
        # try:
        subject = "An email with attachment from Python"
        body = "This is an email with attachment sent from Python"
        sender_email = "testing_radius@visnet.in"
        receiver_email = ["suchilenkavis@gmail.com"]
        # receiver_email = ["testing_radius@visnet.in"]
        cc_email = ["lenkasuchismita01@gmail.com"]
        # password = "R@d$tag1ng@123"
        password = "yggvxsssbhjfcxwq"

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ",".join(receiver_email)
        message["Subject"] = subject
        message["Cc"] = ",".join(cc_email)
        # message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))
        text = message.as_string()
        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            server.sendmail(sender_email, cc_email, text)
        # except:
        #     log.error("~Agent Email interaction : FAIL")
        #     log.error("End email ignore")

    def accept_op(self, log):
        try:
            accept = WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.XPATH, self.accept_btn)))
            time.sleep(4)
            assert accept.is_displayed()
            log.info("~Email land : Success")
        except NoSuchElementException:
            log.error("~Email land : FAIL")
            # log.error("End email ignore")
        except Exception as e:
            print(f"Email land : {e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Email land.png")
        except TimeoutException:
            log.error("~Email land : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Email land.png")
        try:
            time.sleep(4)
            accept = WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.XPATH, self.accept_btn)))
            # time.sleep(4)
            accept.click()
            time.sleep(2)
            call_status = self.driver.find_element(By.XPATH, self.call_status_hover)
            action = ActionChains(self.driver)
            action.move_to_element(call_status).perform()
            time.sleep(2)
            value = self.driver.find_element(By.XPATH, self.status_value).text
            print(value)
            assert value == "Established"
            # active = self.driver.find_element(By.XPATH, self.interaction_active)
            # assert active.is_displayed()
            log.info("~Agent accepts email : Success")
        except Exception as e:
            print(f"Email accept email : {e}")
            log.error("~Agent accepts email : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent accepts email.png")

        # Forward mail
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.email_header).click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.forward_icon).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.input_email_address).send_keys("lenkasuchismita01@gmail.com")
            time.sleep(2)
            action = ActionChains(self.driver)
            action.send_keys(Keys.ENTER).perform()
            self.driver.find_element(By.XPATH, self.send_icon).click()
            time.sleep(1)
            # success = self.driver.find_element(By.XPATH, self.success_toast)
            # assert success.is_displayed()
            toast = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, self.success_toast)))
            assert toast.is_displayed()
            log.info("~Email forward : Success")
        # except:
        #     log.error("~Email forward : Fail")
        #     self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Email forward.png")
        except Exception as e:
            print(f"Email forward : {e}")
            log.error("~Email forward : Fail")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Email forward.png")

        # Reply
        try:
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.email_header).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.reply_icon).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.text_area).send_keys("I am writing this mail for testing")
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.send_icon).click()
            time.sleep(1)
            # success = self.driver.find_element(By.XPATH, self.success_toast)
            # assert success.is_displayed()
            toast = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.success_toast)))
            assert toast.is_displayed()
            log.info("~Email reply send : Success")
        except Exception as e:
            log.error("~Email reply send : Fail")
            print(f"Email reply send : {e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Email reply send.png")
        # Reply all
        try:
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.email_header).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.reply_all_icon).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.text_area).send_keys("I am writing this mail to reply all")
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.send_icon).click()
            time.sleep(1)
            # success = self.driver.find_element(By.XPATH, self.success_toast)
            # assert success.is_displayed()
            toast = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.success_toast)))
            assert toast.is_displayed()
            log.info("~Email reply all send : Success")
        except Exception as e:
            log.error("~Email reply all send : Fail")
            print(f"Email rply all send{e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Email reply all send.png")

        # Hang up
        try:
            time.sleep(5)
            self.driver.find_element(By.XPATH, self.hang_up).click()
            time.sleep(2)
            element1 = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.disposition_click)))
            assert element1.is_displayed()
            log.info("~Agent hang up email : Success")
        except Exception as e:
            log.error("~Agent hang up email : Fail")
            print(f"Agent hang up email{e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}Agent hang up email.png")

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
        except Exception as e:
            log.error("~Agent Disposition and Mark-Done : Fail")
            print(f"agent disposition and mark done {e}")
            log.error("End email ignore")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}email agent Disposition and Mark-Done.png")

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
            log.info("~Email agent Logout : Success")
        except Exception as e:
            log.error("~Email agent Logout : Fail")
            print(f"logout fail{e}")
            self.driver.save_screenshot(f"..\\screenshot\\{self.time_stamp}(Email)logout.png")

    def email_login_op(self):
        log = self.getLogger()
        try:
            self.email_login(log)
        except:
            print("email Login failed")
        try:
            self.process_join_m(log)
        except:
            print("process joined failed")
        try:
            self.mail_sender(log)
        except:
            print("email sender fail")
        try:
            self.accept_op(log)
        except :
            print("Accept fail")

