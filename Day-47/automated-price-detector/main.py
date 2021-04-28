from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.com/dp/B079LY61FP/ref=sspa_dk_detail_6?psc=1&pd_rd_i=B079LY61FP&pd_rd_w=XEPv5&pf_rd_p=085568d9-3b13-4ac1-8ae4-24a26c00cb0c&pd_rd_wg=93TxG&pf_rd_r=WH0X97W073T0G4W7H0YN&pd_rd_r=daecb0a5-2808-4b0c-abd6-e906cb5db4c3&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFXTkI5WE1KVUNRT1EmZW5jcnlwdGVkSWQ9QTA5MDUzMDExSDI0NDBEQ1dYWTVKJmVuY3J5cHRlZEFkSWQ9QTA0Njg0MjkzRTRRT0ZESE5YUDVEJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
BUY_PRICE = 50
# Scraping Amazon Product Page
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, 'lxml')

# Getting price of item as a float
price_span = soup.find("span", id="price_inside_buybox")
price_without_currency = price_span.getText().split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

#Getting title
title = soup.find(id="productTitle").get_text().strip()
print(title)


if price_as_float < BUY_PRICE:
    message = f"{title} is now {price_as_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
