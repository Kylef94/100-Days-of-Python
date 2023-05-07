import requests
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "UNPLLQCPZUVK30GP"
endpoint = "https://www.alphavantage.co/query"

api_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": api_key

}


yest_close_date = datetime.date.today() - datetime.timedelta(1)
prev_close_date = datetime.date.today() - datetime.timedelta(2)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

r = requests.get(url=endpoint, params=api_parameters)
data = r.json()
yest_close = float(data['Time Series (Daily)'][str(yest_close_date)]['4. close'])
prev_close = float(data['Time Series (Daily)'][str(prev_close_date)]['4. close'])
daily_return = ((yest_close - prev_close)/prev_close)*100
print(yest_close)
print(prev_close)
print(daily_return)
if daily_return >= 5 or daily_return <= -5:
    print('Get News')

else:
    print('return was {}'.format(daily_return))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

