## Rodent continous performance test (rCPT) written in python2.7 
#### The task use a Windows tablet and a [3D-printed operant chamber](https://github.com/sronilsson/3D_designs/tree/master/operant_box). Stimuli presentation is controlled by [PsychoPy](https://www.psychopy.org/). Rodents respond by capacitance touch detected via the [CapSense](https://playground.arduino.cc/Main/CapacitiveSensor/) library and processed by [pySerial](https://pythonhosted.org/pyserial/). 

#### The rCPT program mirrors and extends the functionality of VisualBasic version and [commercial Lafayette version](http://lafayetteneuroscience.com/products/image-cpt-rats) of the task used in these papers: [[Chi Hun et al. 2015]](https://link.springer.com/article/10.1007/s00213-015-4081-0), [[Mar et al. 2017]](https://link.springer.com/article/10.1007/s00213-017-4679-5), [[Hvoslef-Eide et al 2018]](http://journals.sagepub.com/doi/abs/10.1177/2398212818772962), [[Nilsson et al. 2018]](https://www.nature.com/articles/s41398-018-0295-3.pdf?origin=ppub). 

![alt-text-1](/images/CPT_2.jpg "Distractors")

##### The PsychoPy version supports distractors and stimuli fading.
![alt-text-1](/images/distractors.jpg "Distractors")

##### Generate different contrast stimuli.
![alt-text-1](/images/Image4.jpg "contrast")

##### Set the test parameters for each box through [ConfigParser](https://docs.python.org/2/library/configparser.html) and executed on set of tablets through [PsExec](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec).
![alt-text-1](/images/Image3.jpg "parameters")

##### Monitor live peformance of animals across multiple boxes on a PC, OS, or RaspberryPi using [tabulate](https://pypi.org/project/tabulate/) printed terminal window.
![alt-text-1](/images/Image1.jpg "monitor")

##### CLI access to descriptive and frequentist statistics for blocks of days and multiple animals.
![alt-text-1](/images/Image2.jpg "descriptive statistics")

##### gif demo starting up rCPT locally, on one windows tablet.
![alt-text-1](/images/rCPT_demo.gif "Operant box misc")

##### gif demo extracting descriptive statistics for a block of days, running CLI to access SQL database.
![alt-text-1](/images/data_demo.gif "Operant box misc")
 
