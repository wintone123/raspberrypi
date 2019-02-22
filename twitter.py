import requests, json, tweepy, time, os, random
from tweepy import OAuthHandler


# get weather info
def weather(city_info):
    api_path = "https://api.darksky.net/forecast/ff71d07afe2151cfe268fd8e053e47d6/"
    full_path = api_path + str(city_info[0]) + "," + str(city_info[1])
    weather_json = requests.get(full_path)
    weather_data = json.loads(weather_json.text)
    summary = weather_data['currently']['summary']
    temperature = (weather_data['currently']['temperature'] - 32) * 5 // 9
    humidity = weather_data['currently']['humidity']
    windspeed = weather_data['currently']['windSpeed']
    weather_message = city_info[2] + " current weather: " + summary + ", temp: " + str(temperature) + \
                      ", humidity: " + str(humidity) + ", windspeed: " + str(windspeed)
    return weather_message


# get exchange rate
def exchange(country):
    api_path = "http://data.fixer.io/api/latest?access_key=37850c375f3367365875dbabd05f31b8"
    exchange_json = requests.get(api_path)
    exchange_data = json.loads(exchange_json.text)
    currency = exchange_data['rates'][country]
    exchange_message = "EUR to " + country + ": " + str(currency)
    return exchange_message


# pic selection
def random_pic(pic_dirs):
    y = random.randint(0, len(pic_dirs)-1)
    dir_path = "//media//pi//RaSegate//" + pic_dirs[y]
    pic_files = [i for i in os.listdir(dir_path) if ".gif" or ".jpg" in i]
    x = random.randint(0, len(pic_files)-1)
    pic_path = dir_path + "//" + pic_files[x]
    return pic_path


# twit message 
def messenger(message, pic_path, api):
    api.update_with_media(pic_path, message)


# check status
def check_status(api):
    hour = api.home_timeline()[0]._json["text"][12:14]
    return hour


# twitter API
consumer_key = "QZ6fdy2LCwSdKHJWkvUCcEoLY"
consumer_secret = "KROWSp0s8y8lWa7fpb5qR26KOd7gy5AHel0oPlxPWDnXXe6W2i"
access_token = "372551387-EBPvGWuDsDvayYiHhvxlyuRbx9sthqyxBcdYuSpx"
access_secret = "B0iZ5Y4tRpvjZUsLze6WXQt1LebZ1ZKBXzqXuJY4W5oX4"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

location = [48.1, 11.416667, "Planegg"]
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
current_hour = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())[11:13]
message = "(" + current_time + ") " + weather(location) + "; " + exchange("CNY")
pic_dirs = ["Zhihu", "Weibo"]

while True:
    messenger(message, random_pic(pic_dirs), api)
    time.sleep(15)
    if check_status(api) == current_hour:
        break