#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import required libraries
from __future__ import division
import serial
import time
from psychopy import core, visual, event
import random
from scipy.stats import norm
from math import exp, sqrt
import decimal
import os
import socket
from configparser import ConfigParser
import subprocess
import numpy as np
import csv
from distractor_calculations import distractor_calculations

server = (r"net use W: \\Server name ")
username = r'/user:Username Password'
persistent = r' /persistent:yes'
server_set = server + username + persistent
subprocess.call(server_set)

date_experiment = time.strftime("%Y%m%d-%H%M%S")
folder = time.strftime("/%Y%m%d")
folder_path =  r'W:\Data save directory'
folder_name = folder_path + folder

capSense = 75

config = ConfigParser()
socket.gethostname()
computerName = socket.gethostname()
if computerName == 'hostname 1':
    config.read(r"W:\ directory to config box 1")
if computerName == 'hostname 2':
    config.read(r"W:\ directory to config box 2")
if computerName == 'hostname 3':
    config.read(r"W:\ directory to config box 3")
if computerName == 'hostname 4':
    config.read(r"W:\ directory to config box 4")
if computerName == 'hostname 5':
    config.read(r"W:\ directory to config box 5")
if computerName == 'hostname 6':
    config.read(r"W:\ directory to config box 6")
if computerName == 'hostname 7':
    config.read(r"W:\ directory to config box 7")
if computerName == 'hostname 8':
    config.read(r"W:\directory to config box 8")
if computerName == 'hostname 9':
    config.read(r"W:\directory to config box 9")
if computerName == 'hostname 10':
    config.read(r"W:\directory to config box 10")

trial_type_list_file = (r":\Path to trial type/ order directory ")
trial_type_list = []
status = 0
trial_val = 0
stimulus_list = 0
hits = 0
falseAlarm = 0
miss = 0
CR = 0
ISItouch = 0
falseAlarm_array = []
hits_array = []
global FAR
global HR
global rewardLat
d = 0
c = 0
beta = 0
SI = 0
RI = 0
FAR_array = []
CR_array = []
miss_array = []
ISItouch_array = []
rewardLatArray = []
responsetimeForLat = 0
ResponseLatency = 0
CorrectResponseLatency = 0
MeanCorrectResponseLatency = 0
CorrectResponseLatencyArray = []
IncorrectResponseLatency = 0
MeanIncorrectResponseLatency = 0
IncorrectResponseLatencyArray = []
ResponseLatencyArray = []
start = 0
start_time = 0
sessionStartTime = 0
p1 = p2 = p3 = p4 = p5 = 0
Z = norm.ppf
global meanRewardLat
lastTrial = 'n/a'
global sessionTime
maxTime = config.getint('Session', 'max_time')
CurrentImage = 0
DataArray = []
meanRewardLat = 0
rewardLat = 0.000
ISI_deduction = 0
Persev_ISItouch = 0
Persev_ISItouch_array = []
end_time = 0
max_rewards = config.getint('Session', 'Max_trials')
distractor_calulation_trials = [5, 10, 12, 13, 2, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]
blank_touch_in_trial = 0
blank_touches_sum = 0




# Definition of the analog pin
AnalogPINS = (0, 1, 2, 3, 4)


# functions
def pumpON():
    ArduinoData.write('1')  # LED on
    ArduinoData.write('3')  # Pump on
    PumpStart = time.time()
    while ((time.time() - PumpStart) < pumpTime):
        pass
    ArduinoData.write('4')  # Pump off

def removeStim(pval):
    if pval == 1:
        showingimage = visual.ImageStim(window, size=[450,450], image=ISIimage)
        showingimage.draw()
        window.flip()

# Return d', c, beta, SI, RI

