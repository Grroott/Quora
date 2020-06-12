# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# # from selenium.common.exceptions import *
#
# driver = webdriver.Chrome(executable_path="E:\chromedriver.exe")
# for i in range(0,1):
#     driver.get("file:///C:/Users/hp%20world/Videos/test.html")
#     driver.maximize_window()
#     x=driver.find_element_by_xpath('/html/body/button')
#     x.click()
#     driver.find_element_by_xpath('//*[@id="id01"]/form/div[2]/input[1]').send_keys("Gokul")



from twitter import *
# from tkinter import *

def showTweets(x, num):
    # display a number of new tweets and usernames
    for i in range(0, num):
        line1 = (x[i]['user']['screen_name'])
        line2 = (x[i]['text'])
        w = Label(master, text=line1 + "\n" + line2 + "\n\n")
        w.pack()

def getTweets():

    x = t.statuses.home_timeline(screen_name="putscreennamehere")
    return x


def tweet():

    global entryWidget

    if entryWidget.get().strip() == "":
        print("Empty")
    else:
        t.statuses.update(status=entryWidget.get().strip())
        entryWidget.delete(0,END)
        print("working")


# Put in token, token_key, con_secret, con_secret_key
t = Twitter(
    auth=OAuth('wfFUI3nxyXO7R4XiUzV64h2Cc', 'RwdIadETIcSAYEPTjzwqqb2iSYaw5v1l560V1Wn3TGV4GsjuvY',
               '882616317542449152-bivoI10UC6mCpKDVyRIy23XlyYk5CLM', 'TBklmsWxkWrDiyoPj7xWUtUUn4SHjmwqNYWIbmNjvOsVY'))

numberOfTweets = 10



# master = Tk()
showTweets(getTweets(), numberOfTweets)

# master.title("Tkinter Entry Widget")
# master["padx"] = 40
# master["pady"] = 20
# Create a text frame to hold the text Label and the Entry widget
# textFrame = Frame(master)
# #Create a Label in textFrame
# entryLabel = Label(textFrame)
# entryLabel["text"] = "Make a new Tweet:"
# entryLabel.pack(side=LEFT)
# # Create an Entry Widget in textFrame
# entryWidget = Entry(textFrame)
# entryWidget["width"] = 50
# entryWidget.pack(side=LEFT)
# textFrame.pack()
# button = Button(master, text="Submit", command=tweet)
# button.pack()
#
# master.mainloop()