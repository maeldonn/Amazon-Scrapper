#! /usr/bin/env python3
# coding: utf-8
"""
Created on Tue Apr 9 2020

@author: DONNART Maël
"""

# Imports
import requests
from bs4 import BeautifulSoup
import smtplib
import time
import sys
from getpass import getpass

###########################     Data      ###########################
URL = 'URL OF YOUR AMAZON ARTICLE'

headers = {"User-Agent": "YOUR USER AGENT"}

new_price = None  # The new price your are waiting for
#####################################################################


def clean_price(price):
    list = []
    for c in price:
        try:
            list.append(str(int(c)))
        except:
            if(c == ',' or c == '.'):
                list.append('.')
            else:
                pass
    return float(''.join(list))


def get_scrap_result():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text().strip()
    price = clean_price(soup.find(id="priceblock_ourprice").get_text())
    return [title, price]


def send_email(user, password, scrapResult):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login(user, password)
        subject = "Price decreased"
        body = "Check the new price :\n\n" + URL
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(user, user, message)
        server.quit()
    except:
        print('Connexion to mail server failed.\n')
        sys.exit()


def get_user():
    user = ''
    while(user == ''):
        user = input('mail : ')
        user.replace(' ', '')
    return user


def get_password():
    password = ''
    while(password == ''):
        password = getpass('password : ')
    print('\n')
    return password


def main():
    print('\n')
    if(len(sys.argv) == 1):
        print('You need to enter a number of time to check the price. Type 0 if you want to get the price only one time.')
        sys.exit()
    if(sys.argv[1] == '0'):
        scrap_result = get_scrap_result()
        print(f"The price for {scrap_result[0]} is {scrap_result[1]} €\n")
    else:
        user = get_user()
        password = get_password()
        while(1):
            scrap_result = get_scrap_result()
            if(scrap_result[1] <= float(new_price)):
                send_email(user, password, scrap_result)
                print("Price decreased, a mail has been sent.\n")
                break
            time.sleep(86400/int(sys.argv[1]))


if __name__ == "__main__":
    main()
