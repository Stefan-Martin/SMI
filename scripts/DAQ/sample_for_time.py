#!/usr/bin/env python

# sample for some amount of time

#set the paths so python can find the comedi module
import sys, os, string, struct, time, numpy as np

import comedi as c

#open a comedi device
dev=c.comedi_open('/dev/comedi0')
if not dev: raise Exception("Error opening Comedi device")

#get a file-descriptor for use later
fd = c.comedi_fileno(dev)
if fd<=0: raise Exception("Error obtaining Comedi device file descriptor")


# set up channels
n_channels = 2
chans=list(range(0,n_channels))
gains=[0] * n_channels



# set up sampling info
BUFSZ = 10000000000
frequency_hz = 400000
period_ns = int((1.0e9)/frequency_hz)
scan_time_s = 5
nscans= scan_time_s * frequency_hz

#wrappers include a "chanlist" object (just an Unsigned Int array) for holding the chanlist information
mylist = c.chanlist(n_channels) #create a chanlist of length nchans

#now pack the channel, gain and reference information into the chanlist object
#N.B. the CR_PACK and other comedi macros are now python functions
aref =[c.AREF_GROUND] * n_channels
for index in range(n_channels):
	mylist[index]=c.cr_pack(chans[index], gains[index], aref[index])

def dump_cmd(cmd):
	print("---------------------------")
	print("command structure contains:")
	print("cmd.subdev : ", cmd.subdev)
	print("cmd.flags : ", cmd.flags)
	print("cmd.start :\t", cmd.start_src, "\t", cmd.start_arg)
	print("cmd.scan_beg :\t", cmd.scan_begin_src, "\t", cmd.scan_begin_arg)
	print("cmd.convert :\t", cmd.convert_src, "\t", cmd.convert_arg)
	print("cmd.scan_end :\t", cmd.scan_end_src, "\t", cmd.scan_end_arg)
	print("cmd.stop :\t", cmd.stop_src, "\t", cmd.stop_arg)
	print("cmd.chanlist : ", cmd.chanlist)
	print("cmd.chanlist_len : ", cmd.chanlist_len)
	print("cmd.data : ", cmd.data)
	print("cmd.data_len : ", cmd.data_len)
	print("---------------------------")

cmd = c.comedi_cmd_struct()
ret = c.comedi_get_cmd_generic_timed(dev, 0,cmd, n_channels, period_ns)
cmd.chanlist = mylist # adjust for our particular context
cmd.chanlist_len = n_channels
cmd.scan_end_arg = n_channels
if cmd.stop_src==c.TRIG_COUNT: cmd.stop_arg=nscans
c.comedi_command_test(dev,cmd)

datastr = ()
t0 = time.time()
ret = c.comedi_command(dev,cmd)

while (1):
	data = os.read(fd,BUFSZ)
	if len(data)==0:
		break
	n = len(data)/2 # 2 bytes per 'H'
	format = repr(int(n))+'H'
	datastr = datastr + struct.unpack(format,data)
t1 = time.time()

count = 0
data = np.reshape(datastr, (-1, n_channels))


data_len = data.shape[0]
print("start time : ", t0)
print("end time : ", t1)
print("collected {} scans in {} seconds".format(data_len, t1-t0))
period = (t1-t0)/data_len
print('effective sampling period: {} s'.format(period))
print('effective sampling frequency {} Hz'.format(1/period))

	
ret = c.comedi_close(dev)
if ret !=0: raise Exception("comedi_close failed...")
