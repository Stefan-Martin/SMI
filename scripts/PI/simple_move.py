"""Example of how to use stage."""

from __future__ import print_function

from pipython import GCSDevice, pitools

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
        pidevice.VEL(pidevice.axes[0], 0.005)  # set velocity to 0.3 mm/s
        pidevice.ACC(pidevice.axes[0], 0.01)
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

if __name__ == '__main__':
    main()