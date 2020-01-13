#!/usr/bin/python
# -*- coding: utf-8 -*-
"""This example helps you to get used to PIPython."""

# (c)2016-2018 Physik Instrumente (PI) GmbH & Co. KG
# Software products that are provided by PI are subject to the
# General Software License Agreement of Physik Instrumente (PI) GmbH & Co. KG
# and may incorporate and/or make use of third-party software components.
# For more information, please read the General Software License Agreement
# and the Third Party Software Note linked below.
# General Software License Agreement:
# http://www.physikinstrumente.com/download/EULA_PhysikInstrumenteGmbH_Co_KG.pdf
# Third Party Software Note:
# http://www.physikinstrumente.com/download/TPSWNote_PhysikInstrumenteGmbH_Co_KG.pdf


from __future__ import print_function

import time
from pipython import GCSDevice, pitools
from scripts.DAQ import comedi_async
import numpy as np

CONTROLLERNAME = 'E-873'  # 'C-884' will also work
STAGES = None
REFMODES = 'FRF'

def main():
    """Connect, setup system and move stages and display the positions in a loop."""

    # We recommend to use GCSDevice as context manager with "with".
    # The CONTROLLERNAME decides which PI GCS DLL is loaded. If your controller worC-884.DBks
    # with the PI_GCS2_DLL (as most controllers actually do) you can leave this empty.

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


        pidevice.VEL(pidevice.axes[0],0.2) # set velocity to 0.3 mm/s
        pidevice.ACC(pidevice.axes[0], 0.1) # set acceleration to 0.1 mm/s^2
        t = time.time()
        res = comedi_async.sample_time_async([0],[1], 800000, 20)
        pidevice.MOV(pidevice.axes[0], 2) # move to 1 mm
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        pidevice.MOV(pidevice.axes[0],-2)
        while pidevice.IsMoving(axes=pidevice.axes[0])['1']:
            pass
        delta = time.time() - t
        print(delta)
        np.save('result_4.npy', res.get())
        print("")

if __name__ == '__main__':
    main()