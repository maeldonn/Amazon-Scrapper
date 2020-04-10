# AmazonScrapper.py

## Description

This program is a web scrapper. It allow you to recover an amazon article price of your choice.
First, you will need to fill the data part of the program (line 17 to 23).

There are two ways to execute the program. In any case, you need to specify an argument. If you only want to get the price, the required argument is 0.

```
python AmazonScrapper.py 0
```

You can also run the program until the price decrease to a new price. The required argument will be the number of time per day which the program will check the actual price.

```
python AmazonScrapper.py number_of_check
```

To execute the program in this way, you need to have a google account, because it will use gmail servers to send you a mail to warn you about the new price.

### Requirements

This program is based on python 3.
You will need also some libraries and their dependencies. The libraries used are :

- requests
- bs4
- smtplib
- time
- sys
- getpass

All the used libraries are specified in the requirements file.

## Connexion to mail server failed

If you have this message when the program is trying to send you an email you will need to do some manipulations. You have two methods.

### Less secure apps

The first method consist to allow your google account to be accessed by less secure apps. You can do this [here](https://myaccount.google.com/lesssecureapps). It not recommended to use this method.

### App password

The second method consist to enable the two factor authentification of your google account. Next you will need to go in your settings account, in the google app password part and create a new password for this program. It is the most appreciated method !
