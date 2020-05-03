# -*- coding:gbk -*-

import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from private_info import *
import mail


def is_element_present(browser, xpath):
    from selenium.common.exceptions import NoSuchElementException

    try:
        element = browser.find_element_by_xpath(xpath)
    except NoSuchElementException as e:
        # print(e)
        return False
    else:
        return True


def sign_in(uid, pwd):
    # set to no-window
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")

    # simulate a browser to open the website
    browser = webdriver.Chrome(options=chrome_options)
    # browser = webdriver.Chrome()
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

    try:
        # input uid and password
        print("Inputting the UID and Password of User {0}".format(uid))
        browser.find_element_by_xpath("//*[@id='mt_5']/div[1]/div[3]/input").send_keys(uid)
        browser.find_element_by_xpath("//*[@id='mt_5']/div[2]/div[3]/input").send_keys(pwd)

        # click to sign in
        browser.find_element_by_xpath("//*[@id='mt_5']/div[4]/div/input").click()
        time.sleep(2)

        # get middle info
        real_mid_page_url = browser.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
        browser.get(real_mid_page_url)

        print("Checking whether User {0} has signed in".format(uid))
        msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[7]/span").text
        # if msg == "今日您已经填报过了":
        #     return msg

        # click to fill in
        span_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]/span").text
        if span_text == "本人填报":
            browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]").click()
        else:
            browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[6]").click()

        time.sleep(2)

        # click to submit
        print("Signing in for User {0}".format(uid))
        browser.find_element_by_xpath("//*[@id='bak_0']/div[19]/div[4]").click()
        time.sleep(2)

        if is_element_present(browser, "//*[@id='bak_0']/div[2]/div[2]/div[2]/div[2]"):
            msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[2]/div[2]/div[2]/div[2]").text
        elif is_element_present(browser, "//*[@id='bak_0']/div[2]"):
            msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[2]").text

    except Exception as e:
        msg = "while signing in for user " + uid + " there is an exception: \n" + str(e)
        mail.mail(msg, MAIL_ADMAIN)
    finally:
        browser.quit()

    # quit the browser
    print("Singing in for User {0} is finished".format(uid))
    return msg


def timing(hour, minute, the_users):
    now = datetime.datetime.now()
    if now.hour == hour and now.minute == minute:
        print("\n\n\n")
        print(now)
        for user in the_users:
            msg = sign_in(user.uid, user.pwd)
            msg = user.uid + ": " + msg
            print("Emailing to User {0} for notification".format(user.uid))
            mail.mail(msg, user.email)
            print("Emailing is finished")


if __name__ == "__main__":
    # For Single User
    # msg = sign_in(UID, PWD)
    # mail.mail(msg, EMAIL_TO)

    # For Multiple Users
    # for user in users:
    #     msg = sign_in(user.uid, user.pwd)
    #     print("Emailing to User {0} for notification".format(user.uid))
    #     mail.mail(msg, user.email)
    #     print("Emailing is finished")

    # For Timing and Multiple Users
    while True:

        # sign for tow
        timing(6, 0, users)
        # sign for the others
        timing(8, 30, stus)

        # sleep 30 secs
        time.sleep(30)
