from selenium import webdriver
from dotenv import load_dotenv
import os

def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(30) # Waits for 10 seconds before throwing NoSuchElementException - globally defined

    load_dotenv()
    context.username = os.getenv("TEST_USERNAME")
    context.password = os.getenv("TEST_PASSWORD")
    
def after_all(context):
    context.driver.quit()