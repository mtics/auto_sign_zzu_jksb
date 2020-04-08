import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from private_info import *
import mail


def sign_in(uid, pwd):

    # set to no-window
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # simulate a browser to open the website
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

    # input uid and password
    browser.find_element_by_xpath("//*[@id='mt_5']/div[1]/div[3]/input").send_keys(uid)
    browser.find_element_by_xpath("//*[@id='mt_5']/div[2]/div[3]/input").send_keys(pwd)

    # click to sign in
    browser.find_element_by_xpath("//*[@id='mt_5']/div[4]/div/input").click()
    time.sleep(2)

    # get middle info
    real_mid_page_url = browser.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
    browser.get(real_mid_page_url)

    msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[7]/span").text
    if msg == "今日您已经填报过了":
        return msg

    # click to fill in
    browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[6]").click()
    time.sleep(2)

    # click to submit
    browser.find_element_by_xpath("//*[@id='bak_0']/div[19]/div[4]").click()
    time.sleep(2)

    final_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[2]/div[2]/div[2]/div[2]").text

    # quit the browser
    browser.quit()
    return final_text


if __name__ == "__main__":

    # For Single User
    # msg = sign_in(UID, PWD)
    # mail.mail(msg, EMAIL_TO)

    # For Multiple Users
    for user in users:
        msg = sign_in(user.uid, user.pwd)
        mail.mail(msg, user.email)
