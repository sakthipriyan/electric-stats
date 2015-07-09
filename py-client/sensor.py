'''
Created on 15-Dec-2012

@author: sakthipriyan
'''

import RPi.GPIO as GPIO
import logging

def get_status():
    return not GPIO.input(4)

def init_sensor():
    logging.info('Setting up sensor')    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    

'''    
import time, random
status = True
next_change = 0

def get_status():
    #return not GPIO.input(4)
    
    #TODO - remove this once 
    global status
    if(change_input()):
        status = not status
    return status

def change_input():
    global next_change
    current_time = int(time.time())
    if(next_change < current_time):
        random_time = random.randrange(10,30,5)
        next_change = current_time + random_time
        return True
    else:
        return False
'''    