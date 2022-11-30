import requests
from bs4 import BeautifulSoup

year = input("Введите год \n")
month = input("Введите месяц в формате мм (пример: Январь - 01) \n")
day = int(input("Введите число \n"))

match month:
    case "01":
        day1 = 31 - day
    case "02":
        day1 = 28 - day
    case "03":
        day1 = 31 - day
    case "04":
        day1 = 30 - day
    case "05":
        day1 = 31 - day
    case "06":
        day1 = 30 - day
    case "07":
        day1 = 31 - day
    case "08":
        day1 = 31 - day
    case "09":
        day1 = 30 - day
    case "10":
        day1 = 31 - day
    case "11":
        day1 = 30 - day
    case "12":
        day1 = 31 - day


url = 'https://www.calc.ru/grafik-Bitcoin-k-rublyu-za-%s-%s.html' % (year, month)
response = requests.get(url)
bs = BeautifulSoup(response.text, "lxml")

btc = bs.find_all('td', style='white-space: nowrap;')[day1]
print("Курс биткоина:", btc.text)