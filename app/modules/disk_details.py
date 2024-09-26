# This module shows the DISK % usage, its used space, free space, and total space.

import psutil

# Get disk usage statistics for the root ("/") partition, returned as a tuple:
# (total space, used space, free space, percentage of disk used)
usage = list(psutil.disk_usage('/'))

# Convert the first three values from bytes to gigabytes
for i in range(3):
    usage[i] = usage[i] / 10**9

# The last element of the usage list is the percentage of disk used
usage_perc = usage[-1]

def run():
    print("========== DISK DETAILS ==========")
    
    # Display percentage of disk used on the "/" partition
    print(f"/ Partition Usage: {usage_perc}%")
    
    # Display used, free, and total space (rounded to the nearest GB)
    print(f"Used space: {usage[1]:.0f}GB")
    print(f"Free space: {usage[2]:.0f}GB")
    print(f"Total space: {usage[0]:.0f}GB")
    
    print("==================================\n")
