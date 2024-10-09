from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step Definitions
@given('I am on the Demo Login Page')
def step_given_login_page(context):
    context.driver = webdriver.Chrome("D:\automation_test\chromedriver-win64\chromedriver.exe")
    context.driver.get("https://www.saucedemo.com/")
    time.sleep(2)  # wait for the page to load

@when('I fill the account information for account StandardUser')
def step_when_fill_standard_user(context):
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')

@when('I fill the account information for account LockedOutUser')
def step_when_fill_locked_out_user(context):
    context.driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')

@when('I click the Login Button')
def step_when_click_login(context):
    context.driver.find_element(By.ID, 'login-button').click()

@then('I am redirected to the Demo Main Page')
def step_then_redirected_to_main(context):
    time.sleep(2)  # wait for the page to load
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"

@then('I verify the App Logo exists')
def step_then_verify_logo(context):
    assert context.driver.find_element(By.CLASS_NAME, 'app_logo').is_displayed()

@then('I verify the Error Message contains the text "{text}"')
def step_then_verify_error_message(context, text):
    time.sleep(2)  # wait for the error message to appear
    error_message = context.driver.find_element(By.CSS_SELECTOR, '.error-message-container').text
    assert text in error_message

@given('I am logged in')
def step_given_logged_in(context):
    context.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    context.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    context.driver.find_element(By.ID, 'login-button').click()

@when('I am on the inventory page')
def step_when_on_inventory(context):
    time.sleep(2)  # wait for the inventory page to load

@then('I extract content from the web page')
def step_then_extract_content(context):
    items = context.driver.find_elements(By.CLASS_NAME, 'inventory_item')
    with open("extracted_data.txt", "w") as file:
        for item in items:
            file.write(item.text + "\n")

@then('I log out')
def step_then_log_out(context):
    context.driver.find_element(By.ID, 'react-burger-menu-btn').click()
    context.driver.find_element(By.ID, 'logout_sidebar_link').click()

@then('I verify I am on the Login page again')
def step_then_verify_login_page(context):
    time.sleep(2)  # wait for the page to load
    assert context.driver.current_url == "https://www.saucedemo.com/"

@given('I close the browser')
def step_given_close_browser(context):
    context.driver.quit()
