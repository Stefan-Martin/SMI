import os
import struct
import numpy as np
import comedi
from multiprocessing.pool import ThreadPool

def sample_time_async(channels, gains, frequency_hz, scan_time_s, comedi_port='/dev/comedi0', buffer_size=1000000000):
    """Asyncronously sample multiple channels for a fixed amount of time.

    This function uses a ThreadPool to collect data in the background. Call
    result.get() to get the raw data whenever you want it.

    Args:
        channels: A list of ints representing which channels to sample from.
        gains: A list containing a gain for each channel.
        frequency_hz: desired sampling frequency in Hz.
        scan_time_s: how long to sample for.
        comedi_port: specify where the comedi device is mounted.
        buffer_size: memory buffer size in bytes (??)

    Returns:
        An ApplyResult that yeilds the sampled data when you call .get() on it.
    """
    def do_sampling():
        dev = comedi.comedi_open(comedi_port)
        if not dev: raise Exception(
            "Error opening Comedi device at {}".format(comedi_port))
        fd = comedi.comedi_fileno(dev)
        if fd <= 0: raise Exception(
            "Error obtaining Comedi device file descriptor")

        # set up sampling info
        period_ns = int((1.0e9) / frequency_hz)
        nscans = scan_time_s * frequency_hz

        channel_list = comedi.chanlist(n_channels)

        aref = [comedi.AREF_GROUND] * n_channels
        for index in range(n_channels):
            channel_list[index] = comedi.cr_pack(channels[index],
                                                 gains[index], aref[index])

        cmd = comedi.comedi_cmd_struct()
        ret = comedi.comedi_get_cmd_generic_timed(dev, 0, cmd,
                                                  n_channels, period_ns)
        cmd.chanlist = channel_list  # adjust for our particular context
        cmd.chanlist_len = n_channels
        cmd.scan_end_arg = n_channels
        if cmd.stop_src == comedi.TRIG_COUNT: cmd.stop_arg = nscans
        comedi.comedi_command_test(dev, cmd)
        datastr = ()
        comedi.comedi_command(dev, cmd)

        while (1):
            data = os.read(fd, buffer_size)
            if len(data) == 0:
                break
            n = len(data) / 2  # 2 bytes per 'H'
            format = repr(int(n)) + 'H'
            datastr = datastr + struct.unpack(format, data)

        return np.reshape(datastr, (-1, n_channels))

    n_channels = len(channels)
    sampling_pool = ThreadPool(processes=1)
    async_result = sampling_pool.apply_async(do_sampling)
    return async_result


