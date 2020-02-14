

from __future__ import print_function

import time
from pipython import GCSDevice, pitools
from scripts.DAQ import comedi_async
import numpy as np
import os

CONTROLLERNAME = 'E-873'  # 'C-884' will also work
STAGES = None
REFMODES = 'FRF'

def main():

    with GCSDevice(CONTROLLERNAME) as pidevice:
        # Choose the interface according to your cabling.

        #pidevice.ConnectTCPIP(ipaddress='192.168.90.207')
        pidevice.ConnectUSB(serialnum='119058661')

        print('connected: {}'.format(pidevice.qIDN().strip()))


        if pidevice.HasqVER():
            print('version info:\n{}'.format(pidevice.qVER().strip()))

        print('initialize stage...')
        pitools.startup(pidevice, stages=STAGES, refmodes=REFMODES)

        rangemin = pidevice.qTMN() # min position
        rangemax = pidevice.qTMX() # max position
        curpos = pidevice.qPOS() # current position
        curvel = pidevice.qVEL(pidevice.axes[0]) # max vel mm/s/
        curacc = pidevice.qACC(pidevice.axes[0]) # max accel mm/s^2
        print('min position: {},\n'
              'max position: {},\n'
              'current position: {},\n'
              'current max velocity: {},\n'
              'current max accelereation: {}'.format(rangemin, rangemax, curpos, curvel, curacc))

        velocity=0.005 #mm/s
        accel=0.1 #mm/s^2
        OD=0.4 #optical density
        distance_moved=0.01 #mm, 1 direction
        file_index=1 #file index
        sample_rate=400000 #DAQ sample rate
        laser_current=35
        metadata=np.array([velocity,accel,OD,distance_moved,file_index,sample_rate,laser_current]) #metadata for move
        if distance_moved>rangemax['1']:
            return -1
        pidevice.VEL(pidevice.axes[0],0.5) # set velocity to 0.3 mm/s
        pidevice.ACC(pidevice.axes[0], 0.5) # set acceleration
        pidevice.MOV(pidevice.axes[0], 1)
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        print('starting recording')

        res = comedi_async.sample_time_async([0],[1], sample_rate, 6)

        pidevice.VEL(pidevice.axes[0], velocity)  # set velocity
        pidevice.ACC(pidevice.axes[0], accel)   # set accel

        time.sleep(0.5) #wait 1 s before moving
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        print('moving out')
        pidevice.MOV(pidevice.axes[0],1+distance_moved)
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        print('moving back')
        pidevice.MOV(pidevice.axes[0],1)
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        time.sleep(0.5)
        output = '/home/stefan/smi_data/14-02-2020'
        os.makedirs(output, exist_ok=True)
        np.save(os.path.join(output,str(distance_moved) +'mm_'+str(file_index)+'.npy'), res.get())
        np.save(os.path.join(output,str(distance_moved) +'mm_'+str(file_index)+'_meta.npy'),metadata)
        print('done')

if __name__ == '__main__':
    main()