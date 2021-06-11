import csv
from datetime import datetime

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
    