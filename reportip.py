#!/usr/bin/python
#-*-coding:utf8-*-

import requests, bs4, re, tweepy
from tweepy import OAuthHandler
ip_num = re.compile(r'((\d)+).((\d)+).((\d)+).((\d)+)')


def get_ip(ip_num):
    ip_page = requests.get("https://www.iplocation.net/find-ip-address")
    ip_item = bs4.BeautifulSoup(ip_page.text, "html.parser")
    ip_string = ip_item.select('p[align="center"]')[0].getText()
    ip = ip_num.search(ip_string).group()
    return ip


# twit message 
def messenger(message):
    consumer_key = "QZ6fdy2LCwSdKHJWkvUCcEoLY"
    consumer_secret = "KROWSp0s8y8lWa7fpb5qR26KOd7gy5AHel0oPlxPWDnXXe6W2i"
    access_token = "372551387-EBPvGWuDsDvayYiHhvxlyuRbx9sthqyxBcdYuSpx"
    access_secret = "B0iZ5Y4tRpvjZUsLze6WXQt1LebZ1ZKBXzqXuJY4W5oX4"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    api.update_status(message)

ip_lan = get_ip(ip_num)
ip_file = open("/home/pi/Downloads/autotask/ip.txt", "r")
if ip_file.read() != ip_lan + "/n":
    ip_file.close()
    ip_file = open("/home/pi/Downloads/autotask/ip.txt", "w")
    ip_file.write(ip_lan)
    ip_file.close()
    message = "@ragnarok0521 " + ip_lan
    messenger(message)
