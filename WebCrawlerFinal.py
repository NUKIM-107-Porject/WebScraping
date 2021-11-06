import bs4
import urllib.request as req
import csv
from csv import writer
import os

if os.path.exists("CreditCardInformation.csv"):
    os.remove("CreditCardInformation.csv")

#花旗銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E8%8A%B1%E6%97%97%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    header = ['CreditCards', 'Domestic', 'Overseas', 'MobilePayment']
    thewriter.writerow(header)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#匯豐銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E6%BB%99%E8%B1%90%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#渣打銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E6%B8%A3%E6%89%93%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#星展銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E6%98%9F%E5%B1%95%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#王道銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E7%8E%8B%E9%81%93%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#星光銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E6%96%B0%E5%85%89%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#中國信託
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E4%B8%AD%E5%9C%8B%E4%BF%A1%E8%A8%97"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#國泰世華
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%9C%8B%E6%B3%B0%E4%B8%96%E8%8F%AF"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#玉山銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E7%8E%89%E5%B1%B1%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#台新銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%8F%B0%E6%96%B0%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#聯邦銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E8%81%AF%E9%82%A6%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#美國運通
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E7%BE%8E%E5%9C%8B%E9%81%8B%E9%80%9A"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#遠東商銀
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E9%81%A0%E6%9D%B1%E5%95%86%E9%8A%80"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#台灣企銀
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E8%87%BA%E7%81%A3%E4%BC%81%E9%8A%80"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#彰化銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%BD%B0%E5%8C%96%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#永豐銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E6%B0%B8%E8%B1%90%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#華泰銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E8%8F%AF%E6%B3%B0%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#華南銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E8%8F%AF%E5%8D%97%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#台北富邦
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%8F%B0%E5%8C%97%E5%AF%8C%E9%82%A6"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#第一銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E7%AC%AC%E4%B8%80%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#高雄銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E9%AB%98%E9%9B%84%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#安泰銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%AE%89%E6%B3%B0%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#合作金庫
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%90%88%E4%BD%9C%E9%87%91%E5%BA%AB"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#兆豐銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%85%86%E8%B1%90%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#凱基銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%87%B1%E5%9F%BA%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#台灣樂天
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%8F%B0%E7%81%A3%E6%A8%82%E5%A4%A9"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#台灣銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E8%87%BA%E7%81%A3%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#台中銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%8F%B0%E4%B8%AD%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#日盛銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E6%97%A5%E7%9B%9B%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#元大銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%85%83%E5%A4%A7%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#三信銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E4%B8%89%E4%BF%A1%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#上海商銀
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E4%B8%8A%E6%B5%B7%E5%95%86%E9%8A%80"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#陽信銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E9%99%BD%E4%BF%A1%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close

#土地銀行
url = "https://www.money101.com.tw/%E4%BF%A1%E7%94%A8%E5%8D%A1/%E5%85%A8%E9%83%A8?providers=%E5%9C%9F%E5%9C%B0%E9%8A%80%E8%A1%8C"

request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root = bs4.BeautifulSoup(data, "html.parser")


CreditcardInfo_dict = {}
CreditcardName_list = []
Creditcardnames = root.find_all('div', class_='pr-1')
for Creditcardname in Creditcardnames:
    if Creditcardname.string != None:
        CreditcardInfo_dict[Creditcardname.string] = []
        CreditcardName_list.append(Creditcardname.string)

index = 0  # 0-29
DomesticFeedback = 0
OverseasFeedback = 0
MobilepaymentFeedback = 0

CreditcardFeedbacks = root.find_all(
    'div', class_='flex justify-center items-center min-h-5')
for CreditcardFeedback in CreditcardFeedbacks:
    index_1 = int(index/3)  # 第幾筆信用卡資訊
    index_2 = int(index % 3)  # 哪種資訊
    if CreditcardFeedback.string == None:
        CreditcardFeedback=CreditcardFeedback.find('span', class_='font-body font-bold sm:font-pullquote sm:font-bold')

    if index_2 == 0:
        if CreditcardFeedback.string == '不適用':
            DomesticFeedback = 0
        else:
            DomesticFeedback = float(CreditcardFeedback.string)
    elif index_2 == 1:
        if CreditcardFeedback.string == '不適用':
            OverseasFeedback = 0
        else:
            OverseasFeedback = float(CreditcardFeedback.string)
    elif index_2 == 2:
        if CreditcardFeedback.string == '不適用':
            MobilepaymentFeedback = 0
        else:
            MobilepaymentFeedback = float(CreditcardFeedback.string)
    CreditcardInfo_dict[CreditcardName_list[index_1]] = [
        DomesticFeedback, OverseasFeedback, MobilepaymentFeedback]
    index += 1

print(CreditcardInfo_dict)

with open('CreditCardInformation.csv', 'a', encoding = 'utf-8-sig', newline = '')as f:
    thewriter = writer(f)
    for row in CreditcardInfo_dict:
        feedback=CreditcardInfo_dict[row]
        creditcard_info=[row,feedback[0],feedback[1],feedback[2]]
        thewriter.writerow(creditcard_info)

f.close