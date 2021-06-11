from typing_extensions import ParamSpecArgs
from bs4 import BeautifulSoup
import requests
from models import Winner



def process_results(ritems):
    for item in ritems:
        date_split = item['date'].split(",")
        item_date =  date_split[0].strip()
        item_day = datetime.strftime(
                datetime.strptime(
                    date_split[1].strip() + "," + date_split[2].strip(), "%B %d,%Y"
                ),
                "%Y-%m-%d",
            )
        obj, winner = Winner.objects.get_or_create(
            day = item_day,
            date = item_date,
            draw_time= item["draw_time"],
            winner = ", ".join(item["winners"]),
            w1 = int(item["winners"][0]),
            w2 = int(item["winners"][1]),
            w3 = int(item["winners"][2]),
            w4 = int(item["winners"][3]),
            w5 = int(item["winners"][4]),
            w6 = int(item["winners"][5]),
            w7 = int(item["winners"][6]),
            w8 = int(item["winners"][7]),
            w9 = int(item["winners"][8]),
            w10 = int(item["winners"][9]),
            w11 = int(item["winners"][10]),
            w12 = int(item["winners"][11]),
            w13 = int(item["winners"][12]),
            w14 = int(item["winners"][13]),
            w15 = int(item["winners"][14]),
            w16 = int(item["winners"][15]),
            w17 = int(item["winners"][16]),
            w18 = int(item["winners"][17]),
            w19 = int(item["winners"][18]),
            w20 = int(item["winners"][19])
        )
        if winner:
            print("data inserted")

def my_scheduled_job():
    file = requests.get("https://www.theluckygene.com/LotteryResults.aspx?gid=OntarioDailyKeno")
    clean_slate = file.text.replace('\n', ' ').replace('\r', '')
    soup = BeautifulSoup(clean_slate, 'html.parser')
    results = soup.find('table', {'class' : 'restbl'}).find_all('tr')[1:-4]
    winners = []
    w_item = {}
    r_items =[]
    passq =0
    draw_d = ""
    for it in results:
        item = it.find_all('td')
        if len(item) == 12:
            draw_d = item[0].text.strip()
            w_item['draw_time'] = item[1].text.strip()
        elif len(item)==11:
            w_item['draw_time'] = item[0].text.strip()

        for i in item[-10:]:
                r_items.append(i.text.strip())

        if len(r_items)==20:
            w_item["date"] = draw_d
            w_item['winners'] = r_items.copy()
            winners.append(w_item.copy())
            w_item.clear()
            r_items.clear()
    process_results(winners)