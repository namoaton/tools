import urllib.request
import requests
import json
import sys
URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=XXXXXXXX&json"


def get_currency_rate(date):
    r = requests.get(URL.replace('XXXXXXXX', date))
    data = json.loads(r.content.decode())
    for currency in data:
        if currency['cc'] == 'USD':
            print(currency['exchangedate'], currency['rate'])
            return currency['rate']


def get_money_for_date(date, money):
    currency = get_currency_rate(date)
    return currency * money


def get_5_percent(values):
    total_sum = 0
    for val in values:
        total_sum = total_sum + val
    print("Total sum =",total_sum)
    return total_sum * 0.05


def get_data(argv):
    data = argv[1:]
    data_dic = {}
    for val in data:
        val_list = val.split(':')
        data_dic[val_list[0]] = int(val_list[1])
    print(data_dic)
    return (data_dic)


def processing(data_dic):
    money = []
    for key in data_dic:
        money.append(get_money_for_date(key, data_dic[key]))
    print("5 percent = ", get_5_percent(money))


if __name__ == "__main__":
    if len(sys.argv)<2:
        print("python3 five_percent_tax.py YYYYMMDD:SUM")
    processing(get_data(sys.argv))
