from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from threading import Thread
from datetime import datetime
import Queue, sys, os

q = Queue.Queue()
ticket_time = datetime(2016, 3, 28, 2, 0, 0, 0)

def get_tickets():

    driver = webdriver.Chrome(os.path.dirname(os.path.realpath(__file__)) + '/chromedriver')
    while 1:
        now = datetime.now()
        if now >= ticket_time:
            break
    ''' opens a new chrome application and clicks on the register then checkout button'''
    # MANDATORY: include direct path to chromedriver here
    # opens bacchanal eventbrite ticketing page
    driver.get("https://www.eventbrite.com/e/bach-testers-tickets-24226391790")
    # click register button
    register = driver.find_element(By.XPATH, '//*[@id="event-page"]/main/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div/div/div/form/span/span[2]/a').click()
    # click checkout buton
    checkout = driver.find_element(By.XPATH, '//*[@id="event-page"]/div[7]/div[2]/div/div/section[3]/div/div/div[3]/input').click()


if __name__ == "__main__":
    # attempt to get 5 tickets
    for i in range(4):
        # new thread for each ticket grabber
        thread = Thread(target=get_tickets, args = '')
        thread.start()
        q.put(thread) # add the thread to the queue
        print(ticket_time)
    try:
        while 1:
            x = 1
    except KeyboardInterrupt:
        sys.exit()
        

