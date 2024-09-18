# Amazon Price Tracker

given_price = 20000.0

# Getting the html page of the product
import requests

amazon_url = "https://www.amazon.in/dp/B0BZP2H373/ref=sspa_dk_detail_0?pd_rd_i=B0BZP2H373&pd_rd_w=Y4HqT&content-id=amzn1.sym.dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_p=dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_r=X95GNPTW0WBBEJEMKJYW&pd_rd_wg=K67pa&pd_rd_r=85df3a65-de82-43dd-adc4-155b5299d54b&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFJN0lJWjFCTEI2U04mZW5jcnlwdGVkSWQ9QTA3NzYyNjUxRzNCOTJHOUc1NFRUJmVuY3J5cHRlZEFkSWQ9QTA4NDU4ODUyRDEyVkk1TElBR09EJndpZGdldE5hbWU9c3BfZGV0YWlsX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
headers = {'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
response = requests.get(amazon_url, headers=headers)

# Using beautifulsoup to scrape the data and find the current price
from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup(response.content, "lxml")

span_tag = soup.find(name="span", class_="a-price-whole")
current_price = float(span_tag.getText().replace(",", "").strip())

product_name = soup.find(name="span", id="productTitle").getText()

# Sending an email if the current price is lower than the price given
import smtplib

if current_price <= given_price:
    my_email = "krrishdummy@gmail.com"
    password = "rvavgalomtfgsgnf"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # tls - transport layer security (encrypts the file)
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="shibenapps@gmail.com",
                            msg=f"Subject:Price is lower!!\nThe price of{product_name}on Amazon is lower than 20,"
                                f"000 rupees.")
