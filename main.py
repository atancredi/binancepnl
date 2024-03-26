from calcuation import profit_loss
from binance.client import Client
import pandas as pd
from dotenv import load_dotenv
from os import environ as env

load_dotenv()

key = env.get("BINANCE_KEY")
secret = env.get("BINANCE_SECRET")

client = Client(key, secret)

account = client.get_account()
balances = [x for x in account["balances"] if float(x["free"]) + float(x["locked"]) > 0]

profits = []
for asset in [x["asset"] for x in balances if x["asset"] not in ["USDT", "EASY"]]:
    print([x for x in balances if x["asset"] == asset])
    pnl = profit_loss(market=f'{asset}-USDT',start_date='2022-01-01', end_date='2024-03-26', client=client, showlog=True)
    profits.append(pnl["total_profit(base)"])
print(sum(profits))

# for c in ["BTC", "BNB", "ETH", "ADA", "AGIX", "UNI", "ETH"]:
    # pnl = profit_loss(market=f'{c}-USDT',start_date='2022-01-01', end_date='2024-03-26', client=client, showlog=False)

# from datetime import datetime


# dates_df = pd.DataFrame(index=[datetime(2020,1,1), datetime(2021,12,31)])
# dates = dates_df.resample('d').first().index[::30]
# profilio = []
# for s in ['BTC-USDT', 'BNB-USDT', 'LINK-USDT', 'ADA-USDT', 'CAKE-USDT', 'UNI-USDT', 'ETH-USDT']:        
#     for start_date, end_date in zip(dates[:], dates[1:]):        
#         pnl = profit_loss(market=s, start_date=start_date.strftime("%Y-%m-%d"), end_date=end_date.strftime("%Y-%m-%d"), client=client)
#         profilio.append({'date': end_date, 'symbol':s, 'pnl':pnl['total_profit(quote)']})    
    
# profilio_df = pd.DataFrame(profilio)
# profilio_df = profilio_df.rename({'symbol':'stock_id'}, axis='columns')    
# RealizedProfitLoss(profilio_df).run_dash()