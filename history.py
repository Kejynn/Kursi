import requests
from bs4 import BeautifulSoup

print("1. Курс на сегодня \n" 
      "2. Курс на определенное число")
vibor = int(input())
if vibor == 1:
    url1 = 'https://cbr.ru'
    response = requests.get(url1)
    bs = BeautifulSoup(response.text, "lxml")

    dol = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[1]
    print("Курс доллара:", dol.text)

    eur = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[3]
    print("Курс евро:", eur.text)
elif vibor == 2:
    data = input("Введите дату в формате дд.мм.гггг \n")
    url = 'https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To=%s' % (data)
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")

    dol = bs.find_all('td')[54]
    print("Курс доллара:", dol.text, "₽")

    eur = bs.find_all('td')[59]
    print("Курс евро:", eur.text, "₽")