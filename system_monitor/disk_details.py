# This module shows the CPU % usage, its frequency and load.

import psutil


usage = list(psutil.disk_usage('/'))
for i in range(3):
    usage[i] = usage[i] / 10**9 # converts bytes in gb
usage_perc = usage[-1]

def run():
    print("========== DISK DETAILS ==========")
    print(f"/ Partition Usage: {usage_perc}%")
    print(f"Used space: {usage[1]:.0f}GB")
    print(f"Free space: {usage[2]:.0f}GB")
    print(f"Total space: {usage[0]:.0f}GB")
    print("==================================\n")