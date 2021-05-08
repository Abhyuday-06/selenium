from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:/Users/ASUS/Downloads/chromedriver.exe")
search = input("Enter the query which you want to search on Google:")
time.sleep(3)
driver.get(f"https://www.google.co.in/search?q={search}")