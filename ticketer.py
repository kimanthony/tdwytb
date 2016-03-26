from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('/Users/AnthonyKim/Documents/workspace/tdwytb/chromedriver')
driver.get("https://www.eventbrite.com/e/ticketing-practice-tickets-24204562498")

register = driver.find_element(By.XPATH, '//*[@id="event-page"]/main/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div/div/div/form/span/span[2]/a').click()


checkout = driver.find_element(By.XPATH, '//*[@id="event-page"]/div[7]/div[2]/div/div/section[3]/div/div/div[3]/input').click()

