# This is the primary script for the RTX/PS5 Tracking Bot

import tweepy
from queue import Queue
from threading import Thread
from datetime import datetime, timezone
import time
import webbrowser

consumer_key = ""
consumer_secret = ""
bearer_token = ""

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tracking_user_names = ["fixitfixitfixit", "falcodrin"]
model_prices = [("3070", 650), ("3070 Ti", 650), ("3060", 400), ("PS5", 415)]
price_exception_keywords = ["bestbuy"]

link_queue = Queue()


def open_links(queue: Queue) -> None:
    links_opened = []
    while True:
        link = queue.get()
        if link not in links_opened:
            print(f"Opening link: {link}")
            webbrowser.open(link)
            links_opened.append(link)
        else:
            print(f"Already opened link: {link}")
        queue.task_done()


def within_price_limit(tweet_data_, price: float) -> bool:
    if tweet_data_.full_text.find("$") > 0:
        price_parse = tweet_data_.full_text.split("$")[1].replace(",", "")
        for index, char in enumerate(price_parse):
            if not char.isnumeric():
                price_parse = price_parse[0:index + 1]
        if price >= float(price_parse):
            print(f"${price} >= ${price_parse}, within limits!")
            return True
        print(f"${price} < ${price_parse}, over-priced!")
    print(f"Unable to find price tag in tweet.")
    return False


def contains_price_exception(tweet_data_) -> bool:
    for keyword in price_exception_keywords:
        if keyword.lower() in tweet_data_.full_text.lower():
            print(f"Contains exception keyword: '{keyword}'")
            return True
    return False


def track_tweets(user: str, links_to_open: Queue) -> None:
    refresh_delay = 60 / (900 / len(tracking_user_names) / 15) + 0.25
    last_url = ""
    links_read = []
    last_tweet_timestamp = ""
    while True:
        time.sleep(refresh_delay)
        try:
            tweet_data = api.user_timeline(screen_name=user, count=1, include_rts=False, tweet_mode='extended')[0]
        except IndexError:
            print("IndexError")
            continue
        if last_tweet_timestamp == tweet_data.created_at:
            continue
        last_tweet_timestamp = tweet_data.created_at
        timestamp_converted = tweet_data.created_at.replace(tzinfo=timezone.utc).astimezone(tz=None)
        latency = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None) - timestamp_converted
        print(f"================\n{user}\nTimestamp: {timestamp_converted}\nLatency: {latency}"
              f"\n-----\n{tweet_data.full_text}")
        for model, price in model_prices:
            if model.lower() in tweet_data.full_text.lower():
                print(f"{model} detected!")
                if within_price_limit(tweet_data, price):
                    links_to_open.put(tweet_data.entities['urls'][0]['url'])
                elif contains_price_exception(tweet_data):
                    links_to_open.put(tweet_data.entities['urls'][0]['url'])
                break
            else:
                print(f"{model} not detected.")
        print("================\n")

threads = []
for index, user_name in enumerate(tracking_user_names):
    print(f"Thread {index} tracking @{user_name}")
    t = Thread(target=track_tweets, args=(user_name, link_queue))
    t.daemon = True
    t.start()
    threads.append(t)

open_links(link_queue)

for worker in threads:
    worker.join()
