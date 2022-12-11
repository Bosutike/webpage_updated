# Webpage_updated

This repository contains a python script that notifies by email when an website is updated.

It works by requesting an website body and scrapping a specific part which is copared with the cached version.

The scrapping configuration as to be altered directly in the code.

## How to use

#### Requirements

Python 3 or higher installed;
pip installed.

#### Configure Gmail API and generate access token:

1. Search "Gmail API" from the google API console [https://console.developers.google.com/] and click "Enable"
2. Follow the steps at https://developers.google.com/gmail/api/quickstart/nodejs. In the quickstart.js file, changing the SCOPES var from ['https://www.googleapis.com/auth/gmail.readonly'] to ['https://mail.google.com/'] in the quickstart js file provided as suggested in troubleshooting at https://nodemailer.com/smtp/oauth2/
3. Use guide in https://developers.google.com/gmail/api/guides/sending and load credentials with:
   import os
   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "token.json"

#### Python related configs:

1. Install all dependencies by running `pip install -r requirements.txt`
2. Create CONSTANTS.py file from template CONSTANTS.py.template with the desired configurations.

#### Run script

Run the script direcly with:
`python3 script.py`

Run script in the background with: (Unix-like operating system)
`chmod +x script.py`
`nohup python3 -u ./script.py &`
