import pytest

from pages.aeslogin import AesLogin
from pages.agentcalling import Agent_calling
from pages.atomoscheck import Atomos
from pages.login import Login
from pages.processcalling import Process_Calling


@pytest.mark.usefixtures("setup")
class TestOne:
    # def test_atomos(self):
    #     ac = Atomos(self.driver)
    #     ac.main_atomos()

    def test_one(self):
        self.driver.delete_all_cookies()
        # print("test one started")
        # lp = Login(self.driver)
        # lp.login_op()
        # pc = Process_Calling(self.driver)
        # pc.process_calling()
        # self.driver.close()
        ac = Agent_calling(self.driver)
        ac.agent_activity()

    # def test_two(self):
    #     aes = AesLogin(self.driver)
    #     aes.aes_login_op()
