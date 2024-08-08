import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.helpers.generic_helpers import generic_random_email_and_password
from src.pages.MyAccountSignedIn import MyAccountSignedIn
@pytest.mark.usefixtures('init_driver')
#getattr(pytest.fixtures, 'init_driver')
class TestRegisterNewUser:
  @pytest.mark.tcid13
  def test_register_valid_new_user(self):
    #go to my account
    #type email
    #type password
    #cick register
    #verify user is registered
    my_account_o = MyAccountSignedOut(self.driver)
    my_account_o.go_to_my_account()
    random_email = generic_random_email_and_password()
    my_account_o.input_register_email(random_email['email'])
    my_account_o.input_register_password(random_email['password'])
    my_account_o.click_register_button()

    my_account_i = MyAccountSignedIn(self.driver)
    my_account_i.verify_user_is_signed_in()