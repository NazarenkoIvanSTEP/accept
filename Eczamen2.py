import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
url="https://privatbank.ua/kak-otpravit-dengi-za-granicu"
file="Bank.csv"
def pars(site = url):
    inf = []
    res = requests.get(site)
    if res.status_code != 200:
        print("Ошибка 1")
    else:
        soup = bs(res.text, features="html.parser")
        soup_list = soup.find_all("article", class_="block-content")
        for i in soup_list:
            inf1 = soup.find("p")
            if inf1:
                inf1 = inf1.get_text(strip = True).replace(" ", "")
            else:
                print("Ошибка 2")
            title = i.find("h2", class_="col-md-7 pull-left wr_inner")
            if title:
                title = title.get_text(strip = True).replace(" ", "")
            inf.append({
                "title": title,
                "INF1": inf1
            })
    print(inf)
pars()
car = ["title", "INF1"]
f=pd.DataFrame(data=pars(),columns=car)
f.to_csv(file,sep=";",encoding='utf8') #encoding="utf8"