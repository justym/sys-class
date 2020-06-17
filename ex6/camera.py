#coding: utf-8
import webiopi
import os
import datetime

#save pic in dir
SAVEDIR = '/home/pi/sys-ex/ex6'
@webiopi.macro
def camera(no):
    filename = SAVEDIR + '/camera_' + no + '.jpg'
    command = 'fswebcam -r 320x420 -d /dev/video0 ' + filename
    os.system(command)
    os.system('sync')

@webiopi.macro
def dates():
    now = datetime.datetime.now()
    date = "{0:%Y.%m.%d:%H:%M:%S}".format(now)
    return date

