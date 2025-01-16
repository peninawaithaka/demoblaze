from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@step('the user navigates to the login page')
def step_navigate_to_login_page(context):
    context.driver.get('https://www.demoblaze.com/')

    #print(context.driver.title)

    assert "STORE" in context.driver.title, "Title is not visible"

@step('the user enters valid credentials')
def step_user_enters_valid_credentials(context):
    login_link = context.driver.find_element(By.ID, 'login2')
    assert login_link.is_displayed(), "Login Link is not visible"
    
    #mouse movements
    actions = ActionChains(context.driver)

    actions.move_to_element(login_link).perform()
    login_link.click()
  
    wait = WebDriverWait(context.driver, 30)
    login_form = wait.until(EC.visibility_of_element_located((By.ID, 'logInModalLabel')))
    #context.driver.find_element(By.ID, 'logInModalLabel')
    assert login_form.is_displayed(), "Login Form is not displayed"
    print("assertions")


    #filling the form
    user_name = context.driver.find_element(By.ID, 'loginusername')
    assert user_name.is_displayed(), "Username is not visible"
    user_name.clear()
    user_name.send_keys(context.username)


    password = context.driver.find_element(By.ID, 'loginpassword')
    assert password.is_displayed(), "Password is not displayed"
    password.clear()
    password.send_keys(context.password)

    #asserting that the close and login buttons are visible
    # buttons = context.driver.find_elements(By.TAG_NAME, 'button')
    # buttons[0].click()

    close = context.driver.find_element(By.XPATH, "//button[normalize-space(@class)='btn btn-primary']")
    print(close.is_displayed())

    assert close.is_displayed(), "Close Button is not visible"

    login = context.driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
    assert login.is_displayed(), "Login Button is not visible"

    

@step('the user is directed to their logged in home page')
def step_user_directed_to_home_page(context):
    pass

