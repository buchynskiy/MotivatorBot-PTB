# MotivatorBot-PTB
Telegram Bot built with PTB Library whose main purpose is to motivate users by sending them inspiring quotes

This is another bot that I build back when I was just starting with programming. 

Unique features:
* Motivator Bot has a file with **2000** motivational quotes from all around the internet. I remember it took me quite a while to get them all together because there was no place I could get such an amount of quotes that would be all different. 

* The bot uses an authentication/subscription system of some kind. The user must first subscribe to the bot. By subscribing, UserId of that user is added to the function that sends quotes daily, and it also notifies the moderator about new subscriptions. Only subscribed users will get quotes from the bot.

## Installation
Simply install the libraries from the requirements.txt file:
```bash
  pip install python-telegram-bot==12.7
  pip install python-dotenv==0.19.2
```
Add a API TOKEN to the .env file:
```bash
  APIKEY ="your_api_key"
```
You can now run the bot :)

### Related
[What are Telegram Bots](https://core.telegram.org/bots/features)

[Python-Telegram-Bot Library](https://github.com/python-telegram-bot)