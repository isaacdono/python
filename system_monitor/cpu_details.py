# This module shows the CPU % usage, its frequency and load.

import psutil

perc = round(psutil.cpu_percent * 100, 2)
freq = psutil.cpu_freq()
load = psutil.getloadavg()

print("======= CPU DETAILS =======")
