import pytest
from src.pages.HomePage import HomePage
from src.pages.Header import Header
from src.pages.CartPage import CartPage
import logging as logger
from src.helpers.generic_helpers import generate_random_coupon
from selenium import webdriver
import time
@pytest.mark.usefixtures('init_driver')
class TestInvalidCoupon:
  driver: webdriver
  @pytest.mark.tcid14
  def test_invalid_coupon(self):
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

    #click add coupon button
    cart_P.click_add_coupon()

    #generate a random coupon code
    random_coupon = generate_random_coupon()

    #enter coupon code in the box
    cart_P.enter_coupon(random_coupon)

    #click apply
    cart_P.click_apply_a_coupon()
    expected_error_msg = f'Coupon "{random_coupon}" does not exist!'
    
    #verify error message  
    cart_P.wait_until_err_message_is_displayed(expected_error_msg)
    