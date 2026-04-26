from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.chrome(service=Service(ChromeDriverManager.install()))
service = Service(executable_path="")
driver = webdriver.Chrome(service=service)

webdriver.chromium

# Entering the correct class page

# Check if there is a new div with  