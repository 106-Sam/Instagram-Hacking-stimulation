#!/usr/bin/python3.7

#Author: 106_Sam
import time

username = input("Enter Username of IG:\n")


for Loop in range(106):
    if Loop == 0:
        time.sleep(10)
        print("Initializing Facebook database..10%")

    elif Loop == 15:
        time.sleep(10)
        print("Fetching Facebook database...20%")

    elif Loop == 25:
        time.sleep(10)
        print("Redirecting to Instagram....30%")

    elif Loop == 35:
        time.sleep(10)
        print("Confirming Username....40%")

    elif Loop == 45:
        time.sleep(10)
        print("trying to fetch the passwords of", username, "....50%")

    elif Loop == 55:
        time.sleep(10)
        print("Sorry password is encrypted....60%")

    elif Loop == 65:
        time.sleep(10)
        print("Bruteforcing the encrypted password....70%")

    elif Loop == 75:
        time.sleep(10)
        print("Please wait Bruteforcing....80%")

    elif Loop == 85:
        time.sleep(10)
        print("Cracked the encrypted password....90%")

    elif Loop == 95:
        time.sleep(10)
        print("Saving it....100%\n")

    elif Loop == 100:
        print("Hacked", username, "saved password in ~/Insta/hackedpassword.txt")
    

