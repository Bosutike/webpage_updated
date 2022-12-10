import requests
import time
import send_email
from bs4 import BeautifulSoup
import CONSTANTS
import datetime


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

    div_destaques = soup.find("div", {"id": "mdl-layout__content"})

    return div_destaques

website_page = ""
website_html = request_website(CONSTANTS.URL)
website_cache = scraper(website_html)

while True:
    website_page = ""
    website_html = request_website(CONSTANTS.URL)
    website_now = scraper(website_html)

    if website_cache != website_now:
        print("Changed!!! Notify!!! - " + str(datetime.datetime.now()))
        break

    print("Not changed - " + str(datetime.datetime.now()))

    website_cache = website_now

    time.sleep(300)

  
send_email.gmail_send_message(notify_emails=CONSTANTS.NOTIFY_EMAILS, email_subject=CONSTANTS.EMAIL_SUBJECT, email_content=CONSTANTS.EMAIL_CONTENT)