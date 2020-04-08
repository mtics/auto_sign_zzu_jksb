import smtplib
from email.mime.text import MIMEText
import constant


def mail(mail_text):
    # set the mail context
    msg = MIMEText(mail_text)

    # set the mail info
    msg['Subject'] = "每日健康打卡通知"
    msg['From'] = constant.MAIL_USER
    msg['To'] = constant.MAIL_TO

    # send the mail
    send = smtplib.SMTP_SSL("smtp.qq.com", 465)
    send.login(constant.MAIL_USER, constant.MAIL_PWD)
    send.send_message(msg)
    # quit QQ EMail
    send.quit()



