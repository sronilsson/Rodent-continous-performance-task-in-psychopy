import os
import subprocess
import time
import distutils.core
import shutil
subprocess.call(r'net use W:', shell = True)
tabs = r'\\'
s = ('\n')


# Mount network drive with credentials
server = (r"net use "Server Name"")
username = r'/user:Username Password'
persistent = r' /persistent:yes'
server_set = server + username + persistent
subprocess.call(server_set)

# Directory for file IP containing list of computers that are to run (IPs or hostnames)
folderpath_IPfile = ("W:\marlab\marlabspace\Boxes_acme\Simon\CPT\Programs")

# PSexec command, with credentials
username = '-u 'Local computer username'
password = (str('-p 'Local computer username' -i -d -e -s ' ))
pythonloc = ' "Python exe directory" '
CPTloc = ('"CPT file directory"')
psexecloc = 'psexec '

# Create directory for config files
folder = ('/configs')
folder_path =  (r'Directory for saving config files')
folder_name = folder_path + folder
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Loop, creates config files for computers that are to be run
def createConfig():
    filename = ('/config_%s.ini') % (animalID)
    fileout = folder_name + filename
    with open(fileout, 'w') as f:
        f.write('[Subject]' + s + 'animalID = ' + (str(animalID)) + s + s)
        f.write('[Session]' + s + 'SD = ' + (str(sd)) + s + 'target = ' + (str(target)) + s + \
                'ISI = ' + (str(isi)) + s + 'max_trials = ' + (str(trials)) + s + 'distractors = ' + (str(distractors)) + s + 'max_time = ' + (str(max_time)) + s + \
                'Probability = ' + (str(probability)) + s + 'Pump = ' + (str(pump)) + s + 'Contrast = ' + (str(contrast)) + s + \
                'random_SD = ' + (str(random_SD)) + s + 'random_SD_min = ' + (str(random_SD_min)) + s + \
                'random_SD_max = ' + str(random_SD_max) + s + 'random_SD_increment = ' + str(random_SD_increment) + s + s)
        f.write('[Box]' + s + 'IP = ' + (str(host)) + s)
        f.close()

# Creates IP list file
def genFile():
    filename = ('/tabletIPs.txt')
    fileout =  folderpath_IPfile + filename
    with open(fileout, 'w') as f:
        f.write (str(genFileLine1) + (str(genFileLine2)) + (str(genFileLine3)) + (str(genFileLine4)) + (str(genFileLine5)) + (str(genFileLine6)) + (str(genFileLine7)) + (str(genFileLine8)) + (str(genFileLine9)) + (str(genFileLine10)))
        f.close()


# Execution command
def execute():
    execute_command = (psexecloc + '@tabletIPs.txt '+ username + password + pythonloc + CPTloc)
    print execute_command
    filename = ('/start_run.bat')
    fileout = folderpath_IPfile + filename
    with open(fileout, 'w') as f:
        f.write (execute_command)
        f.close()
    filepath = r'File path for generated .bat file'
    p = subprocess.Popen(filepath, stdout = subprocess.PIPE, shell = True)
    stdout, stderr = p.communicate()
    print p.returncode


## ******************************Config BOX 1 ***************************************************
run_box = 1                         #               0 = NO, 1 = YES
host = 'host or IP box 1'           #               Box hostname
target = 2                          #               1 = horizontal, 2 = vertical, 3 = White Square
animalID = 1                        #               Animal ID
sd = 5                              #               Stimulus duration (used if session is set to fixed SD)
isi = 4                             #               Inter-stimulus interval length
trials = 4000                       #               Max session trials
max_time = 2700                     #               Max session time
probability = 0.5                   #               Target probability
pump = 0.05                         #               Pump onset time
distractors = 1                     #               0 = NO distractors, 1 = distractors
contrast = 100                      #               Stimuli cotrast
random_SD = 0                       #               0 = Use fixed SD, 1 = Use variable SD within session
random_SD_min = 0                   #               If random_SD = 1, specify shortest SD
random_SD_max = 0                   #               If random_SD = 1, specify longest SD
random_SD_increment = 2             #               If random_SD = 1, specify increment between SD min / SD max
if run_box == 1:
    genFileLine1 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine1 = ''


################### *************** Config BOX 2 ***************************************************
run_box = 1
host = 'host or IP box 2'
target = 2 #
animalID = 2
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 100
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine2 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine2 = ''


## *************** Config BOX 3 ***************************************************
run_box = 0
host = 'host or IP box 3'
target = 1 #
animalID = 3
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 100
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine3 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine3 = ''

## *************** Config BOX 4 ***************************************************
run_box = 1
host = 'host or IP box 4'
target = 2
animalID = 4
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 100
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine4 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine4 = ''

## *************** Config BOX 5 ***************************************************
run_box = 0
host = 'host or IP box 5'
target = 1
animalID = 5
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 100
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine5 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine5 = ''

## *************** Config BOX 6 ***************************************************
run_box = 0
host = 'host or IP box 6'
target = 2
animalID = 6
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 100
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine6 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine6 = ''

## *************** Config BOX 7 ***************************************************
run_box = 0
host = 'host or IP box 7'
target = 1
animalID = 7
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 100
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine7 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine7 = ''

## *************** Config BOX 8 ***************************************************
run_box = 0
host = 'host or IP box 8'
target = 2
animalID = 8
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 12
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine8 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine8 = ''

## *************** Config BOX 9 ***************************************************
run_box = 0
host = 'host or IP box 9'
target = 1
animalID = 9
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 100
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine9 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine9 = ''

## *************** Config BOX 10 ***************************************************
run_box = 0
host = 'host or IP box 10'
target = 2
animalID = 10
sd = 5
isi = 4
trials = 4000
max_time = 2700
probability = 0.5
pump = 0.05
distractors = 1
contrast = 100
random_SD = 0
random_SD_min = 0
random_SD_max = 0
random_SD_increment = 0
if run_box == 1:
    genFileLine10 = (host + s)
    createConfig()
if run_box == 0:
    genFileLine10 = ''

## *************** Generate txt file for batch ***************************************************
genFile()

## *************** Run execute *****************************************
execute()
