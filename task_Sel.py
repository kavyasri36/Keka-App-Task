from robocorp.tasks import task
from robocorp import browser
from RPA.PDF import PDF
from RPA.Browser.Selenium import Selenium
import time
from fpdf import FPDF
from bs4 import BeautifulSoup
import requests
 
 
@task
def task_1():
    browser.configure(slowmo=100,)
    browser=Selenium()
    open_keka_me()
    log_in()
    goto_me()
    leave_page()
    # timesheet_page()
    # attendance_page()
    # performance_page()
    # expenses_page()
    # apps_page()
 
 
def open_keka_me():
    browser=Selenium()
    browser.open_browser("https://esolutions.keka.com/#/home/welcome",browser="chrome")
    print("Browser opened")
    time.sleep(2)
    # browser.wait_until_element_is_visible("//img[@src='https://cdn.kekastatic.net/login/v/M176_2024.05.16.1/images/logos/microsoft.svg']",timeout=10)
    browser.click_button("//img[@src='https://cdn.kekastatic.net/login/v/M176_2024.05.16.1/images/logos/microsoft.svg']")
    print("Selected Login Option as Microsoft")
    time.sleep(2)
   
 
def log_in():
    browser=Selenium()
    browser.input_text("//input[@id='i0116']","")
    print("email entered")
    time.sleep(2)
    # time.sleep(20)
    browser.click_button("//input[@id='idSIButton9']")
    print("click on Next")
    time.sleep(2)
    browser.input_password("//*[@id='i0118']","")
    print("password entered")
    browser.click_button("//input[@id='idSIButton9']")
    print("click on submit")
    time.sleep(5)
    browser.click_button("//*[@id='KmsiCheckboxField']")
    print("Check box")
    browser.click_button("//input[@id='idSIButton9']")
    print("Click yes to stay signed in")
    time.sleep(3)
 
 
def goto_me():
    browser=Selenium()
    browser.click_button("//*[@id='accordion']/li[2]/a/span[1]")
    time.sleep(2)
 
 
def leave_page():
    browser=Selenium()
    # browser.open_browser("https://esolutions.keka.com/#/me/leave/summary",browser="chrome")
    open_keka_me()
    log_in()
    goto_me()
    browser.print_to_pdf("output/leave.pdf")
    browser.click_button_when_visible("//a[@routerlink='timesheet']")
    time.sleep(2)
