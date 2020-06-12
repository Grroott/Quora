from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import *
from threading import *



class S(Thread):
    def run(self):
        count=0
        count1=0
        xxx=0

        l=0
        xp=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0,50):
            lst = []
            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x=driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("What happens if I eat Parotta daily?")
                x.send_keys(Keys.ENTER)
                y=driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
                count1 = 0
            except NoSuchElementException:
                print("Element not found")
                Keys.F5
                count1 = count1 + 1
                time.sleep(15)
                lst=['just','summa']

            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(500, 1000)")
            time.sleep(2)
            #driver.execute_script("window.scrollTo(1000, 1500)")
            #time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")


            ids = driver.find_elements_by_xpath('//*[@id]')
            for ii in ids:
                u=str(ii.get_attribute('id'))
                if u.endswith('9_paged_list'):
                    print (u)
                    x = ii.get_attribute('id')
                    xx = '//*[@id="' + u + '"]'
                    try:
                        poi = driver.find_element_by_xpath(xx)
                        poi.click()
                        xxx=xxx+1
                        print('case 1')
                        break
                    except WebDriverException:
                        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
            #     if u.endswith('18'):
            #         print(ii.get_attribute('id'))
            #         x=ii.get_attribute('id')
            #         xx='//*[@id="'+u+'"]'
            #         lst.append(xx)
            #         l=len(lst)
            # xp=int(l)-2
            # print (xp)
            # try:
            #     print (str(lst[xp]))
            #     poi = driver.find_element_by_xpath(str(lst[xp]))
            #     poi.click()
            #     print ('case 2')
            # except InvalidSelectorException:
            #     print ("No ad found")
            # except WebDriverException:
            #     driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
            for ii in ids:
                u=str(ii.get_attribute('id'))
                if '_ad' in u:
                    print(ii.get_attribute('id'))
                    x = ii.get_attribute('id')
                    xp = '//*[@id="' + u + '"]'
                    poi = driver.find_element_by_xpath(xp)
                    poi.click()
                    xxx=xxx+1
                    print ('sucess 3')
                # if u.endswith('paged_list'):
                #     print(ii.get_attribute('id'))
                #     x = ii.get_attribute('id')
                #     print('case 1')

            count = count + 1

            print(str(count) + '-first')

            xp=0
            if count1 > 2:
                print("Check internet connection")
                #exit()
            time.sleep(1)
            print(xxx)
            #driver.close()

class SS(Thread):
    def run(self):
        count=0
        count1=0
        xxx=0

        l=0
        xp=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0,50):
            lst = []
            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x=driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("What happens if I eat Parotta daily?")
                x.send_keys(Keys.ENTER)
                y=driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
                count1 = 0
            except NoSuchElementException:
                print("Element not found")
                Keys.F5
                count1 = count1 + 1
                time.sleep(15)
                lst=['just','summa']

            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(500, 1000)")
            time.sleep(2)
            #driver.execute_script("window.scrollTo(1000, 1500)")
            #time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")


            ids = driver.find_elements_by_xpath('//*[@id]')
            for ii in ids:
                u=str(ii.get_attribute('id'))
                if u.endswith('9_paged_list'):
                    print (u)
                    x = ii.get_attribute('id')
                    xx = '//*[@id="' + u + '"]'
                    try:
                        poi = driver.find_element_by_xpath(xx)
                        poi.click()
                        xxx=xxx+1
                        print('case 1')
                        break
                    except WebDriverException:
                        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
            #     if u.endswith('18'):
            #         print(ii.get_attribute('id'))
            #         x=ii.get_attribute('id')
            #         xx='//*[@id="'+u+'"]'
            #         lst.append(xx)
            #         l=len(lst)
            # xp=int(l)-2
            # print (xp)
            # try:
            #     print (str(lst[xp]))
            #     poi = driver.find_element_by_xpath(str(lst[xp]))
            #     poi.click()
            #     print ('case 2')
            # except InvalidSelectorException:
            #     print ("No ad found")
            # except WebDriverException:
            #     driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
            for ii in ids:
                u=str(ii.get_attribute('id'))
                if '_ad' in u:
                    print(ii.get_attribute('id'))
                    x = ii.get_attribute('id')
                    xp = '//*[@id="' + u + '"]'
                    poi = driver.find_element_by_xpath(xp)
                    poi.click()
                    xxx=xxx+1
                    print ('sucess 3')
                # if u.endswith('paged_list'):
                #     print(ii.get_attribute('id'))
                #     x = ii.get_attribute('id')
                #     print('case 1')

            count = count + 1

            print(str(count) + '-second')

            xp=0
            if count1 > 2:
                print("Check internet connection")
                #exit()
            time.sleep(1)
            print(xxx)
            #driver.close()

