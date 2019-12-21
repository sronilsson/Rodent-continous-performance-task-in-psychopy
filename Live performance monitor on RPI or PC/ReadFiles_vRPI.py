#!/usr/bin/python
import csv
import os
from tabulate import tabulate
import numpy as np
import time
x = 0
tabs = r'\\'
s = ('\n')

summaryTable = np.zeros(shape=(10,18))
np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.2f}'.format}, linewidth=200)
data_folder = r"/home/pi/Research_drive/Research_Drive/marlab/marlabspace/boxes_acme/Simon/CPT/Data"
today_folder = time.strftime("/%Y%m%d")
folder_name = fileout = data_folder + today_folder
print folder_name

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
   os.system("clear")

# Store all tables
while True:
    for filename in os.listdir(folder_name):
        filename = os.path.join(folder_name, filename)
        if filename.endswith(".csv"):
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
                    os.system('clear')
                    x = 0
                    summaryTable=summaryTable[summaryTable[:,1].argsort()]
                    headers = ['ID', 'HIT', 'MISS', 'FA', 'CR', 'HR', 'FAR', "d'", 'c', 'b', 'SI', 'ISI.PE.', 'RI', 'ISI.T', 'C.LAT.', 'IC.LAT', 'R.LAT', 'STATUS']
                    table = tabulate(summaryTable, headers, tablefmt="fancy_grid")
                    print color.RED + 'CPT DATA' + '\n' + table
                    summaryTable = np.zeros(shape=(10, 18))
                    time.sleep(5)






