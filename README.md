# Twitter GPU Stock Automation Bot

## Description

The goal of this script was to automate the following of in-stock trackers on Twitter. This bot can do the following:
1. Watch the feeds one or multiple Twitter accounts
2. Analyze the text in new tweets to find URLs and price tags
3. Open the URL linked in a tweet in the default browser if it fits the specified criteria

## Prerequisites
1. You will need a [Twitter Developer account](https://developer.twitter.com/en) in order to use this script. 
You will have to submit an application, but if state exactly what you are going to do with it they should approve your application within 24 hours.
For the scope of the developer application, this bot only reads the data stored in the latests tweets made by specific users.
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
Use `python ./bot.py` to activate the bot.

## [Donations are Appreciated!] (https://www.paypal.com/paypalme/theagentoxygen?locale.x=en_US)
