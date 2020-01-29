

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

        print('initialize connected stages...')
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


        pidevice.VEL(pidevice.axes[0],0.5) # set velocity to 0.3 mm/s
        pidevice.ACC(pidevice.axes[0], 0.5) # set acceleration to 0.1 mm/s^2
        pidevice.MOV(pidevice.axes[0], 2)
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        print('starting recording')

        res = comedi_async.sample_time_async([0],[1], 300000, 15)

        pidevice.VEL(pidevice.axes[0], 0.007)  # set velocity to 0.3 mm/s
        pidevice.ACC(pidevice.axes[0], 0.01)

        time.sleep(5)
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        print('moving out')
        pidevice.MOV(pidevice.axes[0],1.975)
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        print('moving back')
        pidevice.MOV(pidevice.axes[0], 2)
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        time.sleep(5)
        output = '/home/trevor/smi_data/speed/17-01-2020-2'
        os.makedirs(output, exist_ok=True)
        np.save(os.path.join(output, '15mum_s_solid_OD04.npy'), res.get())
        print('recording done')
        print("")

if __name__ == '__main__':
    main()