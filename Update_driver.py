from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()

with open("driver_path.txt","w") as f:
    f.write(driver_path)

print(f"Driver installed at: {driver_path}")