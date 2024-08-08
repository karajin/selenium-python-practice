import pytest
from src.pages.HomePage import HomePage
from src.pages.Header import Header
from src.pages.CartPage import CartPage
from src.helpers.generic_helpers import generate_random_coupon
from selenium.webdriver.remote.webdriver import WebDriver

@pytest.mark.usefixtures('init_driver')
class TestInvalidCouponValidation():
  driver: WebDriver
  @pytest.mark.tcid23
  def test_invaild_coupon_validation(self):
    home_P = HomePage(self.driver)
    header_P = Header(self.driver)
    cart_P = CartPage(self.driver)
   
    #go to home page
    home_P.go_to_home_page()

    home_P.max_win()

    #add 1 item to cart
    home_P.click_first_add_to_cart()

    #verify an item has been added to the cart
    header_P.wait_until_cart_item_count(1)

    #go to cart
    header_P.click_on_cart_header()
    products = cart_P.get_all_product_names_in_cart()
    assert len(products)==1, f"Expected 1 item in cart but #found {len(products)}"

    #generate a random coupon
    random_coupon = generate_random_coupon()

    #apply the coupon
    cart_P.click_add_coupon()
    cart_P.enter_coupon(random_coupon)
    cart_P.click_apply_a_coupon()
    
    #Verify error message
    expected_mesg = f'Coupon "{random_coupon}" does not exist!'
    cart_P.wait_until_err_message_is_displayed(expected_mesg)
   
    
   