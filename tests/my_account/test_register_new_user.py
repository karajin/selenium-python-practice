import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.helpers.generic_helpers import generic_random_email_and_password
from src.pages.MyAccountSignedIn import MyAccountSignedIn
from selenium.webdriver.remote.webdriver import WebDriver
@pytest.mark.usefixtures('init_driver')
#getattr(pytest.fixtures, 'init_driver')
class TestRegisterNewUser:
  driver:WebDriver
  @pytest.mark.tcid13
  def test_register_valid_new_user(self):
    
    my_account_i = MyAccountSignedIn(self.driver)
    my_account_o = MyAccountSignedOut(self.driver)

    #go to my account
    my_account_o.go_to_my_account()

    #generate random email and password
    random_email = generic_random_email_and_password()

    #type email
    my_account_o.input_register_email(random_email['email'])

    #type password
    my_account_o.input_register_password(random_email['password'])

    #cick register
    my_account_o.click_register_button()

    #verify user is registered
    my_account_i.verify_user_is_signed_in()