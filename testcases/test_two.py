import pytest

from pages.chatlogin import ChatLogin
from pages.emaillogin import EmailLogin


@pytest.mark.usefixtures("setup")
class TestTwo:
    def test_one(self):
        print("test one started")
        obc = ChatLogin(self.driver)
        obc.chat_log_op()

    # def test_two(self):
    #     print("test two started")
    #     obe = EmailLogin(self.driver)
    #     obe.email_login_op()
