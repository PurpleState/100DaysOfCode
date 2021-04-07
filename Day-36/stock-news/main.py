import requests
from twilio.rest import Client
# pip install twilio

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR KEY GOES HERE"
NEW_API_KEY = "YOUR KEY GOES HERE"
TWILIO_SID = "YOUR KEY GOES HERE"
TWILIO_AUTH_TOKEN = "YOUR KEY GOES HERE"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEW_API_KEY,
    "sortBy": "publishedAt"
}

## STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
daily_data = [value for (key, value) in data.items()]

yesterday_closing_price = float(daily_data[0]["4. close"])
day_before_closing_price = float(daily_data[1]["4. close"])
difference = yesterday_closing_price - day_before_closing_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / yesterday_closing_price) * 100)
print(diff_percent)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if abs(diff_percent) > 5:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    three_articles = response.json()["articles"][:3]
    print(three_articles)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    #HINT 1: Consider using a List Comprehension.
    formatted_articles = [f"{COMPANY_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="VIRTUAL_TWILIO_NUMBER",
            to="VERIFIED_NUMBER"
        )

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

