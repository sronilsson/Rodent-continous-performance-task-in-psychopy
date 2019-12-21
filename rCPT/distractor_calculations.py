from __future__ import division

import numpy as np
from numpy import genfromtxt
from scipy.stats import norm
import os

Z = norm.ppf

def distractor_calculations(fileout, distractor_filename):
    readfile = fileout
    data_array = np.genfromtxt(readfile, delimiter='\t', skip_header=7, dtype=None)

    single_stimulus_CR = data_array[np.where((data_array[:,2] == 'CORRECT REJECTION') * (data_array[:,25] == '1'))]
    single_stimulus_HITS = data_array[np.where((data_array[:,2] == 'HIT') * (data_array[:,25] == '1'))]
    single_stimulus_FA = data_array[np.where((data_array[:,2] == 'FALSE ALARM') * (data_array[:,25] == '1'))]
    single_stimulus_MISS = data_array[np.where((data_array[:,2] == 'MISS') * (data_array[:,25] == '1'))]
    single_stimulus_blank = data_array[np.where(data_array[:,25] == '1')]

    oneStim_CR_counter = np.size(single_stimulus_CR, 0)
    oneStim_FA_counter = np.size(single_stimulus_FA, 0)
    oneStim_MISS_counter = np.size(single_stimulus_MISS, 0)
    oneStim_HIT_counter = np.size(single_stimulus_HITS, 0)
    oneStim_correct_lat = (single_stimulus_HITS[:,5])
    oneStim_correct_lat = oneStim_correct_lat.astype(float)
    oneStim_incorrect_lat = (single_stimulus_FA[:,5])
    oneStim_incorrect_lat = oneStim_incorrect_lat.astype(float)

    oneStim_blanks = (single_stimulus_blank[:,24])
    oneStim_blanks = oneStim_blanks.astype(int)
    oneStim_totalBlanks = sum(oneStim_blanks)

    try:
        oneStim_mean_correct_lat = sum(oneStim_correct_lat) / float(len(oneStim_correct_lat))
        oneStim_mean_correct_lat = round(oneStim_mean_correct_lat, 4)
    except (ZeroDivisionError):
        oneStim_mean_correct_lat = 0
    try:
        oneStim_mean_incorrect_lat = sum(oneStim_incorrect_lat) / float(len(oneStim_incorrect_lat))
        oneStim_mean_incorrect_lat = round(oneStim_mean_incorrect_lat, 4)
    except (ZeroDivisionError):
        oneStim_mean_incorrect_lat = 0



    try:
        oneStim_HR = oneStim_HIT_counter / (oneStim_HIT_counter + oneStim_MISS_counter)
        oneStim_HR = round(oneStim_HR, 2)

    except (ZeroDivisionError):
        oneStim_HR = 0
    try:
        oneStim_FAR = oneStim_FA_counter / (oneStim_FA_counter + oneStim_CR_counter)
        oneStim_FAR = round(oneStim_FAR, 2)
    except (ZeroDivisionError):
        oneStim_FAR = 0

    if oneStim_HR == 1:
        oneStim_HR = (oneStim_HIT_counter - 0.5) / (oneStim_HIT_counter + oneStim_MISS_counter)
        oneStim_HR = round(oneStim_HR, 2)
    if oneStim_HR == 0:
        if (oneStim_HIT_counter + oneStim_MISS_counter) > 0:
            oneStim_HR = (oneStim_HIT_counter + 0.5) / (oneStim_HIT_counter + oneStim_MISS_counter)
            oneStim_HR = round(oneStim_HR, 2)
        else:
            oneStim_HR = 0
    if oneStim_FAR == 1:
        oneStim_FAR = (oneStim_FA_counter - 0.5) / (oneStim_FA_counter + oneStim_CR_counter)
        oneStim_FAR = round(oneStim_FAR, 2)
    if oneStim_FAR == 0:
        if (oneStim_FA_counter + oneStim_CR_counter) > 0:
            oneStim_FAR = (oneStim_FA_counter + 0.5) / (oneStim_FA_counter + oneStim_CR_counter)
            oneStim_FAR = round(oneStim_FAR, 2)
        else:
            oneStim_FAR = 0
    try:
        oneStim_d = (Z(oneStim_HR) - Z(oneStim_FAR))
        oneStim_d = round(oneStim_d, 2)
    except (ZeroDivisionError):
        oneStim_d = 0
    try:
        oneStim_c = (-(Z(oneStim_HR) + Z(oneStim_FAR)) / 2)
        oneStim_c = round(oneStim_c, 2)
    except (ZeroDivisionError):
        oneStim_c = 0

    congruent_CR = data_array[np.where((data_array[:,2] == 'CORRECT REJECTION') * (data_array[:,25] == '2'))]
    congruent_HITS = data_array[np.where((data_array[:,2] == 'HIT') * (data_array[:,25] == '2'))]
    congruent_FA = data_array[np.where((data_array[:,2] == 'FALSE ALARM') * (data_array[:,25] == '2'))]
    congruent_MISS = data_array[np.where((data_array[:,2] == 'MISS') * (data_array[:,25] == '2'))]
    congruent_distractor = data_array[np.where(data_array[:, 25] == '2')]

    congruent_CR_counter = np.size(congruent_CR, 0)
    congruent_FA_counter = np.size(congruent_FA, 0)
    congruent_MISS_counter = np.size(congruent_MISS, 0)
    congruent_HIT_counter = np.size(congruent_HITS, 0)
    congruent_correct_lat = (congruent_HITS[:,5])
    congruent_correct_lat = congruent_correct_lat.astype(float)
    congruent_incorrect_lat = (congruent_FA[:,5])
    congruent_incorrect_lat = congruent_incorrect_lat.astype(float)

    congruent_distractor_touch = (congruent_distractor[:, 24])
    congruent_distractor_touch = congruent_distractor_touch.astype(int)
    congruent_totalDistractor_touch = sum(congruent_distractor_touch)

    try:
        congruent_mean_correct_lat = sum(congruent_correct_lat) / float(len(congruent_correct_lat))
        congruent_mean_correct_lat = round(congruent_mean_correct_lat, 4)
    except (ZeroDivisionError):
        congruent_mean_correct_lat = 0
    try:
        congruent_mean_incorrect_lat = sum(congruent_incorrect_lat) / float(len(congruent_incorrect_lat))
        congruent_mean_incorrect_lat = round(congruent_mean_incorrect_lat, 2)
    except (ZeroDivisionError):
        congruent_mean_incorrect_lat = 0

    try:
        congruent_HR = congruent_HIT_counter / (congruent_HIT_counter + congruent_MISS_counter)
        congruent_HR = round(congruent_HR, 2)
    except (ZeroDivisionError):
        congruent_HR = 0

    try:
        congruent_FAR = congruent_FA_counter / (congruent_FA_counter + congruent_CR_counter)
        congruent_FAR = round(congruent_FAR, 2)
    except (ZeroDivisionError):
        congruent_FAR = 0

    if congruent_HR == 1:
        congruent_HR = (congruent_HIT_counter - 0.5) / (congruent_HIT_counter + congruent_MISS_counter)
        congruent_HR = round(congruent_HR, 2)
    if congruent_HR == 0:
        if (congruent_HIT_counter + congruent_MISS_counter) > 0:
            congruent_HR = (congruent_HIT_counter + 0.5) / (congruent_HIT_counter + congruent_MISS_counter)
            congruent_HR = round(congruent_HR, 2)
        else:
            congruent_HR = 0
    if congruent_FAR == 1:
        congruent_FAR = (congruent_FA_counter - 0.5) / (congruent_FA_counter + congruent_CR_counter)
        congruent_FAR = round(congruent_FAR,2 )
    if congruent_FAR == 0:
        if (congruent_FA_counter + congruent_CR_counter) > 0:
            congruent_FAR = (congruent_FA_counter + 0.5) / (congruent_FA_counter + congruent_CR_counter)
            congruent_FAR = round(congruent_FAR, 2)
        else:
            congruent_FAR = 0
    try:
        congruent_d = (Z(congruent_HR) - Z(congruent_FAR))
        congruent_d = round(congruent_d, 2)
    except (ZeroDivisionError):
        congruent_d = 0
    try:
        congruent_c = (-(Z(congruent_HR) + Z(congruent_FAR)) / 2)
        congruent_c = round(congruent_c, 2)
    except (ZeroDivisionError, RuntimeWarning):
        congruent_c = 0

    incongruent_CR = data_array[np.where((data_array[:,2] == 'CORRECT REJECTION') * (data_array[:,25] == '3'))]
    incongruent_HITS = data_array[np.where((data_array[:,2] == 'HIT') * (data_array[:,25] == '3'))]
    incongruent_FA = data_array[np.where((data_array[:,2] == 'FALSE ALARM') * (data_array[:,25] == '3'))]
    incongruent_MISS = data_array[np.where((data_array[:,2] == 'MISS') * (data_array[:,25] == '3'))]
    incongruent_distractor = data_array[np.where(data_array[:, 25] == '3')]

    incongruent_CR_counter = np.size(incongruent_CR, 0)
    incongruent_FA_counter = np.size(incongruent_FA, 0)
    incongruent_MISS_counter = np.size(incongruent_MISS, 0)
    incongruent_HIT_counter = np.size(incongruent_HITS, 0)
    incongruent_correct_lat = (incongruent_HITS[:,5])
    incongruent_correct_lat = incongruent_correct_lat.astype(float)
    incongruent_incorrect_lat = (incongruent_FA[:,5])
    incongruent_incorrect_lat = incongruent_correct_lat.astype(float)

    incongruent_distractor_touch = (incongruent_distractor[:, 24])
    incongruent_distractor_touch = incongruent_distractor_touch.astype(int)
    incongruent_totalDistractor_touch = sum(incongruent_distractor_touch)

    try:
        incongruent_mean_correct_lat = sum(incongruent_correct_lat) / float(len(incongruent_correct_lat))
        incongruent_mean_correct_lat = round(incongruent_mean_correct_lat, 2)
    except (ZeroDivisionError):
        incongruent_mean_correct_lat = 0
    try:
        incongruent_mean_incorrect_lat = sum(incongruent_incorrect_lat) / float(len(incongruent_incorrect_lat))
        incongruent_mean_incorrect_lat = round(incongruent_mean_incorrect_lat, 2)
    except (ZeroDivisionError):
        incongruent_mean_incorrect_lat = 0

    try:
        incongruent_HR = incongruent_HIT_counter / (incongruent_HIT_counter + incongruent_MISS_counter)
        incongruent_HR = round(incongruent_HR, 2)
    except (ZeroDivisionError):
        incongruent_HR = 0
    try:
        incongruent_FAR = incongruent_FA_counter / (incongruent_FA_counter + incongruent_CR_counter)
        incongruent_FAR = round(incongruent_FAR, 2)
    except (ZeroDivisionError):
        incongruent_FAR = 0

    if incongruent_HR == 1:
        incongruent_HR = (incongruent_HIT_counter - 0.5) / (incongruent_HIT_counter + incongruent_MISS_counter)
        incongruent_HR = round(incongruent_HR, 2)
    if incongruent_HR == 0:
        if (incongruent_HIT_counter + incongruent_MISS_counter) > 0:
            incongruent_HR = (incongruent_HIT_counter + 0.5) / (incongruent_HIT_counter + incongruent_MISS_counter)
            incongruent_HR = round(incongruent_HR, 2)
        else:
            incongruent_HR = 0
    if incongruent_FAR == 1:
        incongruent_FAR = (incongruent_FA_counter - 0.5) / (incongruent_FA_counter + incongruent_CR_counter)
        incongruent_FAR = round(incongruent_FAR, 2)
    if incongruent_FAR == 0:
        if (incongruent_FA_counter + incongruent_CR_counter) > 0:
            incongruent_FAR = (incongruent_FA_counter + 0.5) / (incongruent_FA_counter + incongruent_CR_counter)
            incongruent_FAR = round(incongruent_FAR, 2)
        else:
            incongruent_FAR = 0
    try:
        incongruent_d = (Z(incongruent_HR) - Z(incongruent_FAR))
        incongruent_d = round(incongruent_d, 2)
    except (ZeroDivisionError, RuntimeWarning):
        incongruent_d = 0
    try:
        incongruent_c = (-(Z(incongruent_HR) + Z(incongruent_FAR)) / 2)
        incongruent_c = round(incongruent_c, 2)
    except (ZeroDivisionError, RuntimeWarning):
        incongruent_c = 0


    single_stimulus_string = str(oneStim_HIT_counter) + '\t' + str(oneStim_MISS_counter) + '\t' + str(oneStim_FA_counter) + '\t' + str(oneStim_CR_counter) + \
        '\t' + str(oneStim_HR) + '\t' + str(oneStim_FAR) + '\t' + str(oneStim_d) + '\t' + str(oneStim_c) + '\t' + str(oneStim_mean_correct_lat) + '\t' + str(oneStim_mean_incorrect_lat) + '\t' + str(oneStim_totalBlanks) + '\n'

    congruent_stimulus_string = str(congruent_HIT_counter) + '\t' + str(congruent_MISS_counter) + '\t' + str(congruent_FA_counter) + '\t' + str(congruent_CR_counter) + \
        '\t' + str(congruent_HR) + '\t' + str(congruent_FAR) + '\t' + str(congruent_d) + '\t' + str(congruent_c) + '\t' + str(congruent_mean_correct_lat) + '\t' + str(congruent_mean_incorrect_lat) + '\t' + str(congruent_totalDistractor_touch) + '\n'

    incongruent_stimulus_string = str(incongruent_HIT_counter) + '\t' + str(incongruent_MISS_counter) + '\t' + str(incongruent_FA_counter) + '\t' + str(incongruent_CR_counter) + \
        '\t' + str(incongruent_HR) + '\t' + str(incongruent_FAR) + '\t' + str(incongruent_d) + '\t' + str(incongruent_c) + '\t' + str(incongruent_mean_correct_lat) + '\t' + str(incongruent_mean_incorrect_lat) + '\t' + str(incongruent_totalDistractor_touch) + '\n'

    header_line = str('HITS') + '\t' + str('MISS') + '\t' + str('FA') + '\t' + str('CR') + '\t' + str('HR') + '\t' + str('FAR') + '\t' + str("d'") + \
        '\t' + str('c') + '\t' + str('Correct_lat') + '\t' + str('Incorrect_lat') + '\t' + str('DIST/BLANK TOUCHES') + '\t' + '\n'

    single_stimulus_output = str('SINGLE STIMULUS PERFORMANCE') + '\n' + str(header_line) + '\n' + single_stimulus_string + ('\n' *5)
    congruent_stimulus_output = str('CONGRUENT PERFORMANCE') + '\n' + str(header_line) + '\n' + congruent_stimulus_string + ('\n' *5)
    incongruent_stimulus_output = str('INCONGRUENT PERFORMANCE') + '\n' + str(header_line) + '\n' + incongruent_stimulus_string + ('\n' * 5)

    with open(distractor_filename, 'w') as f:
        f.write (single_stimulus_output)
        f.write (congruent_stimulus_output)
        f.write (incongruent_stimulus_output)
        f.close()