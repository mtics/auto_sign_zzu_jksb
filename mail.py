# -*- coding:gbk -*-

import smtplib
from email.mime.text import MIMEText
from private_info import *


def mail(mail_text, mail_to):
    # set the mail context
    msg = MIMEText(mail_text)

    # set the mail info
    msg['Subject'] = "每日健康打卡通知"
    msg['From'] = MAIL_USER
    msg['To'] = mail_to

    # send the mail
    send = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
    send.login(MAIL_USER, MAIL_PWD)
    send.send_message(msg)
    # quit QQ EMail
    send.quit()
