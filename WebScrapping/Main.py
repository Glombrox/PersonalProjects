import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import keyboard

# # url = "https://www.amazon.com/Valve-Handheld-Console-No-Operating-System/dp/B0BBQRYN9M/
# # ref=sr_1_1?crid=2NE92XI0QTC5N&keywords=steam+deck&qid=1705494295&sprefix=%2Caps%2C603&sr=8-1"
#
# url = ("https://www.amazon.com/Razer-BlackShark-V2-Gaming-Headset/dp/B086PKMZ21/ref=sr_1_1?"
#        "_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&"
#        "keywords=gaming+headsets&pd_rd_r=a2252c89-4140-4f7c-88db-0de9c6f921d6&pd_rd_w=YcscW&pd_rd_wg=ZRQLI&"
#        "pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=E6416DVDV6BYZZ9HTZQX&qid=1705490536&sr=8-1")
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
#                          " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#            "Accept-Language": "fr-DZ,fr;q=0.9,ar-DZ;q=0.8,ar;q=0.7,az-AZ;q=0.6,az;q=0.5,fr-FR;q=0.4,en-US;q=0.3,en;q=0.2",
#            "Accept-Encoding": "gzip, deflate, br"}
#
# page = requests.get(url, headers=headers)
#
# print(page)
#
# # printing the html from the amazon page
# soup1 = BeautifulSoup(page.content, "html.parser")
# # print(soup1)
#
# # making the html more comprehensible
# soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
# # print(soup2)
#
# title = soup2.find(id='productTitle').get_text()
# # print(title)
#
# price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()
# # print(price)
#
# # Striping
# title = title.strip()
# print(title)
#
# print("\n")
#
# price = price.strip()[1:7]
# print(price)
#
# # path = "C:/Users/EM/Desktop/DATA ANALYST/Amazon_Web_Scrapper_DataSet.csv"
# path = "Amazon_Web_Scrapper_DataSet.csv"
#
# date = datetime.date.today()
#
# header = ['Title', 'Price', 'Date']
# data = [title, price, date]
#
# with open("Amazon_Web_Scrapper_DataSet.csv", 'w', newline='', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(data)
#
# df = pd.read_csv(path)
# print(df)
#
# with open("Amazon_Web_Scrapper_DataSet.csv", 'a+', newline='', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(data)

def check_price():

    path = "Amazon_Web_Scrapper_DataSet.csv"

    Url = ("https://www.amazon.com/Razer-BlackShark-V2-Gaming-Headset/dp/B086PKMZ21/"
           "ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a"
           "&keywords=gaming+headsets&pd_rd_r=a2252c89-4140-4f7c-88db-0de9c6f921d6&pd_rd_w=YcscW&pd_rd_wg=ZRQLI"
           "&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=E6416DVDV6BYZZ9HTZQX&qid=1705490536&sr=8-1")


    custom_headers = \
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "fr-DZ,fr;q=0.9,ar-DZ;q=0.8,ar;q=0.7,az-AZ;q=0.6,az;q=0.5,fr-FR;q=0.4,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br"}

    page = requests.get(Url, headers=custom_headers)
    print(page)

    # showing the html from the amazon page
    soup1 = BeautifulSoup(page.content, "html.parser")
    # print(soup1)

    # making the html more comprehensible
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    # print(soup2)

    # collecting the name and price of the product
    title = soup2.find(id='productTitle').get_text()
    price = soup2.find(id='corePriceDisplay_desktop_feature_div').get_text()

    # stripping the name and price of additional text
    title = title.strip()
    price = price.strip()[1:7]

    date = datetime.date.today()

    # creating the dataframe for our "soon to be" dataset
    header = ['Title', 'Price', 'Date']
    data = [title, price, date]

    # with open("Amazon_Web_Scrapper_DataSet.csv", 'w', newline='', encoding='UTF8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     writer.writerow(data)

    # appending new product into the csv file/creating the dataset
    with open("Amazon_Web_Scrapper_DataSet.csv", 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    df = pd.read_csv(path)
    print(df)


# looping for a better price over a set period of time(in seconds)
print("The loop will refresh every 2 hours to add a new entry to the dataset.\n")

while True:
    check_price()
    time.sleep(7200)
    if keyboard.is_pressed('s'):
        break
