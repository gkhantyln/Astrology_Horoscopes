import requests
from bs4 import BeautifulSoup

#MYNET ZODIAC SIGNS

def burcRequest(path, path2, dogumtarihi, dogumsaati, type):
    if type == "ozellikleri":
        url = f"https://www.mynet.com/kadin/burclar-astroloji/{path}-burcu-{type}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find("div", {"class": "medyanet-content"}).text.strip()
    if type == "uyumu":
        url = f"https://www.mynet.com/kadin/burclar-astroloji/burc-{type}-{path}-{path2}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find("div", {"class": "detail-content-inner"}).text.strip()
    if type == "yukselen":
        url = f"https://www.mynet.com/kadin/burclar-astroloji/{type}-burc-{path}.html?bdate={dogumtarihi}&btime={dogumsaati}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find("div", {"class": "detail-content-inner"}).text.strip()
    else:
        type = "gunluk" if type == "g" else "haftalik"
        url = f"https://www.mynet.com/kadin/burclar-astroloji/{path}-burcu-{type}-yorumu.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.find("div", {"class": "detail-content-inner"}).text.strip()
    content = content.replace(". ", ".\n")
    return content


def main():
    
    path = ""

    secenek = input(
        """
ASTROLOJI BURCLAR | YÜKSELEN BURÇ
---------------------------------------------------------
Günlük yorum için "g" tuşlayın.
Haftalık yorum için "h" tuşlayın.
Burç özellikleri için "o" tuşlayın.
Burçlar arası uyum için "u" tuşlayın.
Yükselen burçlar için "y" tuşlayın.

>>> """
    )

    if secenek == "g":
        burc = input("Burcunuzu girin: ")
        yorum = burcRequest(burc, None, None, None,"gunluk")
        print(f"{burc.capitalize()} burcu için günlük yorum:")
        print(yorum)
    elif secenek == "h":
        burc = input("Burcunuzu girin: ")
        yorum = burcRequest(burc, None, None, None, "haftalik")
        print(f"{burc.capitalize()} burcu için haftalık yorum:")
        print(yorum)
    elif secenek == "o":
        burc = input("Burcunuzu girin: ")
        ozellikler = burcRequest(burc, None, None, None, "ozellikleri")
        print(f"{burc.capitalize()} burcunun özellikleri:")
        print(ozellikler)
    elif secenek == "u":
        path = input("Senin Burcun : ")
        path2 = input("Diğer Burç : ")
        uyumlar = burcRequest(path, path2, None, None, "uyumu")
        print(f"\n{path.capitalize()} - {path2.capitalize()} burçların uyumu :")
        print(uyumlar)
    elif secenek == "y":
        dogumtarihi = int(
            input(
                """
 DOĞUM TARİHİ SEÇİNİZ :
---------------------------------------------
    0 ||  21 Mart - 19 Nisan
    1 ||  20 Nisan - 20 Mayıs
    2 ||  21 Mayıs - 21 Haziran
    3 ||  22 Haziran - 22 Temmuz
    4 ||  23 Temmuz - 22 Ağustos
    5 ||  23 Ağustos - 22 Eylül
    6 ||  23 Eylül - 22 Ekim
    7 ||  23 Ekim - 21 Kasım
    8 ||  22 Kasım - 21 Aralık
    9 ||  22 Aralık - 19 Ocak
  10 || 20 Ocak - 18 Şubat
  11 || 19 Şubat - 20 Mart
---------------------------------------------
>>> """
            )
        )

        dogumsaati = int(
            input(
                """
 DOĞUM SAATİ SEÇİNİZ :
---------------------------------------------
    0 ||  05 - 07
    1 ||  07 - 09
    2 ||  09 - 11
    3 ||  11 - 13
    4 ||  13 - 15
    5 ||  15 - 17
    6 ||  17 - 19
    7 ||  19 - 21
    8 ||  21 - 23
    9 ||  23 - 01
  10 ||  01 - 03
  11 ||  03 - 05
---------------------------------------------
>>> """
            )
        )
        burclar = ["koc", "boga", "ikizler", "yengec", "aslan", "basak", "terazi", "akrep", "yay", "oglak", "kova", "balik"]
        path = burclar[(dogumtarihi + dogumsaati) % len(burclar)]         
        yukselenler = burcRequest(path, None, dogumtarihi, dogumsaati, "yukselen")
        print(f"\nyükselen burcu {path.capitalize()} olanlar için yorum :")
        print(yukselenler)
    else:
        print("Geçersiz seçenek!")


if __name__ == "__main__":
    main()