def signal_detection(trial_type,hits, miss, falseAlarm, CR, rewardLat, ResponseLatency, Persev_ISItouch, MeanCorrectResponseLatency, MeanIncorrectResponseLatency, blank_touch_in_trial, blank_touches_sum, fileout, textFile):
    trial_category = 0
    if trial_type < 6:
        trial_category = 1
    if trial_type > 5 and trial_type < 11:
        trial_category = 2
    if trial_type > 10 and trial_type < 15:
        trial_category = 3
    if trial_type > 14 and trial_type < 19:
        trial_category = 3
    if trial_val != 0:
        try:
            HR = hits / (hits + miss)
        except (ZeroDivisionError):
            HR = 0
        try:
            FAR = falseAlarm / (falseAlarm + CR)
        except (ZeroDivisionError):
            FAR = 0

        # Avoid d' infinity
        if HR == 1:
            HR = (hits - 0.5) / (hits + miss)
        if HR == 0:
            if (hits + miss) > 0:
                HR = (hits + 0.5) / (hits + miss)
            else:
                HR = 0
        if FAR == 1:
            FAR = (falseAlarm - 0.5) / (falseAlarm + CR)
        if FAR == 0:
            if (falseAlarm + CR) > 0:
                FAR = (falseAlarm + 0.5) / (falseAlarm + CR)
            else:
                FAR = 0
        try:
            d = (Z(HR) - Z(FAR))
        except (ZeroDivisionError):
            d = 0
        try:
            c = (-(Z(HR) + Z(FAR)) / 2)
        except (ZeroDivisionError):
            c = 0
        try:
            beta = (exp((Z(FAR) ** 2 - Z(HR) ** 2) / 2))
        except (ZeroDivisionError):
            beta = 0
        try:
            SI = ((HR - FAR) / (2 * (HR + FAR) - (HR + FAR) ** 2))
        except (ZeroDivisionError):
            SI = 0
        try:
            RI = ((HR - FAR - 1) / 1 - ((HR - FAR) ** 2))
        except (ZeroDivisionError):
            RI = 0
        HR = decimal.Decimal(HR)
        FAR = decimal.Decimal(FAR)
        d = decimal.Decimal(d)
        c = decimal.Decimal(c)
        beta = decimal.Decimal(beta)
        SI = decimal.Decimal(SI)
        RI = decimal.Decimal(RI)
        centerStimulus.split("\\Stimuli\\")
        path, stimulusName = centerStimulus.split("\\Stimuli\\")
        stimulusName = stimulusName[:-4]
        newtextFile = (str(animalID) + '\t' + str(hits) + '\t' + str(miss) + '\t' + str(falseAlarm) + '\t' + str(CR) + '\t' + str(round(HR,2)) + '\t' +
                       str(round(FAR,2)) + '\t' + str(round(d,2)) + '\t' + str(round(c,2)) + '\t' + str(round(beta,2)) + '\t' + str(round(SI,2)) + '\t' + str(Persev_ISItouch) +
                       '\t' + str(round(RI,2)) + '\t' + str(ISItouch) + '\t' + str(round(MeanCorrectResponseLatency,2)) + '\t' +
                       str(round(MeanIncorrectResponseLatency,2)) + '\t' + str(round(meanRewardLat,2)) + '\t' + str(blank_touches_sum) + '\t' + str(status) + '\n')
        textFile2 = (str(trial_val) + '\t' + str(round(sessionTime,2)) + '\t' + str(lastTrial) + '\t' + str(stimulusName) + '\t' + str(SD) + '\t' + str(round(ResponseLatency,2)) + '\t' +
                     str(round(rewardLat,5)) + '\t' + str(hits) + '\t' + str(miss) + '\t' + str(falseAlarm) + '\t' +
                     str(CR) + '\t' + str(round(HR,2)) + '\t' + str(round(FAR,2)) + '\t' + str(round(d,2)) + '\t' +
                     str(round(c,2)) + '\t' + str(round(beta,2)) + '\t' + str(round(SI,2)) + '\t' + str(round(RI,2)) + '\t' +
                     str(ISItouch) + '\t' + str(round(MeanCorrectResponseLatency,2)) + '\t' +
                     str(round(MeanIncorrectResponseLatency,2)) + '\t' + str(round(meanRewardLat,2)) + '\t' + str(InTrial_Persev_ISItouch) + '\t' + str(blank_touch_in_trial) + '\t'+ str(trial_type) + '\t' + str(trial_category) + '\n')

        with open(fileout, 'ab') as f:
            f.write(textFile2)
            f.close()

        with open(fileout) as fin:
            lines = fin.readlines()
        lines[1] = lines[1].replace(textFile, newtextFile)

        with open(fileout, 'w') as fout:
            for line in lines:
                fout.write(line)

        textFile = newtextFile
        return textFile

