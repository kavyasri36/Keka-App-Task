from robocorp import browser
from RPA.PDF import PDF
from RPA.Browser.Selenium import Selenium
import time
from fpdf import FPDF
from bs4 import BeautifulSoup

def web_to_pdf():
    page=Selenium()
    page.open_browser("https://www.google.com/", browser="chrome")
    page.print_to_pdf("output/example.pdf")
    
web_to_pdf()