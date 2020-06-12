from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import *
from threading import *



class S(Thread):
    def run(self):
        count=0
        count1=0

        xp=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0,150):
            lst=[]
            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x=driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("Which is the best option to invest if I have 2 thousand rupees per month?")
                x.send_keys(Keys.ENTER)
                y=driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
            except NoSuchElementException:
                print("Element not found")
                count1 = count1 + 1

            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 2500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(2500, 3500)")
            time.sleep(4)
            ids = driver.find_elements_by_xpath('//*[@id]')
            addd = 0
            for ii in ids:
                u = str(ii.get_attribute('id'))
                if u.endswith('32'):
                    print(ii.get_attribute('id'))
                    x = ii.get_attribute('id')
                    xx = '//*[@id="' + u + '"]'
                    try:
                       # print(str(lst[xp]))
                        poi = driver.find_element_by_xpath(xx)
                        poi.click()
                        addd=addd+1
                        print('case 2')
                    except InvalidSelectorException:
                        pass
                    except ElementNotVisibleException:
                        pass
                    except WebDriverException:
                        pass
                if addd > 0:
                    break
            #
            #     driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
            # for ii in ids:
            #     u = str(ii.get_attribute('id'))
            #     if '_ad' in u:
            #         print(ii.get_attribute('id'))
            #         x = ii.get_attribute('id')
            #         xp = '//*[@id="' + u + '"]'
            #         poi = driver.find_element_by_xpath(xp)
            #         poi.click()
            #         print('sucess 3')
                # if u.endswith('paged_list'):
                #     print(ii.get_attribute('id'))
                #     x = ii.get_attribute('id')
                #     print('case 1')

            count = count + 1

            print(str(count) + '-first')
            #time.sleep(10000)
            xp = 0
            if count1 > 2:
                print("Check internet connection")
                # exit()
            time.sleep(1)
            # driver.close()
class SS(Thread):
    def run(self):
        count = 0
        count1=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0, 150):
            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x = driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("Which is the best option to invest if I have 2 thousand rupees per month?")
                x.send_keys(Keys.ENTER)
                y = driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
            except NoSuchElementException:
                print("Element not found")
                count1 = count1 + 1

            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 2500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(2500, 3500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(3500, 4000)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(4500, 5000)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(5000, 5500)")
            count = count + 1
            print(str(count) + '-second')
            if count1 > 3:
                print("Check internet connection")
                exit()
            time.sleep(1)

class SSS(Thread):
    def run(self):
        count = 0
        count1=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0, 150):

            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x = driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("Which is the best option to invest if I have 2 thousand rupees per month?")
                x.send_keys(Keys.ENTER)
                y = driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
            except NoSuchElementException:
                print("Element not found")
                count1 = count1 + 1

            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 2500)")
            time.sleep(4)
            driver.execute_script("window.scrollTo(2500, 3500)")
            time.sleep(4)
            driver.execute_script("window.scrollTo(3500, 4000)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(4500, 5000)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(5000, 5500)")
            count = count + 1
            print(str(count) + '-third')
            if count1 > 3:
                print("Check internet connection")
                exit()
            time.sleep(1)
t1=S()
t2=SS()
t3=SSS()

t1.start()
#t2.start()
#t3.start()


