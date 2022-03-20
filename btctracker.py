import pandas
import time
from datetime import timezone
import datetime
import telegram_send

btc_addresses = {
    '#3': '1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ',
    'Random': '14m3sd9HCCFJW4LymahJCKMabAxTK4DAqW',
    }

t_time = {}
amount = {}

for key in btc_addresses:
    t_time[key] = 0
    amount[key] = 0

check_again = True

while True:
    time.sleep(1)
    while check_again:
        for whale in btc_addresses:
            transactions_url = 'https://blockchain.info/rawaddr/' + btc_addresses[whale]
            df               = pandas.read_json(transactions_url)
            transactions     = df['txs']
            last_time        = transactions[0]['time']
            last_amount      = transactions[0]['result']
            
            if last_time != t_time[whale]:
                t_time[whale] = last_time
                amount[whale] = last_amount
                
                if int(last_amount) > 0:
                    direction = "accumulating"
                elif int(last_amount) < 0:
                    direction = "dumping"

                btc_amount = int((float(abs(last_amount))/100000000))
                print(f'{whale} is {direction} {btc_amount} BTC')
                telegram_send.send(messages=[f'Whale Alert: {whale} is {direction} {btc_amount} BTC'])

            time.sleep(15)

        check_again = False

    now      = datetime.datetime.now(timezone.utc)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    minutes  = ((now - midnight).seconds) // 60

    if (minutes % 60) == 0:
        telegram_send.send(messages=['Whale watcher checking in.'])    
        time.sleep(60)
        check_again = True
