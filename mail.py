import smtplib

from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate, formataddr
from utils.mail_utils import sender, smpt_server, smpt_port, smpt_user, smpt_password, subject

def reorganize_mailing_list(mailing_list):
    """reorganize mailing list by student id as key"""
    new_mailing_list = dict()
    for item in mailing_list:
        id = item["Student No."]
        name = item["Name"]
        email = item["Email"]
        new_mailing_list[id] = {"name": name, "email": email}
    return new_mailing_list

def send_mail(receiver_name, receiver_email, body):
    """send mail to a single receiver"""
    receiver = f"{receiver_name} <{receiver_email}>"
    msg = MIMEText(body, "html", "utf-8")
    msg["From"] = Header(formataddr((sender, sender)), "utf-8")
    msg["To"] = formataddr((receiver_name, receiver_email))
    msg["Subject"] = Header(subject.format(receiver_name), "utf-8")
    msg["Date"] = formatdate(localtime=True)

    try:
        smtp = smtplib.SMTP_SSL(smpt_server, smpt_port)
        smtp.login(smpt_user, smpt_password)
        smtp.sendmail(sender, receiver, msg.as_string())
        print(f"Mail sent successfully to {receiver_name}")
    except smtplib.SMTPException as e:
        print(f"Error: Unable to send mail to {receiver_name}", e)
    finally:
        smtp.quit()


