# This module shows the CPU % usage, its frequency and load.

import psutil


usage = psutil.disk_usage('/')
for i in range(3):
    usage[i] = usage[i] / 10^9 # converts bytes in gb
usage_perc = usage[-1]

def run():
    print("========== DISK DETAILS ==========")
    print("/ Partition Usage Percentage: " + usage_perc)
    print("Used space: " + usage_perc[1])
    print("Free space: " + usage_perc[2])
    print("Total space: " + usage_perc[0])
    print("================================\n")