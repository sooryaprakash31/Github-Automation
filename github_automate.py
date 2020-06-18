from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys
import os

foldername = str(sys.argv[1])
username = str(sys.argv[2])
password = str(sys.argv[3])

class github:
     def __init__(self):
          self.options = Options()
          #Selenium fails if your default profile has many bookmarks and extensions
          #Create a new profile and get the paths using chrome://version/
          self.options.add_argument("user-data-dir=/path/to/your/chrome/profile")
          self.driver = webdriver.Chrome(options=self.options,executable_path = "path/to/your/executable/chromedriver")
          self.driver.get("https://github.com/login/")
          sleep(1)
          self.driver.find_elements_by_xpath('//*[@id="login_field"]')[0].send_keys(username)
          self.driver.find_elements_by_xpath('//*[@id="password"]')[0].send_keys(password)
          sleep(1)
          self.driver.find_elements_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]')[0].click()
          self.driver.find_elements_by_xpath('/html/body/div[1]/header/div[6]/details/summary')[0].click()
          sleep(1)
          self.driver.find_elements_by_xpath('/html/body/div[1]/header/div[6]/details/details-menu/a[1]')[0].click()
          sleep(1)
          self.driver.find_elements_by_xpath('//*[@id="repository_name"]')[0].send_keys(foldername)
          self.driver.find_elements_by_xpath('//*[@id="new_repository"]/div[3]/button')[0].click()
          sleep(5)
          self.driver.quit()

github()