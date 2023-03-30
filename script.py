import requests
import time
import send_email
from bs4 import BeautifulSoup
import CONSTANTS
import datetime

CONST = {}

CONST = CONSTANTS.ENV_CONST[CONSTANTS.RUN_ENV]

## ** Script get page **  ##
def request_website(URL):
    
    headers = {'user-agent': 'my-app/0.0.1',
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "referer": "https://spotsescalada.wordpress.com/"
            }
    page = requests.get(URL, headers=headers)

    return page.text


## ** Script scrape page (from txt file) **  ##
def scraper(website_html):
    soup = BeautifulSoup(website_html, "html.parser")

    div_destaques = soup.find("div", {CONST["FILTER"]["ATTRIBUTE"]: CONST["FILTER"]["VALUE"]})

    return div_destaques

website_page = ""
website_html = request_website(CONST["URL"])
website_cache = scraper(website_html)

send_email.gmail_send_message(notify_emails=CONST["MAILING"]["RECIPIENT"]["START"], email_subject=CONST["MAILING"]["SUBJECT"]["START"], email_content=CONST["MAILING"]["CONTENT"]["START"])

try:
    while True:
        website_page = ""
        website_html = request_website(CONST["URL"])
        website_now = scraper(website_html)

        if website_cache != website_now:
            print("Changed!!! Notify!!! - " + str(datetime.datetime.now()))
            send_email.gmail_send_message(notify_emails=CONST["MAILING"]["RECIPIENT"]["CHANGED"], email_subject=CONST["MAILING"]["SUBJECT"]["CHANGED"], email_content=CONST["MAILING"]["CONTENT"]["CHANGED"])

        print("Not changed - " + str(datetime.datetime.now()))

        website_cache = website_now
         
        time.sleep(CONST["VERIFICATION_INTERVAL"])
except Exception as err:
    print(err)
    send_email.gmail_send_message(notify_emails=CONST["MAILING"]["RECIPIENT"]["ERROR"], email_subject=CONST["MAILING"]["SUBJECT"]["ERROR"], email_content=CONST["MAILING"]["CONTENT"]["ERROR"] + str(err))