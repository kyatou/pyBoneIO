'''
 blink user led
 Note: current version pyBBGPIO needs root permission.
 type 'sudo -s' before using this script.
'''
import time
from pyBBGPIO import *

def setup():
	print "Blink user LEDs(LED2 and LED3). interval=1 sec"
	print "Ctrl+c to exit."

def loop():
	
	turnOnUserLED(2)	
	turnOnUserLED(3)	
	delaySec(1)
	turnOffUserLED(2)
	turnOffUserLED(3)
	delaySec(1)
	
run(setup,loop)

