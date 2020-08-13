# PRELIMINARIES

# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# MONITORING SCRIPT

# This is a simple script, which downloads the page of VentureBeat,
# and if it find some text, email notification will be send. If no
# matching text, it will wait 1 hour and downloads the page again.

while True:
    # Set the url as VentureBeat
    url = "https://www.wolverinesupplies.com/ProductDetail/BTHBT36058_B-T-AG-APC223-SA--223-Rem---5-56-Nato--264-mm-Barrel--Restricted-#?sortValue=0"
    # Set the header like we are a brower
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    # Download the homepage
    response = requests.get(url, headers=headers)
    # Parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")

    # If the number of times the word "In Stock" occurs on the page is less than 1,
    if str(soup).find("In Stock") == -1:
        # Wait 1 hour,
        time.sleep(3600)
        # Continue with the script,
        continue
    # But if the word "In Stock" occurs any other number of times,
    else:
        # Create an email message with just a subject line,
        msg = "Subject: This is Ning\'s script talking, CHECK IN STOCK"
        # Set the 'from' address,
        fromaddr = 'email'
        # Se the 'to' addresses,
        toaddrs = ['email']

        # Setup the email server,
        server = smtplib.SMTP('smtp.gamail.com', 587)
        server.starttls()
        # Add my account login name and password,
        server.login("email", "password")

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # Send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # Disconnect from the server
        server.quit()

        break