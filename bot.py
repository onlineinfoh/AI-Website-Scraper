from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Web clicking helper libraries
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def scrape(website):
    print("Scraping website...")

    with open("driver_path.txt", "r") as file:
        saved_path_to_driver = file.read().strip()

    service = Service(executable_path=saved_path_to_driver)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        print("Page successfully loaded...")
        html = driver.page_source
        return html
    finally: 
        driver.quit()

def extract(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split(dom_content, max_length=7000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]