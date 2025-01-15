from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    # chrome_options = Options() #--headless - runs tests in a headless mode

    # service = Service("D:\python\selenium\chrome.exe")
    #context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(20)

def after_all(context):
    context.driver.quit()