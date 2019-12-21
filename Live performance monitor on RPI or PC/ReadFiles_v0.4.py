#!/usr/bin/python
import csv
import os
from tabulate import tabulate
import numpy as np
import time
import codecs
x = 0
summaryTable = np.zeros(shape=(10,19))
np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.2f}'.format}, linewidth=200)
data_folder = r"W:\marlab\marlabspace\Boxes_acme\Simon\CPT\Data"
today_folder = time.strftime("/%Y%m%d")
date_time = time.strftime("%Y%m%d-%H%M%S")
filename = ('/Summary_file_') + date_time + '.csv'
fileout2 = data_folder + today_folder + filename
folder_name = fileout = data_folder + today_folder


class color:
    RED = '\033[91m'

def clear():
   os.system("cls" if os.name == "nt" else "clear")

# Store all tables
while True:
    for filename in os.listdir(folder_name):
        filename = os.path.join(folder_name, filename)
        if filename.__contains__("A"):
            with open(filename, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter='\t')
                x = x + 1
                summaryLine = 1
                if x == 1:
                    summaryTable[0] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 2:
                    summaryTable[1] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 3:
                    summaryTable[2] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 4:
                    summaryTable[3] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 5:
                    summaryTable[4] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 6:
                    summaryTable[5] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 7:
                    summaryTable[6] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 8:
                    summaryTable[7] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 9:
                    summaryTable[8] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 10:
                    summaryTable[9] = next((x for i, x in enumerate(csv_reader) if i == summaryLine), None)
                if x == 11:
                    os.system('cls')
                    x = 0
                    summaryTable=summaryTable[summaryTable[:,1].argsort()]
                    summaryTable=np.unique(summaryTable, axis=0)
                    headers = ['ID', 'HIT', 'MISS', 'FA', 'CR', 'HR', 'FAR', "d'", 'c', 'b', 'SI', 'ISI.PE.', 'RI', 'ISI.T', 'C.LAT.', 'IC.LAT', 'R.LAT', 'BLANK', 'STATUS']
                    table = tabulate(summaryTable, headers, tablefmt="fancy_grid")
                    print color.RED + 'CPT DATA' + '\n' + table
                    with open(fileout2, 'w') as f:
                        f.write(str(headers))
                        f.write(tabulate(summaryTable))
                    summaryTable = np.zeros(shape=(10, 19))
                    time.sleep(5)







