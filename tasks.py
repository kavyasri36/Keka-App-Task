from RPA.Browser.Selenium import Selenium
from RPA.Windows import Windows
from robocorp.tasks import task
import time
from cookies import * 
from pathlib import Path

browser=Selenium()
input= "Kavya.Sri@esolutionsfirst.com"
passwd="KSR@0329"
comment="Robocorp Libraries Documentation"

@task
def open_keka_me():
    browser.open_available_browser(url="https://esolutions.keka.com/#/home/welcome",browser_selection="chrome", maximized=True)
    #browser.open_user_browser(url="https://esolutions.keka.com/#/home/welcome")
    # browser.open_available_browser(
                                    # url="https://esolutions.keka.com/#/home/welcome",
                                    # use_profile=True,
                                    # profile_name="context",
                                    # profile_path=Path(os.getcwd(), "context"),
                                    # browser_selection="chrome",
                                    # maximized=True,
                                    # download='AUTO',
                                    # # alias="OfficeAlly",
                                    # )
    print("Browser opened \n")
    
    # load_cookies()
    # browser.reload_page()
    
    
    microsoft=browser.does_page_contain_element('//p[@class="ps-2" and text()="Microsoft"]')
    if microsoft:
        browser.click_element('//p[@class="ps-2" and text()="Microsoft"]')
        print("Login through microsoft \n")
        time.sleep(2)
    username_field=browser.does_page_contain_element("//input[contains(@placeholder, 'Email or phone')]")
    if username_field:
        browser.input_text("//input[contains(@placeholder, 'Email or phone')]",text=input)
        browser.click_element("//input[@id='idSIButton9' and @type='submit' and @value='Next']")
        print("input email and Click next \n")
    time.sleep(2)
    password_field=browser.does_page_contain_element("//input[@id='i0118' and @name='passwd' and @type='password']")
    if password_field:
        browser.input_text("//input[@id='i0118' and @name='passwd' and @type='password']",text=passwd)
        browser.click_element("//input[@id='idSIButton9' and @type='submit' and @value='Sign in']")
        print("input password and click sign in \n")
        time.sleep(2)
    
    checkbox_field=browser.does_page_contain_element('//input[@id="KmsiCheckboxField"]')
    if checkbox_field:
        browser.click_element('//input[@id="KmsiCheckboxField"]')
        print("tick on dont show again \n")
        browser.wait_until_page_contains_element("//input[@id='idSIButton9' and @type='submit' and @value='Yes']",timeout='30s')
        browser.click_element("//input[@id='idSIButton9' and @type='submit' and @value='Yes']")
        print("click in yes \n")
        time.sleep(5)
    # save_cookies()
    #leave_page()

# def leave_page():
#     browser.wait_until_page_contains_element("//a[@class='nav-link' and @href='/#/me/leave']/span[@class='ki-user sidebar-list-icon' and following-sibling::span[@class='sidebar-list-label' and text()='Me']]",timeout='30s')
#     browser.click_element("//a[@class='nav-link' and @href='/#/me/leave']/span[@class='ki-user sidebar-list-icon' and following-sibling::span[@class='sidebar-list-label' and text()='Me']]")
#     print("open leave page \n")
#     time.sleep(3)
#     browser.print_to_pdf("output/leave.pdf")
#     text=browser.get_text("//me-leave//div[@class='page-container']")
#     with open ("leave.txt","w",encoding="utf-8") as f:
#         f.write(text)
#     print("leave page text copied \n\n")
#     with open("leave.txt","r",encoding="utf-8") as f:
#         print(f.read())
#     time.sleep(3)
#     timesheet_page()

# def timesheet_page():
#     browser.wait_until_page_contains_element("//a[@routerlink='timesheet' and @href='#/me/timesheet']",timeout='30s')
#     browser.click_element("//a[@routerlink='timesheet' and @href='#/me/timesheet']")
#     time.sleep(2)
#     print("open timesheet page \n")
#     # browser.wait_until_page_contains_element("//*[@id='preload']//tr[2]/td[4]",timeout='20s')
#     # browser.input_text("//*[@id='preload']//tr[2]/td[4]",text="8")
#     # print("enter hours in timesheet \n")
#     # time.sleep(2)
#     # browser.wait_until_page_contains_element("//*[@id='preload']//div/textarea",timeout='20s')
#     # browser.input_text("//*[@id='preload']//div/textarea",text=comment)
#     # print("enter the comment \n")
#     # time.sleep(2)
#     browser.print_to_pdf("output/timesheet.pdf")
#     text=browser.get_text("//employee-timesheet//div[@class='page-container']")
#     with open ("leave.txt","a",encoding="utf-8") as f:
#         f.write(text)
#     print("timesheet page content copied \n\n")
#     with open("leave.txt","r",encoding="utf-8") as f:
#         print(f.read())
#     time.sleep(2)
#     attendance_page()

# def attendance_page():
#     browser.wait_until_page_contains_element("//a[@routerlink='attendance' and @href='#/me/attendance']",timeout='30s')
#     browser.click_element("//a[@routerlink='attendance' and @href='#/me/attendance']")
#     print("open attendance page \n")
#     time.sleep(2)
#     browser.print_to_pdf("output/attendance.pdf")
#     text=browser.get_text("//employee-attendance//div[@class='page-container']")
#     with open ("leave.txt","a",encoding="utf-8") as f:
#         f.write(text)
#     print("attendance content copied \n\n")
#     with open("leave.txt","r",encoding="utf-8") as f:
#         print(f.read())
#     time.sleep(2)
#     performance_page()

# def performance_page():
#     browser.wait_until_page_contains_element("//a[text()='Performance' and @href='#/me/performance/objectives/summary']",timeout='30s')
#     browser.click_element("//a[text()='Performance' and @href='#/me/performance/objectives/summary']")
#     print("open performance page \n")
#     time.sleep(2)
#     browser.print_to_pdf("output/performance.pdf")
#     text=browser.get_text("//employee-me-performance//div[@class='page-container']")
#     with open ("leave.txt","a",encoding="utf-8") as f:
#         f.write(text)
#     print("performance content copied \n\n")
#     with open("leave.txt","r",encoding="utf-8") as f:
#         print(f.read())
#     time.sleep(2)
#     expenses_page()

# def expenses_page():
#     browser.wait_until_page_contains_element("//a[@routerlink='expenses' and @href='#/me/expenses']",timeout='30s')
#     browser.click_element("//a[@routerlink='expenses' and @href='#/me/expenses']")
#     print("expense page opened \n")
#     time.sleep(2)
#     browser.print_to_pdf("output/expenses.pdf")
#     text=browser.get_text("//employee-expenses[@class='ng-star-inserted']")
#     with open ("leave.txt","a",encoding="utf-8") as f:
#         f.write(text)
#     print("expense content copied \n\n")
#     with open("leave.txt","r",encoding="utf-8") as f:
#         print(f.read())
#     time.sleep(2)
#     apps_page()

# def apps_page():
#     browser.wait_until_page_contains_element("//a[@routerlink='apps' and @href='#/me/apps']",timeout='30s')
#     browser.click_element("//a[@routerlink='apps' and @href='#/me/apps']")
#     print("open apps page \n")
#     time.sleep(2)
#     browser.print_to_pdf("output/apps.pdf")
#     text=browser.get_text("//me-app-integration[@class='ng-star-inserted']")
#     with open ("leave.txt","a",encoding="utf-8") as f:
#         f.write(text)
#     print("apps content copied \n\n")
#     with open("leave.txt","r",encoding="utf-8") as f:
#         print(f.read())
#     time.sleep(2)
    




















    
