from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@step('the user navigates to the login page')
def step_navigate_to_login_page(context):
    context.driver.get('https://www.demoblaze.com/')
    context.driver.implicitly_wait(30)

    #print(context.driver.title)

    assert "STORE" in context.driver.title

@step('the user enters valid credentials')
def step_user_enters_valid_credentials(context):
    login_link = context.driver.find_element(By.ID, 'login2')
    
    actions = ActionChains(context.driver)

    actions.move_to_element(login_link).click()
    context.driver.implicitly_wait(60)

    print("Are we getting to this point")

@step('the user is directed to their logged in home page')
def step_user_directed_to_home_page(context):
    pass

