from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")

service = Service('D:\Database\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://en.wikipedia.org/wiki/Wiki')
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")