# program to simulate some functions of a car using user input
# exact functionality is on the fly but trying to stick to standards this time ( logging changes etc)
#######################################
#######################################
# CHANGELOG
# 20220302 
# created function keyIn()
# 
# 
# 
# 
# 
# #
#######################################
#######################################
#
#######################################
#######################################
#imports
from queue import Queue
import time,os,sys,threading,random
#######################################
#######################################
# needed variables and predefined things
#
#
key = False # inserted key boolean
engineOn = False # engine on/off
gas_level = [] # think i will use a function to calculate gas level
rpm = 0 # start with 0 RPM
tstat = [] # array of sensors in the car engine for temp 
oil = [] # array for oil health 
speed = 0
accel = 0
velocity = 0
mpg = range(25,30) # standard i think
dashboard = [] # things to display on dash, might make this a dictionary




#######################################
#######################################
# functions
#
def keyIn():
    keyin = input('Would you like to start your car?\n[1] yes\n[2] no\n')
    if int(keyin) == 1: key = True; return key
    if int(keyin) == 2: key = False; return key

def engineStart():
    engineOn = True
    return engineOn
#
#######################################
#######################################
#main flow
#
t = keyIn()
if t: engineStart()
else: print('no action')
#######################################
#######################################s