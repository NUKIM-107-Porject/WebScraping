import requests
from bs4 import BeautifulSoup
from requests.api import head
from csv import writer
import os

if os.path.exists("MobilePaymentType.csv"):
    os.remove("MobilePaymentType.csv")

source = requests.get('https://www.cardu.com.tw/mpay/detail.php?31640').text
soup = BeautifulSoup(source,'lxml')

with open('MobilePaymentType.csv', 'a', encoding = 'utf-8-sig', newline ='')as f:
    thewriter = writer(f)
    header = ['MobilePaymentType']
    thewriter.writerow(header)

    MobilePaymentInfo = {}
    MobilePaymentType = []
    for article in soup.find_all('span', style = "color:#2980b9") :
        detail = article.find('strong')
        if detail == None:
            detail=article.find('span', style = "font-size:22px")
        print(detail)

        thewriter.writerow(detail)

