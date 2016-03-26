from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from threading import Thread
import Queue
import sys
q = Queue.Queue()

def get_tickets():
    
    driver = webdriver.Chrome('/Users/AnthonyKim/Documents/workspace/tdwytb/chromedriver')
    driver.get("https://www.eventbrite.com/e/bacchanal-2016-tickets-22507236751")

    register = driver.find_element(By.XPATH, '//*[@id="event-page"]/main/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div/div/div/form/span/span[2]/a').click()

    checkout = driver.find_element(By.XPATH, '//*[@id="event-page"]/div[7]/div[2]/div/div/section[3]/div/div/div[3]/input').click()


if __name__ == "__main__":

         
    for i in range(5):
        thread = Thread(target=get_tickets, args = '')
        thread.start()
        q.put(thread)
    try:
        while 1:
            x = 1
    except KeyboardInterrupt:
        sys.exit()
        

