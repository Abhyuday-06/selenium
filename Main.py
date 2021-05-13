from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

driver_path = r"C:/Users/ASUS/Downloads/chromedriver.exe"
brave_path = r"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.binary_location = brave_path
opt.add_experimental_option("prefs", {

	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(driver_path, port = 0,options=opt)
code = input("Enter the query which you want to search on Google:")
time.sleep(5)
driver.get(f"https://meet.google.com/{code}")


"""
option = webdriver.ChromeOptions()
option.binary_location = brave_path
browser = webdriver.Chrome(executable_path=driver_path, options=option)
code = input("Enter the query which you want to search on Google:")
time.sleep(5)
browser.get(f"https://meet.google.com/{code}")
"""