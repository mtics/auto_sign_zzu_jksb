import time
from selenium import webdriver
import constant
import mail


def sign_in(uid, pwd):
    # simulate a browser to open the website
    browser = webdriver.Chrome()
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")
    # maximize the browser's window
    browser.maximize_window()

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
    return final_text


if __name__ == "__main__":
    msg = sign_in(constant.UID, constant.PWD)
    mail.mail(msg)
