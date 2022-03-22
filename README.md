### BTC Wallet Tracker

This is a python script for sending notifications of BTC transactions from defined BTC wallets to a custom Telegram channel. 

With the proper Telegram notifications and alerts set, you can receive notifications on your phone or any device using Telegram when a new transaction has been made.

For a complete description and write-up, have a look at [this post](https://onepercent.blog/2022/03/21/bitcoin-whale-tracking-using-python/).

## Installation

In a new terminal window, or from the command line...

```
sudo apt install git
git clone https://github.com/nickpagz/btc-whale-tracker.git
cd btc-whale-tracker
sudo apt-get install python3-pip
pip3 install -r requirements.txt
export PATH="$HOME/.local/bin:$PATH"
```

### Setup a new bot channel on Telegram

Use this link to open the BotFather channel in Telegram:
https://telegram.me/BotFather

Send the message:
```
/newbot
```
... and follow the instructions.

Using the key provided by the BotFather, in the terminal window, type:

```
telegram-send configure
```

You'll be asked to enter the token you received from the BotFather. After you send it, you will receive a password as a response. Open your new user (link provided in the response in the shell window) and send the password.
That's it, the bot is now set up.

To modify the BTC wallets you want to follow, you'll modify the dictionary `btc_addresses` in the code. Follow the same format as shown. The key can be anything you want, preferably a reference to the wallet that makes it easy to remember what it is, and then add the wallet address as the value.
In the sample code I'm following `#3`, so referenced as it's currently the 3rd largest BTC wallet that's not an exchange or fund. The second one is called `Random` as it's a random large wallet I added to show the structure.

Examples:
if you want to only follow #3, your dictionary will look like this:
```
btc_addresses = {
    '#3': '1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ',
    }
```

If you want to add more...
```
btc_addresses = {
    '#3': '1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ',
    'Random': '14m3sd9HCCFJW4LymahJCKMabAxTK4DAqW',
    'Mr. C': 'soMeaDDressFormrCwhatEverThatMaybE',
    }
```

Notes:
- The service providing the transactions has a limit of 1 request every 10 seconds, so be careful not to change the delay settings. In testing I was locked out for a while and had to use a VPN to continue.
- The script currently checks for transactions every hour, on the hour. You can change that on line 52, changing the "60", in minutes, to some other value.
- Line 53 sends out a ping to your bot every hour, as a way of checking in, so you know the script is still running. Delete that line if it gets annoying.
- Lastly, the messages indicate the wallet is "accumulating" or "dumping", though this may not actually be the case. It only indicates Bitcoin going in or out of the wallet. This could be to another wallet, payment for something, or to an exchange. As an example, #3's transactions are typically to and from Coinbase. In most cases, if #3 sends a large amount to Coinbase, it's likely they're about to sell, indicating a price drop may be imminent. All I'm saying is, use the messages with caution.
- It's best to setup and run the script on a VM, like Google Cloud, so it runs continuously. Again, [the post here](https://onepercent.blog/2022/03/21/bitcoin-whale-tracking-using-python/) gives the full details on how to set that up.