def setTrialType(leftStimulus, centerStimulus, rightStimulus):
    # Only 1 central stimulus
    if trial_type == 1:
        leftStimulus = ISIimage
        centerStimulus = correctStim
        rightStimulus = ISIimage
    if trial_type == 2:
        leftStimulus = ISIimage
        centerStimulus = incorrectStim1
        rightStimulus = ISIimage
    if trial_type == 3:
        leftStimulus = ISIimage
        centerStimulus = incorrectStim2
        rightStimulus = ISIimage
    if trial_type == 4:
        leftStimulus = ISIimage
        centerStimulus = incorrectStim3
        rightStimulus = ISIimage
    if trial_type == 5:
        leftStimulus = ISIimage
        centerStimulus = incorrectStim4
        rightStimulus = ISIimage

    #congruent trial types
    if trial_type == 6:
        leftStimulus = correctStim
        centerStimulus = correctStim
        rightStimulus = correctStim
    if trial_type == 7:
        leftStimulus = incorrectStim1
        centerStimulus = incorrectStim1
        rightStimulus = incorrectStim1
    if trial_type == 8:
        leftStimulus = incorrectStim2
        centerStimulus = incorrectStim2
        rightStimulus = incorrectStim2
    if trial_type == 9:
        leftStimulus = incorrectStim3
        centerStimulus = incorrectStim3
        rightStimulus = incorrectStim3
    if trial_type == 10:
        leftStimulus = incorrectStim4
        centerStimulus = incorrectStim4
        rightStimulus = incorrectStim4

    # Incongruent target trial types
    if trial_type == 11:
        leftStimulus = incorrectStim1
        centerStimulus = correctStim
        rightStimulus = incorrectStim1
    if trial_type == 12:
        leftStimulus = incorrectStim2
        centerStimulus = correctStim
        rightStimulus = incorrectStim2
    if trial_type == 13:
        leftStimulus = incorrectStim3
        centerStimulus = correctStim
        rightStimulus = incorrectStim3
    if trial_type == 14:
        leftStimulus = incorrectStim4
        centerStimulus = correctStim
        rightStimulus = incorrectStim4

    # Incongruent non-target trial types
    if trial_type == 15:
        leftStimulus = correctStim
        centerStimulus = incorrectStim1
        rightStimulus = correctStim
    if trial_type == 16:
        leftStimulus = correctStim
        centerStimulus = incorrectStim2
        rightStimulus = correctStim
    if trial_type == 17:
        leftStimulus = correctStim
        centerStimulus = incorrectStim3
        rightStimulus = correctStim
    if trial_type == 18:
        leftStimulus = correctStim
        centerStimulus = incorrectStim4
        rightStimulus = correctStim

    return leftStimulus, centerStimulus, rightStimulus


# Associate port and board
ArduinoData = serial.Serial()
ArduinoData.port = "COM4"
ArduinoData.baudrate = 9600
ArduinoData.timeout = 1
ArduinoData.setRTS(False)
ArduinoData.open()
ArduinoData.reset_input_buffer()
ArduinoData.reset_output_buffer()

