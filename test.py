from RPA.Browser.Selenium import Selenium
from robocorp.tasks import task
import time


browser=Selenium()
input= "Kavya.Sri@esolutionsfirst.com"
passwd="KSR@0329"

@task
def open_keka_me():
    browser.open_available_browser(url="https://esolutions.keka.com/#/home/welcome",browser_selection="chrome", maximized=True)
    print("Browser opened")
    browser.wait_until_page_contains_element('//p[@class="ps-2" and text()="Microsoft"]',timeout='30s')
    browser.click_element('//p[@class="ps-2" and text()="Microsoft"]')
    time.sleep(2)
    browser.wait_until_page_contains_element("//input[contains(@placeholder, 'Email or phone')]",timeout='30s')
    browser.input_text("//input[contains(@placeholder, 'Email or phone')]",text=input)
    browser.click_element("//input[@id='idSIButton9' and @type='submit' and @value='Next']")
    time.sleep(2)
    browser.wait_until_page_contains_element("//input[@id='i0118' and @name='passwd' and @type='password']",timeout='30s')
    browser.input_text("//input[@id='i0118' and @name='passwd' and @type='password']",text=passwd)
    browser.click_element("//input[@id='idSIButton9' and @type='submit' and @value='Sign in']")
    time.sleep(2)
    browser.wait_until_page_contains_element('//input[@id="KmsiCheckboxField"]',timeout='30s')
    browser.click_element('//input[@id="KmsiCheckboxField"]')
    browser.wait_until_page_contains_element("//input[@id='idSIButton9' and @type='submit' and @value='Yes']",timeout='30s')
    browser.click_element("//input[@id='idSIButton9' and @type='submit' and @value='Yes']")
    time.sleep(2)
    leave_page()

def leave_page():
    browser.wait_until_page_contains_element("//a[@class='nav-link' and @href='/#/me/leave']/span[@class='ki-user sidebar-list-icon' and following-sibling::span[@class='sidebar-list-label' and text()='Me']]",timeout='30s')
    browser.click_element("//a[@class='nav-link' and @href='/#/me/leave']/span[@class='ki-user sidebar-list-icon' and following-sibling::span[@class='sidebar-list-label' and text()='Me']]")
    time.sleep(3)
    browser.print_to_pdf("output/leave.pdf")
    time.sleep(3)
    timesheet_page()

def timesheet_page():
    browser.wait_until_page_contains_element("//a[@routerlink='timesheet' and @href='#/me/timesheet']",timeout='30s')
    browser.click_element("//a[@routerlink='timesheet' and @href='#/me/timesheet']")
    time.sleep(2)
    browser.print_to_pdf("output/timesheet.pdf")
    time.sleep(2)
    attendance_page()

def attendance_page():
    browser.wait_until_page_contains_element("//a[@routerlink='attendance' and @href='#/me/attendance']",timeout='30s')
    browser.click_element("//a[@routerlink='attendance' and @href='#/me/attendance']")
    time.sleep(2)
    browser.print_to_pdf("output/attendance.pdf")
    text=browser.get_text("//div[@class='page-container']")
    with open ("attendance.txt","w",encoding="utf-8") as f:
        f.write(text)
    with open("attendance.txt","r",encoding="utf-8") as f:
        print(f.read())
    time.sleep(2)
    performance_page()

def performance_page():
    browser.wait_until_page_contains_element("//a[text()='Performance' and @href='#/me/performance/objectives/summary']",timeout='30s')
    browser.click_element("//a[text()='Performance' and @href='#/me/performance/objectives/summary']")
    time.sleep(2)
    browser.print_to_pdf("output/performance.pdf")
    time.sleep(2)
    expenses_page()

def expenses_page():
    browser.wait_until_page_contains_element("//a[@routerlink='expenses' and @href='#/me/expenses']",timeout='30s')
    browser.click_element("//a[@routerlink='expenses' and @href='#/me/expenses']")
    time.sleep(2)
    browser.print_to_pdf("output/expenses.pdf")
    time.sleep(2)
    apps_page()

def apps_page():
    browser.wait_until_page_contains_element("//a[@routerlink='apps' and @href='#/me/apps']",timeout='30s')
    browser.click_element("//a[@routerlink='apps' and @href='#/me/apps']")
    time.sleep(2)
    browser.print_to_pdf("output/apps.pdf")
    time.sleep(2)