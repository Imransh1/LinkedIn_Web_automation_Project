from user_pwd import user,password
from selenium import webdriver
import warnings
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox

# Ignoring any unnecessary warnings
warnings.filterwarnings('ignore')

# Initialize web driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Asus\Documents\Imran Learning\Study_material\Web_Automation\chromedriver.exe")

# Open web url
driver.get('https://www.linkedin.com/mynetwork/invitation-manager/sent/')
driver.maximize_window()
sleep(2)

action = ActionChains(driver)

# go to sign-in page
signin = driver.find_element('xpath', "//a[@class = 'main__sign-in-link']")
signin.click()
sleep(2)

# enter username
username = driver.find_element('xpath', "//input[@id = 'username']")
username.click()

#window_after = driver.window_handles[1]
#driver.switch_to.window(window_after)

username.send_keys(user)
sleep(1)

# enter password
pwd = driver.find_element('xpath', "//input[@id = 'password']")
pwd.click()
sleep(1)

pwd.send_keys(password)
pwd.send_keys(Keys.RETURN)

def withdraw_requests():
    withdraw_request = driver.find_element('xpath', "//button[@class= 'artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--tertiary ember-view invitation-card__action-btn']")
    withdraw_request.click()
    sleep(2)

    confirm_withdrawal= driver.find_element('xpath', "//button[@class= 'artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view']")
    confirm_withdrawal.click()
    sleep(5)

x = 0
try:
    # recursion of withdraw_requests function() untill sent requests is 0
    while x != 1:
        withdraw_requests()
except:
    messagebox.showinfo("Successful", "End of requests")