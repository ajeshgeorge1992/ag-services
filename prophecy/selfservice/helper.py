import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests

class helper():

    def seed_from_tsv():
        data =[]
        with open("/Users/ajeshgeorge/Documents/Django Projects/Lot/DataFormatted.tsv") as fd:
            rd = csv.reader(fd, delimiter="\t", quotechar='"')
            for row in rd:
                single_row ={}
                date_split= row[0].split(",")
                single_row['day']=date_split[0].strip()
                single_row['date'] = datetime.strftime(datetime.strptime(date_split[1].strip()+','+date_split[2].strip(), '%B %d,%Y'),'%Y-%m-%d')
                single_row['winner'] = ', '.join(row[2:])
                single_row['draw_time'] = row[1].strip()
                for index, item in enumerate(row[2:]):
                    single_row["w"+str((index+1))] = int(item)
                data.append(single_row)
                
        return data

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
    # print(winners)
    process_results(winners)

my_scheduled_job()