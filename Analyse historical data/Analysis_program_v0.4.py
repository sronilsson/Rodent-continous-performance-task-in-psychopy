import numpy as np
from datetime import date, timedelta
import os.path
import os, glob
import fnmatch
import datetime
from io import StringIO
from numpy import inf
import sys
import re

errMsg = '\n' + str('NO MATCHING DATA')
filename = 'temp'
outputFile = 'SummaryAnalysis '
datetime = datetime.datetime.now().strftime("%Y-%m-%d %H.%M")
filename = str(filename) + str(datetime) + str('.csv')
outputFile = str(outputFile) + str(datetime) + str('.csv')

userIN = 0
animalID_array = []

summaryFile = []
fileNames_array = []
dateArray = []
folder_path_array = []
current_path = os.path.dirname(os.path.abspath(__file__))
i = 0
headers = str('ID') + '\t' + str('HITS') + '\t' + str('MISSES') + '\t' + str('FA') + '\t' + str('CR') + '\t' + str('HR') + '\t' + str('FAR') + \
          '\t' + str("d'") + '\t' + str('c') + '\t' + str('BETA') + '\t' + str('SI') + '\t' + str('target ISI') + \
          '\t'+ str('ISI TOUCHES') + '\t' + str('MEAN CORRECT LAT') + '\t' + str('MEAN INCORRECT LAT') + '\t' + str('RI') + '\t' + str('ISI touch') + \
           '\t' + str('MEAN RETRIEVAL LAT') + '\n'

#Specify number of days and dates
start_Date = input("Start date: ")
end_Date = input("End date: ")
StartYear = int(start_Date[:4])
StartMonth = int(start_Date[4:6])
StartDay = int(start_Date[6:8])
EndYear = int(end_Date[:4])
EndMonth = int(end_Date[4:6])
EndDay = int(end_Date[6:8])
d1 = date(StartYear, StartMonth, StartDay)  # start date
d2 = date(EndYear, EndMonth, EndDay)  # end date
delta = d2 - d1
daysInfo = str('MEAN PERFORMANCE FOR DAYS SPANNING') + '\n' + str('Start date') + '\t' + str(d1) + '\n' + str('End date') + '\t' + str(d2) + '\n' + '\n'

Animal_ID = input("Enter animal ID: ")
animalID_array = np.append(animalID_array, Animal_ID)
while userIN == 0:
    Animal_ID = input("Enter another animal ID (or type any letter to finish input and run analysis): ")
    try:
        Animal_ID = int(Animal_ID)
        animalID_array = np.append(animalID_array, Animal_ID)
    except (ValueError):
        userIN = 1

with open(outputFile, 'a') as f:
    f.write(daysInfo)
    print (daysInfo)
    f.write(headers)
    print (headers)
    f.close()

for k in animalID_array:
    Animal_ID = k
    Animal_ID = str('Animal') + str('_') + Animal_ID + str('-')
    for i in range(delta.days + 1):
        date = (str(d1 + timedelta(days=i)))
        date = date.replace("-", "")
        dateArray.append(date)

    dir_list = next(os.walk('.'))[1] #Get subfolders
    matched_folders = np.intersect1d(dir_list, dateArray) #Get subfolders matching the dates
    matched_folders = np.array(matched_folders).tolist()

    for i in matched_folders: #Get complete paths for the folders to search
        folder_path = str(current_path) + str('/') + str([i])
        folder_path = folder_path.replace("'", '')
        folder_path= folder_path.replace('[', '')
        folder_path = folder_path.replace(']', '')
        folder_path_array.append(folder_path)

    for i in folder_path_array: #Get complete filenames with directories for the files to analyse
        folder = i
        for root, dirs, files in os.walk(folder):
            for name in files:
                if name.startswith(Animal_ID):
                    file_path = os.path.join(root, name)
                    fileNames_array.append(file_path)

    for x in fileNames_array:                                   #Read in summaryline and append to array
        readFile = x
        line = open(x, "r").readlines()[1]
        line = str(line)

        with open(filename,'a') as f:
            f.write(line)
            f.close()
    try:
        summaryArray = np.loadtxt(filename)
        summaryArray[np.isinf(summaryArray)] = 0
        summaryArray = np.round(summaryArray, decimals=2)
        meanHits = np.mean(summaryArray[:,1])
        meanMisses = np.mean(summaryArray[:,2])
        meanFA = np.mean(summaryArray[:,3])
        meanCR = np.mean(summaryArray[:,4])
        meanHR = np.mean(summaryArray[:,5])
        meanFAR = np.mean(summaryArray[:,6])
        meanD = np.mean(summaryArray[:,7])
        meanC = np.mean(summaryArray[:,8])
        meanBETA = np.mean(summaryArray[:,9])
        meanSI = np.mean(summaryArray[:,10])
        meanTARGET_ISI = np.mean(summaryArray[:,11])
        mean_RI = np.mean(summaryArray[:, 12])
        meanISI_touch = np.mean(summaryArray[:,13])
        mean_correct_lat = np.mean(summaryArray[:,14])
        mean_incorrect_lat = np.mean(summaryArray[:,15])
        mean_reward_lat = np.mean(summaryArray[:,16])
        Animal_ID = re.sub("[^0-9]", "", Animal_ID)

        printString = str(Animal_ID) + '\t' + str(round(meanHits,2)) + '\t' + str(round(meanMisses, 2)) + '\t' + str(round(meanFA, 2)) + '\t' + str(round(meanCR, 2)) + '\t'+ str(round(meanHR, 2)) + '\t' + \
            str(round(meanFAR, 2)) + '\t' + str(round(meanD, 2)) + '\t' + str(round(meanC, 2)) + '\t' + str(round(meanBETA, 2)) + '\t' + str(round(meanSI, 2)) + '\t' + str(round(meanTARGET_ISI, 2)) + '\t' + \
            str(round(meanTARGET_ISI, 2)) + '\t' + str(round(mean_correct_lat, 2)) + '\t' + str(round(mean_incorrect_lat, 2)) + '\t' + \
            str(round(mean_RI, 2)) + '\t' + str(round(meanISI_touch, 2)) + '\t' + str(round(mean_reward_lat, 2)) + '\n'

        print (printString)

        with open(outputFile, 'a') as f:
            f.write(printString)
            f.close()
    except(OSError):
        print(errMsg)
        with open(outputFile,'a') as f:
            f.write(errMsg)
            f.close()

os.remove(filename)





















