class SSS(Thread):
    def run(self):
        count=0
        count1=0
        xxx=0

        l=0
        xp=0
        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
        for i in range(0,50):
            lst = []
            try:

                driver.get("https://duckduckgo.com/")
                driver.maximize_window()
                x=driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
                x.send_keys("What happens if I eat Parotta daily?")
                x.send_keys(Keys.ENTER)
                y=driver.find_element_by_xpath('//*[@id="r1-0"]/div/h2/a[1]')
                y.click()
                count1 = 0
            except NoSuchElementException:
                print("Element not found")
                Keys.F5
                count1 = count1 + 1
                time.sleep(15)
                lst=['just','summa']

            except NoSuchWindowException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            except WebDriverException:
                driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
                print("skipped")
                pass
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(2)
            driver.execute_script("window.scrollTo(500, 1000)")
            time.sleep(2)
            #driver.execute_script("window.scrollTo(1000, 1500)")
            #time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")
            # time.sleep(2)
            # driver.execute_script("window.scrollTo(2000, 2500)")


            ids = driver.find_elements_by_xpath('//*[@id]')
            for ii in ids:
                u=str(ii.get_attribute('id'))
                if u.endswith('9_paged_list'):
                    print (u)
                    x = ii.get_attribute('id')
                    xx = '//*[@id="' + u + '"]'
                    try:
                        poi = driver.find_element_by_xpath(xx)
                        poi.click()
                        xxx=xxx+1
                        print('case 1')
                        break
                    except WebDriverException:
                        driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
            #     if u.endswith('18'):
            #         print(ii.get_attribute('id'))
            #         x=ii.get_attribute('id')
            #         xx='//*[@id="'+u+'"]'
            #         lst.append(xx)
            #         l=len(lst)
            # xp=int(l)-2
            # print (xp)
            # try:
            #     print (str(lst[xp]))
            #     poi = driver.find_element_by_xpath(str(lst[xp]))
            #     poi.click()
            #     print ('case 2')
            # except InvalidSelectorException:
            #     print ("No ad found")
            # except WebDriverException:
            #     driver = webdriver.Chrome(executable_path="C:\Web driver\chromedriver_win32\chromedriver.exe")
            for ii in ids:
                u=str(ii.get_attribute('id'))
                if '_ad' in u:
                    print(ii.get_attribute('id'))
                    x = ii.get_attribute('id')
                    xp = '//*[@id="' + u + '"]'
                    poi = driver.find_element_by_xpath(xp)
                    poi.click()
                    xxx=xxx+1
                    print ('sucess 3')
                # if u.endswith('paged_list'):
                #     print(ii.get_attribute('id'))
                #     x = ii.get_attribute('id')
                #     print('case 1')

            count = count + 1

            print(str(count) + '-second')

            xp=0
            if count1 > 2:
                print("Check internet connection")
                #exit()
            time.sleep(1)
            print(xxx)
            #driver.close()
t1=S()
t2=SS()
t3=SSS()

t1.start()
t2.start()
t3.start()



