from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium
import json
import time
import os
from pathlib import Path
browser = Selenium()
 
cookie_file = "cookies.json"
def save_cookies():
    cookies = browser.get_cookies(as_dict=True)
    for cookie_name in cookies:
        print(cookie_name)
    with open(cookie_file, "w") as file:
        json.dump(cookies, file)
def load_cookies():
    try:
        with open(cookie_file, "r") as file:
            cookies = json.load(file)
            for key,value in cookies.items():
                # Add cookies directly without modifying attributes
                print(key)
                print(value)
                browser.add_cookie(name=key, value=value, secure=True, expiry=None)
    except FileNotFoundError:
        print("No cookies file found. Proceeding without cookies.")