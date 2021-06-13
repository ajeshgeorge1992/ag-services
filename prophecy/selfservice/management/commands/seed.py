from django.core.management.base import BaseCommand
from selfservice.models import Winner
import csv
from datetime import date, datetime

def seed_from_tsv():
    data = []
    with open(
        "DataFormatted.tsv"
    ) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            single_row = {}
            date_split = row[0].split(",")
            single_row["day"] = date_split[0].strip()
            single_row["date"] = datetime.strftime(
                datetime.strptime(
                    date_split[1].strip() + "," + date_split[2].strip(), "%B %d,%Y"
                ),
                "%Y-%m-%d",
            )
            single_row["draw_time"] = row[1].strip()
            single_row["winner"] = ", ".join(row[2:])
            for index, item in enumerate(row[2:]):
                single_row["w" + str((index + 1))] = int(item)
            data.append(single_row)

    return data

def seed_data():
    for w in seed_from_tsv():
        obj, winner = Winner.objects.get_or_create(
            day = w['day'],
            date = w['date'],
            draw_time= w['draw_time'],
            winner= w['winner'],
            w1 =w['w1'],
            w2 =w['w2'],
            w3 =w['w3'],
            w4 =w['w4'],
            w5 =w['w5'],
            w6 =w['w6'],
            w7 =w['w7'],
            w8 =w['w8'],
            w9 =w['w9'],
            w10 =w['w10'],
            w11 =w['w11'],
            w12 =w['w12'],
            w13 =w['w13'],
            w14 =w['w14'],
            w15 =w['w15'],
            w16 =w['w16'],
            w17 =w['w17'],
            w18 =w['w17'],
            w19 =w['w19'],
            w20 =w['w20']
        )
        if winner:
            print("data inserted")
        # winner.get_or_create()

def clear_data():
  Winner.objects.all().delete()

class Command(BaseCommand):
  def handle(self, *args, **options):
    # clear_data()
    seed_data()
    print("completed")

# seed_from_tsv()