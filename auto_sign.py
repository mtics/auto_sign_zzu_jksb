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
    # browser = webdriver.Chrome()
    browser.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

    # input uid and password
    print("正在输入用户{0}的用户名和密码".format(uid))
    browser.find_element_by_xpath("//*[@id='mt_5']/div[1]/div[3]/input").send_keys(uid)
    browser.find_element_by_xpath("//*[@id='mt_5']/div[2]/div[3]/input").send_keys(pwd)

    # click to sign in
    browser.find_element_by_xpath("//*[@id='mt_5']/div[4]/div/input").click()
    time.sleep(2)

    # get middle info
    real_mid_page_url = browser.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
    browser.get(real_mid_page_url)

    print("正在检查用户{0}的签到状态".format(uid))
    msg = browser.find_element_by_xpath("//*[@id='bak_0']/div[7]/span").text
    if msg == "今日您已经填报过了":
        return msg

    # click to fill in
    span_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]/span").text
    if span_text == "本人填报":
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[4]").click()
    else:
        browser.find_element_by_xpath("//*[@id='bak_0']/div[13]/div[3]/div[6]").click()

    time.sleep(2)

    # click to submit
    print("正在为用户{0}进行签到".format(uid))
    browser.find_element_by_xpath("//*[@id='bak_0']/div[19]/div[4]").click()
    time.sleep(2)

    final_text = browser.find_element_by_xpath("//*[@id='bak_0']/div[2]/div[2]/div[2]/div[2]").text

    # quit the browser
    print("用户{0}的签到已结束".format(uid))
    browser.quit()
    return final_text


if __name__ == "__main__":

    # For Single User
    msg = sign_in(UID, PWD)
    mail.mail(msg, EMAIL_TO)

    # For Multiple Users
    for user in users:
        msg = sign_in(user.uid, user.pwd)
        print("即将发送邮件通知用户{0}".format(user.uid))
        mail.mail(msg, user.email)
        print("邮件发送已结束")
