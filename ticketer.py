from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from threading import Thread
import Queue, sys

q = Queue.Queue()

def get_tickets():
    ''' opens a new chrome application and clicks on the register then checkout button'''
    # MANDATORY: include direct path to chromedriver here
    driver = webdriver.Chrome('/Users/AnthonyKim/Documents/workspace/tdwytb/chromedriver')
    # opens bacchanal eventbrite ticketing page
    driver.get("https://www.eventbrite.com/e/practice-tickets-24208427057")
    # click register button
    register = driver.find_element(By.XPATH, '//*[@id="event-page"]/main/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div/div/div/form/span/span[2]/a').click()
    # click checkout buton
    checkout = driver.find_element(By.XPATH, '//*[@id="event-page"]/div[7]/div[2]/div/div/section[3]/div/div/div[3]/input').click()


if __name__ == "__main__":
    # attempt to get 5 tickets
    for i in range(5):
        # new thread for each ticket grabber
        thread = Thread(target=get_tickets, args = '')
        thread.start()
        q.put(thread) # add the thread to the queue
    try:
        while 1:
            x = 1
    except KeyboardInterrupt:
        sys.exit()
        

