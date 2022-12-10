## Send emails with Gmail API

1. Search "Gmail API" from the google API console [https://console.developers.google.com/] and click "Enable"
2. Follow the steps at https://developers.google.com/gmail/api/quickstart/nodejs. In the quickstart.js file, changing the SCOPES var from ['https://www.googleapis.com/auth/gmail.readonly'] to ['https://mail.google.com/'] in the quickstart js file provided as suggested in troubleshooting at https://nodemailer.com/smtp/oauth2/
3. Use guide in https://developers.google.com/gmail/api/guides/sending and load credentials with:
   import os
   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "token.json"

**Scrapping configuration as to be altered directly in the code**

## Run file in background

`chmod +x script.py`

`nohup python3 -u ./script.py &`
