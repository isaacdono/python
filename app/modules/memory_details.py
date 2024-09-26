# This module shows the RAM ans swap metrics.

import psutil

# Get virtual memory (RAM) statistics:
# returns a named tuple with total, available, percent used, etc.
metrics = psutil.virtual_memory()

# Get swap memory statistics:
# returns a named tuple with total, used, free, percent used, etc.
swap = psutil.swap_memory()

def run():
    print("======== MEMORY DETAILS ========")
    
    # Display percentage of RAM currently in use
    print(f"RAM Usage: {metrics[2]}%")
    
    # Display total RAM, converting bytes to gigabytes
    print(f"Total RAM: {metrics[0] / 10**9:.0f}GB")
    
    # Display percentage of swap memory currently in use
    print(f"Swap Usage: {swap[3]}%")
    
    # Display total swap memory, converting bytes to gigabytes
    print(f"Total Swap: {swap[0] / 10**9:.0f}GB")
    
    print("================================\n")
