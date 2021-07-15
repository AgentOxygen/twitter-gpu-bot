# Twitter GPU Stock Automation Bot

## Description

The goal of this script was to automate the following of in-stock trackers on Twitter. This bot can do the following:
1. Watch the feeds one or multiple Twitter accounts
2. Analyze the text in new tweets to find URLs and price tags
3. Open the URL linked in a tweet in the default browser if it fits the specified criteria

This process does not involve the use of proxies or web-scraping. Everything is done through the use of an approved Twitter API connection.
The only caveat is that since it relies on other bot's notifications you will never be the first to try to buy something, but in reality you almost never need to be *first*
you just don't want to be *last +1*.

## Prerequisites
1. You will need a [Twitter Developer account](https://developer.twitter.com/en) in order to use this script (scraping can result in timeouts and bans so this is a safe and fast way to read Twitter without using something clunky like proxies). 
You will have to submit an application, but if state exactly what you are going to do with it they should approve your application within 24 hours.
For the scope of the developer application, this bot only reads the data stored in the latests tweets made by specific users of your choosing.
After your application is approved, go to the developer portal and paste the keys and tokens into the script so that it can use the API:
~~~
consumer_key = ""
consumer_secret = ""
bearer_token = ""

access_token = ""
access_token_secret = ""
~~~
2. [Python 3 or higher](https://www.python.org/downloads/) installed
3. [Tweepy](https://docs.tweepy.org/en/stable/install.html) installed

## Customizing Your Selection
Example customization
~~~
tracking_user_names = ["fixitfixitfixit", "falcodrin"]
model_prices = [("3070", 650), ("3060", 475), ("3060 Ti", 515), ("6700 xt", 500), ("PS5", 500)]
price_exception_keywords = ["bestbuy", "amd.com"]
~~~
- `tracking_user_names` is a list containing the usernames of Twitter accounts that you want the bot to track. Since each individual developer account has a limited number of requests it can make every 15 minutes, the more accounts you add the more likely your latency will increase. Only put quality tracking sources here.
  
- `model_prices` is a list of tuples with each tuple containing a keyword followed by the maximum price you want the bot the trigger at. The bot will scan tweets to see if they contain any of the keywords. If it finds a match, it will try to find a price tag. If it finds a price tag, it will compare it to the maximum price corresponding to that keyword. If the price tag is less than the specified maximum, then it opens the URL if it can find it.

- `price_exception_keywords` is a list of keywords that are scanned in the event that no price tag is found. This can be useful for camping Best Buy because a single GPU coming in stock is often a warning sign for others.

## Running the Bot
To run the bot, open the terminal of your choice and navigate to the directory where **bot.py** is located. 
I prefer to use Powershell on Windows which you can open by pressing shift and then right clicking in the white space of a File Explorer window.
Use `python ./bot.py` to activate the bot. You do not need to be in the window for it to run, just check on it every so often to make sure it hasn't crashed or bugged out.
- `latency` refers to the time between analyzing the tweet and when it was posted (this is a good measure of lag)

![image](https://user-images.githubusercontent.com/13355009/125833831-b12072db-655a-4df4-abb6-006367715cb5.png)

## Donations are Appreciated! 

<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="business" value="YSVPF57ECUQ4Y" />
<input type="hidden" name="no_recurring" value="0" />
<input type="hidden" name="item_name" value="Donations to my coding efforts" />
<input type="hidden" name="currency_code" value="USD" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1" />
</form>

[Link to Paypal if button is broken](https://www.paypal.com/donate?business=YSVPF57ECUQ4Y&no_recurring=0&item_name=Donations+to+my+coding+efforts&currency_code=USD)
