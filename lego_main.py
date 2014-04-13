# -*- coding=utf8 -*-
'''
Created on 14.04.2011

@author: jskonst
'''
import lego_drive as drive
import nxt
import time
b = nxt.locator.find_one_brick()
drive1 = drive.Drive(b, nxt.PORT_B)
drive2 = drive.Drive(b, nxt.PORT_C)

def action(a):
    global b
    # b = nxt.find_one_brick(name='MyNXT')
    drive1 = drive.Drive(b, nxt.PORT_B)
    drive2 = drive.Drive(b, nxt.PORT_C)
    drive1.SetParam(1, 1, 1)
    drive2.SetParam(1, 1, 1)
    drive1.start()
    drive2.start()
    drive1.stop()
    drive2.stop()
    if a == "q":
        print "Стоп"
        drive1.stop()
        drive2.stop()
        drive1.join()
        drive2.join()
    else:
        if a == "w":
            print "Вперед"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()
            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)
            drive1.SetParam(-1,degree=90)
            drive2.SetParam(-1,degree=90)
            drive1.start()
            drive2.start()
        if a == "s":
            print "Назад"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(1,degree=90)
            drive2.SetParam(1,degree=90)
            drive1.start()
            drive2.start()
        if a == "a":
            print "Влево"

            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(1, 50,degree=90)
            drive2.SetParam(-1, 50,degree=90)
            drive1.start()
            drive2.start()
        if a == "d":
            print "Вправо"
            drive1.stop()
            drive2.stop()
            drive1.join()
            drive2.join()

            drive1 = drive.Drive(b, nxt.PORT_B)
            drive2 = drive.Drive(b, nxt.PORT_C)

            drive1.SetParam(-1, 50,degree=90)
            drive2.SetParam(1, 50,degree=90)
            drive1.start()
            drive2.start()
