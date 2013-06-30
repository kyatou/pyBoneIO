'''
 Read analog value from temperature sensor
 type 'sudo -s' before using this script.

 connect temperature sensor(lm35dz) output to ain0-ain6.
'''
import time
from pyBoneIO import *

def setup():
	setupAnalogInput()
	print "Blink LED interval=1 sec"
	print "Ctrl+c to exit."

def loop():
	sensorvalues=readAllAnalogInputmV()
	for val in sensorvalues:
		temp=int(val)/10
		print str(temp)+ "\t",
	print ""	
	print "-"*60
	delaySec(1)
	
run(setup,loop)
