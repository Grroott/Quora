from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from selenium.common.exceptions import *
from threading import *



class S(Thread):
    def run(self):
        count=0
        count1=0
        xxx=0
        driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
        for i in range(0,1):
            try:
                driver.get("file:///C:/Users/hp%20world/Videos/test.html")
                driver.maximize_window()
                x=driver.find_element_by_xpath('/html/body/button')
                x.click()
#                 '''
#                 x.send_keys("Which is the best option to invest if I have 2 thousand rupees per month?")
#                 time.sleep(3)
#                 x.send_keys(Keys.ENTER)
#                 y=driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
#                 y.click()
#             except NoSuchElementException:
#                 print("Element not found")
#                 count1 = count1 + 1
#
#             except NoSuchWindowException:
#                 driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#                 print("skipped")
#                 pass
#             except WebDriverException:
#                 driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#                 print("skipped")
#                 pass
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(0, 2500)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(2500, 3500)")
#             time.sleep(4)
#             driver.execute_script("window.scrollTo(3500, 4000)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(4500, 5000)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(5000, 5500)")
#             count = count + 1
#             ids = driver.find_elements_by_xpath('//*[@id]')
#             for ii in ids:
#                 u = str(ii.get_attribute('id'))
#                 if u.endswith('11_paged_list'):
#                     #print(u)
#                     x = ii.get_attribute('id')
#                     xx = '//*[@id="' + u + '"]'
#                     try:
#                         poi = driver.find_element_by_xpath(xx)
#                         poi.click()
#                         xxx = xxx + 1
#                         driver.switch_to.window(driver.window_handles[0])
#                         # driver.switch_to_window(driver.window_handles[0])
#                         #print('case 1')
#
#                     except WebDriverException:
#                         driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#                 if u.endswith('12_paged_list'):
#                     #print(u)
#                     x = ii.get_attribute('id')
#                     xx = '//*[@id="' + u + '"]'
#                     try:
#                         poi = driver.find_element_by_xpath(xx)
#                         poi.click()
#                         xxx = xxx + 1
#                         driver.switch_to.window(driver.window_handles[0])
#                         # driver.switch_to_window(driver.window_handles[0])
#                         #print('case 2')
#
#                     except WebDriverException:
#                         driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#                 if u.endswith('37_paged_list'):
#                     #print(u)
#                     #x = ii.get_attribute('id')
#                     xx = '//*[@id="' + u + '"]'
#                     try:
#                         poi = driver.find_element_by_xpath(xx)
#                         poi.click()
#                         xxx = xxx + 1
#                         driver.switch_to.window(driver.window_handles[0])
#                         # driver.switch_to_window(driver.window_handles[0])
#                         #print('case 3')
#
#                     except WebDriverException:
#                         driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#             print(str(count) + '-first')
#             if count1 > 3:
#                 print("Check internet connection")
#                 exit()
#             print (xxx)
#             time.sleep(3)
# Class SS(Thread):
#     def run(self):
#         count = 0
#         count1=0
#         xxx=0
#         driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#         for i in range(0, 50):
#             try:
#
#                 driver.get("https://duckduckgo.com/")
#                 driver.maximize_window()
#                 x = driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
#                 x.send_keys("Which is the best option to invest if I have 2 thousand rupees per month?")
#                 x.send_keys(Keys.ENTER)
#                 y = driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
#                 y.click()
#             except NoSuchElementException:
#                 print("Element not found")
#                 count1 = count1 + 1
#
#             except NoSuchWindowException:
#                 driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#                 print("skipped")
#                 pass
#             except WebDriverException:
#                 driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#                 print("skipped")
#                 pass
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(0, 2500)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(2500, 3500)")
#             time.sleep(4)
#             driver.execute_script("window.scrollTo(3500, 4000)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(4500, 5000)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(5000, 5500)")
#             count = count + 1
#             ids = driver.find_elements_by_xpath('//*[@id]')
#             for ii in ids:
#                 u = str(ii.get_attribute('id'))
#                 if u.endswith('12_paged_list') or u.endswith('11_paged_list'):
#                     #print(u)
#                     x = ii.get_attribute('id')
#                     xx = '//*[@id="' + u + '"]'
#                     try:
#                         poi = driver.find_element_by_xpath(xx)
#                         poi.click()
#                         xxx = xxx + 1
#                         driver.switch_to.window(driver.window_handles[0])
#                         # driver.switch_to_window(driver.window_handles[0])
#                         #print('case 1')
#
#                     except WebDriverException:
#                         driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#             count = count + 1
#             print(str(count) + '-second')
#             if count1 > 3:
#                 print("Check internet connection")
#                 exit()
#             print (xxx)
#             time.sleep(3)
#
# class SSS(Thread):
#     def run(self):
#         count = 0
#         count1=0
#         xxx=0
#         driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#         for i in range(0, 50):
#
#             try:
#
#                 driver.get("https://duckduckgo.com/")
#                 driver.maximize_window()
#                 x = driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
#                 x.send_keys("Which is the best option to invest if I have 2 thousand rupees per month?")
#                 x.send_keys(Keys.ENTER)
#                 y = driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
#                 y.click()
#             except NoSuchElementException:
#                 print("Element not found")
#                 count1 = count1 + 1
#
#             except NoSuchWindowException:
#                 driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#                 print("skipped")
#                 pass
#             except WebDriverException:
#                 driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#                 print("skipped")
#                 pass
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(0, 2500)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(2500, 3500)")
#             time.sleep(4)
#             driver.execute_script("window.scrollTo(3500, 4000)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(4500, 5000)")
#             time.sleep(2)
#             driver.execute_script("window.scrollTo(5000, 5500)")
#             count = count + 1
#             ids = driver.find_elements_by_xpath('//*[@id]')
#             for ii in ids:
#                 u = str(ii.get_attribute('id'))
#                 if u.endswith('12_paged_list') or u.endswith('11_paged_list'):
#                     #print(u)
#                     x = ii.get_attribute('id')
#                     xx = '//*[@id="' + u + '"]'
#                     try:
#                         poi = driver.find_element_by_xpath(xx)
#                         poi.click()
#                         xxx = xxx + 1
#                         driver.switch_to.window(driver.window_handles[0])
#                         # driver.switch_to_window(driver.window_handles[0])
#                         #print('case 1')
#
#                     except WebDriverException:
#                         driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
#             count = count + 1
#             print(str(count) + '-third')
#             if count1 > 3:
#                 print("Check internet connection")
#                 exit()
#             print (xxx)
#             time.sleep(1)
t1=S()

t1.start()
#t2.start()
#t3.start()