# ImageList
stimuli_contrast = config.getint('Session', 'contrast')
stimuli_folder = 'C:\Directory to stimuli locations' + str(stimuli_contrast)
stimulus1 = stimuli_folder + '\Horizontal.jpg'
stimulus2 = stimuli_folder + '\Vertical.jpg'
incorrectStim2 = stimuli_folder + '\DiagLeft.jpg'
incorrectStim3 = stimuli_folder + '\Rings.jpg'
incorrectStim4 = stimuli_folder + '\DiagRight.jpg'
ISIimage = stimuli_folder + str('\Square.jpg')

leftStimulus = stimuli_folder + str('\Horizontal.jpg')
centerStimulus = stimuli_folder + str('\Horizontal.jpg')
rightStimulus = stimuli_folder + str('\Horizontal.jpg')

# perform set up
setIDloop = 1
setCorrect = config.getint('Session', 'target')
Probability = config.getfloat('Session', 'Probability')
animalID = config.getint('Subject', 'animalID')
window = visual.Window(allowGUI=False, size=[1540, 700], units='pix', pos=(0, 0), color=(-1, -1, -1))
window.setMouseVisible(False)
responseMade = False
blackSquare = ISIimage[0]
AfterReward = 7
pumpTime = config.getfloat('Session', 'pump')
distractors = config.getint('Session', 'distractors')
SD = config.getfloat('Session', 'SD')
random_SD = config.getint('Session', 'random_SD')
if random_SD == 1:
    random_SD_min = config.getfloat('Session', 'random_SD_min')
    random_SD_max = config.getfloat('Session', 'random_SD_max')
    random_SD_increment = config.getfloat('Session', 'random_SD_increment')
    SD_list = np.arange(random_SD_min, random_SD_max, random_SD_increment)
ISI_time = config.getint('Session', 'ISI')
nextISI = ISI_time
sessionTime = 0
HR = 0
FAR = 0
nosepoke = 0
noRetrievalTimer = 0
max_trials = config.getint('Session', 'Max_trials')
testingArduinoString = 0
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

