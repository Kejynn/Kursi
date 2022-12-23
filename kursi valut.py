
import requests
from bs4 import BeautifulSoup
import json
print("1. Курс валют \n"
      "2. Курс криптовалют\n"
      "3. Калькулятор валют ")

kurs = int(input())

if kurs == 1:
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


elif kurs == 2:
    print("1. Курс на сегодня \n"
          "2. Курс на определенное число")
    vibor = int(input())
    if vibor == 1:
        url2 = 'https://blockchain.info/ticker'

        response = requests.get(url2).text

        res = json.loads(response)
        print("Курс биткоина:", res.get('RUB').get('last'), "₽")

    elif vibor == 2:
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
        
elif kurs == 3:
    print("Какую валюты вы бы хотели превести")
    print("1. Рубли \n"
          "2. Доллары \n"
          "3. Евро \n"
          "4. Биткоины")
    val = int(input())
    if val == 1:
        print("Введите количество рублей:")
        kolvo = int(input())

        print("В какую валюту вы бы хотели перевести рубли?")
        print("1.В Доллары\n"
              "2.В Евро\n"
              "3.В Биткоины")
        rub = int(input())
        if rub == 1:
            url1 = 'https://cbr.ru'
            response = requests.get(url1)
            bs = BeautifulSoup(response.text, "lxml")

            dol = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[1]
            dolint = float(dol.text[:6].replace(",", "."))

            itog = kolvo / int(dolint)
            print(kolvo, "₽ в долларах:", itog, "$")

        if rub == 2:
            url1 = 'https://cbr.ru'
            response = requests.get(url1)
            bs = BeautifulSoup(response.text, "lxml")

            eur = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[3]
            eurint = float(eur.text[:6].replace(",", "."))

            itog = kolvo / int(eurint)
            print(kolvo, "₽ в евро:", itog, "€")

        if rub == 3:
            url2 = 'https://blockchain.info/ticker'

            response = requests.get(url2).text

            res = json.loads(response)
            btc = float(res.get('RUB').get('last'))

            itog = kolvo / btc
            print(kolvo, "₽ в биткоинах:", itog, "BTC")



    if val == 2:
        print("Введите количество долларов:")
        kolvo = int(input())

        print("1.В Рубли\n"
              "2.В Евро\n"
              "3.В Биткоины")
        dollar = int(input())

        if dollar == 1:
            url1 = 'https://cbr.ru'
            response = requests.get(url1)
            bs = BeautifulSoup(response.text, "lxml")

            dol = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[1]
            dolint = float(dol.text[:6].replace(",", "."))

            itog = kolvo * int(dolint)
            print(kolvo, "$ в рублях:", itog, "₽")

        if dollar == 2:
            url1 = 'https://cbr.ru'
            response = requests.get(url1)
            bs = BeautifulSoup(response.text, "lxml")

            dol = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[1]
            dolint = float(dol.text[:6].replace(",", "."))

            eur = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[3]
            eurint = float(eur.text[:6].replace(",", "."))

            itog = (kolvo * int(dolint)) / int(eurint)
            print(kolvo, "$ в евро:", itog, "€")

        if dollar == 3:
            url2 = 'https://blockchain.info/ticker'

            response = requests.get(url2).text

            res = json.loads(response)
            btc = float(res.get('USD').get('last'))

            itog = kolvo / btc
            print(kolvo, "$ в биткоинах:", itog, "BTC")


    if val == 3:
        print("Введите количество евро:")
        kolvo = int(input())

        print("1.В Рубли\n"
              "2.В Доллары\n"
              "3.В Биткоины")
        euro = int(input())

        if euro == 1:
            url1 = 'https://cbr.ru'
            response = requests.get(url1)
            bs = BeautifulSoup(response.text, "lxml")

            eur = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[3]
            eurint = float(eur.text[:6].replace(",", "."))

            itog = kolvo * int(eurint)
            print(kolvo, "€ в рублях", itog, "₽")

        if euro == 2:
            url1 = 'https://cbr.ru'
            response = requests.get(url1)
            bs = BeautifulSoup(response.text, "lxml")

            dol = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[1]
            dolint = float(dol.text[:6].replace(",", "."))

            eur = bs.find_all('div', 'col-md-2 col-xs-9 _right mono-num')[3]
            eurint = float(eur.text[:6].replace(",", "."))

            itog = (kolvo * int(eurint)) / int(dolint)
            print(kolvo, "€ в долларах:", itog, "$")

        if euro == 3:
            url2 = 'https://blockchain.info/ticker'

            response = requests.get(url2).text

            res = json.loads(response)
            btc = float(res.get('EUR').get('last'))

            itog = kolvo / btc
            print(kolvo, "€ в биткоинах:", itog, "BTC")


    if val == 4:
        print("Введите количество биткоинов:")
        kolvo = int(input())

        print("1.В Рубли\n"
              "2.В Доллары\n"
              "3.В Евро")
        btc = int(input())

        if btc == 1:
            url2 = 'https://blockchain.info/ticker'

            response = requests.get(url2).text

            res = json.loads(response)
            btc = float(res.get('RUB').get('last'))

            itog = kolvo * btc
            print(kolvo, "BTC в рублях:", itog, "₽")

        if btc == 2:
            url2 = 'https://blockchain.info/ticker'

            response = requests.get(url2).text

            res = json.loads(response)
            btc = float(res.get('USD').get('last'))

            itog = kolvo * btc
            print(kolvo, "BTC в долларах:", itog, "$")

        if btc == 3:
            url2 = 'https://blockchain.info/ticker'

            response = requests.get(url2).text

            res = json.loads(response)
            btc = float(res.get('EUR').get('last'))

            itog = kolvo * btc
            print(kolvo, "BTC в евро:", itog, "€")
