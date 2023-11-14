from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class DataForm:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def fill_forms(self, url, address, price, link):
        for index in range(len(address)):
            self.driver.get(url)
            sleep(3)
            data_entry = self.driver.find_elements(By.CSS_SELECTOR, "form input[type='text']")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, ".lRwqcd div[role='button']")
            data_entry[0].send_keys(address[index])
            data_entry[1].send_keys(price[index])
            data_entry[2].send_keys(link[index])
            submit_button.click()
            sleep(3)
        self.driver.quit()