while start == 0:
    date_filename = date_experiment
    sessionStartTime = time.time()
    end_time = sessionStartTime + maxTime
    headerFile = ('ID' + '\t' 'HITS ' + '\t' + 'MISSES ' + '\t' + 'FALSE ALARMS ' + '\t' + 'CR ' + '\t' + 'HIT RATE ' + '\t'
                  + 'FALSE ALARM RATE ' + '\t' + "d' " + '\t' + 'CRITERION C ' + '\t' + 'BETA ' + '\t' + 'SI ' + '\t' 'TARGET ISI' + '\t' +
                  'RI ' + '\t' + 'ISI TOUCHES' + '\t' + 'MEAN CORRECT LAT ' + '\t' + 'MEAN INCORRECT LAT ' + '\t' +
                  'MEAN RETRIEVAL LAT' + '\t' + 'TOT. BLANK' + '\t' + 'STATUS' + '\n')
    textFile = ((str(animalID)) + '\t' + (str(hits)) + '\t' + (str(miss)) + '\t' + (str(falseAlarm)) + '\t' + (str(CR)) +'\t'
                + (str(round(HR,2))) + '\t' + (str(round(FAR,2))) + '\t' + (str(round(d,2))) + '\t' + (str(round(c,2))) + '\t' + (str(round(beta,2)))
                + '\t' + (str(round(SI,2))) + (str(Persev_ISItouch)) + '\t' + (str(round(RI,2))) + '\t' + (str(round(ISItouch,2))) +'\t' + (str(round(MeanCorrectResponseLatency,4))) +
                '\t' + (str(round(MeanIncorrectResponseLatency,4))) + '\t' + (str(round(meanRewardLat,2))) + '\t' + (str(blank_touches_sum)) + '\t' + (str(status)) + '\n')
    spaceFile = ('\n' * 5)
    trialHeading = ('TRIAL' + '\t' + 'TIME' + '\t' + 'OUTCOME' + '\t' + 'STIMULUS' + '\t' + 'SD' + '\t' 'RESP. LAT.' + '\t' +
                    'REW. LAT.' + '\t' + 'CUMUL. HITS' + '\t' + 'CUMUL. MISS' + '\t' +
                    'CUMUL. F. A' + '\t' + 'CUMUL. CR' + '\t' +
                    'CUMUL. HR.' + '\t' + 'CUMUL. FAR' +'\t' + "CUMUL. d'" + '\t' +
                    'CUMUL. C' + '\t' + 'CUMUL. BETA' + '\t' + 'CUMUL. SI' + '\t' +
                    'CUMUL. RI' + '\t' + 'CUMUL. ISI TOUCH' + '\t' + 'CUMUL. COR. LAT.' + '\t' +
                    'CUMUL. INCOR. LAT.' + '\t' + 'CUMUL. REW. LAT.' + '\t' + 'TARGET PERSEV.' + '\t' + 'BLANK TOUCHES' + '\t' + 'TRIAL TYPE' + '\t' + 'TRIAL CAT.' + '\n')
    filename = ('/Animal_%s-') % (animalID) + date_experiment + '.csv'
    distractor_filename = ('/animal_%s-') % (animalID) + date_experiment + ('_distractor_data') + '.csv'
    fileout = folder_name + filename
    distractor_filename = folder_name + distractor_filename
    with open(fileout, 'wb') as f:
        f.write(headerFile)
        f.write(textFile)
        f.write(spaceFile)
        f.write(trialHeading)
        f.close()
    if setCorrect == 1:
        correctStim = stimulus1
        incorrectStim1 = stimulus2
    if setCorrect == 2:
        correctStim = stimulus2
        incorrectStim1 = stimulus1
    if setCorrect == 3:
        correctStim = stimulus3
    trial_type_list = np.genfromtxt(trial_type_list_file, delimiter='\t', dtype=None)
    start += 1
    ArduinoData.reset_input_buffer()
    ArduinoData.reset_output_buffer()
  # Read touch-sensor inputs
    while trial_val <= max_trials and sessionTime <= maxTime and hits < max_rewards:
        blank_touch_in_trial = 0
        if (distractors == 1) and (trial_val in distractor_calulation_trials):
            distractor_calculations(fileout,distractor_filename)
        if random_SD == 1:
            SD = int(np.random.choice(SD_list,1))
        trial_type = trial_type_list[stimulus_list]
        testingArduinoString = 0
        InTrial_Persev_ISItouch = 0
        i = 0
        responseMade = False
        trial_timer = time.time()
        touchtimer = time.time()
        while (time.time() - trial_timer) < (nextISI - ISI_deduction):
            testingArduinoString = 0
            ResponseLatency = 0
            rewardLat = 0
            ArduinoString = ArduinoData.readline()
            DataArray = ArduinoString.split(',')
            while testingArduinoString == 0:
                try:
                    Center = int(DataArray[1])
                    testingArduinoString = 1
                except (ValueError, IndexError):
                    ArduinoString = ArduinoData.readline()
                    DataArray = ArduinoString.split(',')
            if Center > capSense and Center > int(DataArray[0]) and Center > int(DataArray[2]):
                trial_timer = time.time()
                if (time.time() - touchtimer) < 0.1:
                    touchtimer = time.time()
                else:
                    ISItouch += 1
                    lastTrial = 'ISI touch'
                    sessionTime = time.time() - sessionStartTime
                    textFile = signal_detection(trial_type, hits, miss, falseAlarm, CR, rewardLat, ResponseLatency,
                                                Persev_ISItouch, MeanCorrectResponseLatency,
                                                MeanIncorrectResponseLatency, blank_touch_in_trial, blank_touches_sum,
                                                fileout, textFile)
                    ISItouch_array.append(time.time())
                    touchtimer = time.time()
        nextISI = ISI_time
        leftStimulus, centerStimulus, rightStimulus = setTrialType(leftStimulus, centerStimulus, rightStimulus)
        CurrentImage = centerStimulus
        showingimageLeft = visual.ImageStim(window, size=[450, 450], image=leftStimulus, pos=(-500, -65))
        showingimageCenter = visual.ImageStim(window, size=[450,450], image=centerStimulus, pos=(0,-65))
        showingimageRight = visual.ImageStim(window, size=[450, 450], image=rightStimulus, pos=(500, -65))
        showingimageLeft.draw()
        showingimageCenter.draw()
        showingimageRight.draw()
        stimulusONtime = time.time()
        window.flip()
        start_time = time.time()
        trialCompleted = 0
        while (time.time() - start_time) < SD and trialCompleted == 0:
            testingArduinoString = 0
            ArduinoString = ArduinoData.readline()
            DataArray = ArduinoString.split(',')
            while testingArduinoString == 0:
                try:
                    nosepoke = int(DataArray[3])
                    Left = int(DataArray[0])
                    Center = int(DataArray[1])
                    Right = int(DataArray[2])
                    testingArduinoString = 1
                except (ValueError, IndexError):
                    ArduinoString = ArduinoData.readline()
                    DataArray = ArduinoString.split(',')
            if CurrentImage == correctStim and Center > capSense and Center > int(DataArray[0]) and Center > int(DataArray[2]):
                responsetimeForLat = time.time()
                removeStim(1)
                trial_val += 1
                stimulus_list += 1
                pumpON()
                responseMade = True
                nextISI = ISI_time + AfterReward
                responseTime = time.time()
                ResponseLatency = (responseTime - stimulusONtime)
                CorrectResponseLatencyArray.append(ResponseLatency)
                MeanCorrectResponseLatency = sum(CorrectResponseLatencyArray) / float(len(CorrectResponseLatencyArray))
                hits += 1
                lastTrial = 'HIT'
                hits_array.append(time.time())
                waitingForRetrieval = True
                trial_timer = time.time()
                touchtimer = time.time()
                ISI_timer = time.time()
                while time.time() <= (responseTime + ISI_time + AfterReward) and ((time.time() - trial_timer) < nextISI):
                    testingArduinoString = 0
                    ArduinoString = ArduinoData.readline()
                    DataArray = ArduinoString.split(',')
                    while testingArduinoString == 0:
                        try:
                            nosepoke = int(DataArray[3])
                            Left = int(DataArray[0])
                            Center = int(DataArray[1])
                            Right = int(DataArray[2])
                            testingArduinoString = 1
                        except (ValueError, IndexError):
                            ArduinoString = ArduinoData.readline()
                            DataArray = ArduinoString.split(',')
                    if nosepoke < 300:
                        ArduinoData.write('2')  # LED off
                        rewardLat = (time.time() - responsetimeForLat)
                        rewardLatArray.append(rewardLat)
                        meanRewardLat = sum(rewardLatArray) / (len(rewardLatArray))
                        sessionTime = time.time() - sessionStartTime
                        textFile = signal_detection(trial_type, hits, miss, falseAlarm, CR, rewardLat, ResponseLatency,
                                                    Persev_ISItouch, MeanCorrectResponseLatency,
                                                    MeanIncorrectResponseLatency, blank_touch_in_trial,
                                                    blank_touches_sum, fileout, textFile)
                        ISI_deduction = time.time() - ISI_timer
                        nextISI = nextISI - ISI_deduction
                        trialCompleted = 1
                        break
                    if Center > capSense and Center > int(DataArray[0]) and Center > int(DataArray[2]):
                        trial_timer = time.time()
                        ISI_timer = time.time()
                        if (time.time() - touchtimer) < 0.1:
                            touchtimer = time.time()
                        else:
                            Persev_ISItouch += 1
                            Persev_ISItouch_array.append(time.time())
                            InTrial_Persev_ISItouch += 1
                            touchtimer = time.time()
                            responseTime = time.time()
                    if (responseTime + ISI_time + AfterReward) < time.time():
                        rewardLat = ISI_time + AfterReward
                        ISI_deduction = time.time() - ISI_timer
                        nextISI = nextISI - ISI_deduction
                        ArduinoData.write('2')
                        sessionTime = time.time() - sessionStartTime
                        textFile = signal_detection(trial_type, hits, miss, falseAlarm, CR, rewardLat, ResponseLatency,
                                                    Persev_ISItouch, MeanCorrectResponseLatency,
                                                    MeanIncorrectResponseLatency, blank_touch_in_trial,
                                                    blank_touches_sum,
                                                    fileout, textFile)
                        break
            if CurrentImage != correctStim and Center > capSense and Center > int(DataArray[0]) and Center > int(DataArray[2]):
                responseMade = True
                removeStim(1)
                responseTime = time.time()
                ResponseLatency = (responseTime - stimulusONtime)
                IncorrectResponseLatencyArray.append(ResponseLatency)
                MeanIncorrectResponseLatency = sum(IncorrectResponseLatencyArray) / float(len(IncorrectResponseLatencyArray))
                trial_val += 1
                falseAlarm += 1
                lastTrial = 'FALSE ALARM'
                falseAlarm_array.append(time.time())
                rewardLat = 0
                ISI_deduction = 0
                sessionTime = time.time() - sessionStartTime
                textFile = signal_detection(trial_type, hits, miss, falseAlarm, CR, rewardLat, ResponseLatency,
                                            Persev_ISItouch, MeanCorrectResponseLatency,
                                            MeanIncorrectResponseLatency, blank_touch_in_trial, blank_touches_sum,
                                            fileout, textFile)
                break
            if ((Left > capSense) and (Left > Center) and (Left > Right)) or ((Right > 75) and (Right > Center) and (Right > Left)):
                trial_timer = time.time()
                if (time.time() - touchtimer) < 0.1:
                    touchtimer = time.time()
                else:
                    blank_touch_in_trial += 1
                    blank_touches_sum += 1
                    touchtimer = time.time()
        if CurrentImage != correctStim and responseMade == False:
            removeStim(1)
            ResponseLatency = 0
            rewardLat = 0
            trial_val += 1
            stimulus_list += 1
            lastTrial = 'CORRECT REJECTION'
            CR += 1
            CR_array.append(time.time())
            ISI_deduction = 0
            sessionTime = time.time() - sessionStartTime
            textFile = signal_detection(trial_type, hits, miss, falseAlarm, CR, rewardLat, ResponseLatency,
                                        Persev_ISItouch, MeanCorrectResponseLatency,
                                        MeanIncorrectResponseLatency, blank_touch_in_trial, blank_touches_sum,
                                        fileout, textFile)
        if CurrentImage == correctStim and responseMade == False:
            removeStim(1)
            rewardLat = 0
            ResponseLatency = 0
            trial_val += 1
            stimulus_list += 1
            lastTrial = 'MISS'
            miss += 1
            miss_array.append(time.time())
            ISI_deduction = 0
            sessionTime = time.time() - sessionStartTime
            textFile = signal_detection(trial_type, hits, miss, falseAlarm, CR, rewardLat, ResponseLatency,
                                        Persev_ISItouch, MeanCorrectResponseLatency,
                                        MeanIncorrectResponseLatency, blank_touch_in_trial, blank_touches_sum,
                                        fileout, textFile)
    if trial_val > max_trials or sessionTime > maxTime or hits >= max_rewards:
        distractor_calculations(fileout, distractor_filename)
        status = 1
        textFile = signal_detection(trial_type, hits, miss, falseAlarm, CR, rewardLat, ResponseLatency,
                                    Persev_ISItouch, MeanCorrectResponseLatency,
                                    MeanIncorrectResponseLatency, blank_touch_in_trial, blank_touches_sum,
                                    fileout, textFile)
        while True:
            #window.flip()
            ArduinoData.write('4')
            time.sleep(0.5)
            ArduinoData.write('2')



















