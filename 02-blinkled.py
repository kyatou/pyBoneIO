'''
 blink led
 type 'sudo -s' before using this script.
'''
import time
from pyBoneIO import *

def setup():
	exportPin(39)
	setToGPIOWrite(39)
	print "Blink LED interval=1 sec"
	print "Ctrl+c to exit."

def loop():
	turnOnGPIO(39)
	delaySec(1)
	turnOffGPIO(39)
	delaySec(1)
	
run(setup,loop)
