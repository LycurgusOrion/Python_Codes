import pyautogui as pg
import smtplib
import config
import datetime
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

pg.PAUSE = 0.2

def take_ss():
    filename = capture_ss()
    return filename


def capture_ss():
    # pg.hotkey("win", "down")
    ss = "Screenshot-" + str(datetime.datetime.now()) + ".png"
    ss = ss.replace(' ', '_')
    ss = ss.replace(':', '_', 2)
    im = pg.screenshot(ss)
    time.sleep(0.2)
    return ss


def attach_and_mail(from_addr, to_addr, password, subject, body, filename):

    msg = MIMEMultipart()

    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    if filename != "None":
        attachment = open(filename, "rb")
        p = MIMEBase("application", "octet-stream")
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',
                     "attachment; filename= %s" % filename)
        msg.attach(p)

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(from_addr, password)
        text = msg.as_string()
        s.sendmail(from_addr, to_addr, text)
        return 0
    except Exception as e:
        return e


def Main():
    time.sleep(2)
    while True:
        body = "Screenshot Captured, PFA."
        filename = capture_ss()
        attach_and_mail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS,
                        config.PASSWORD, filename, body, filename)
        time.sleep(90)


if __name__ == "__main__":
    Main()
