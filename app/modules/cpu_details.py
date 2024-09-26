# # This module shows the CPU % usage, its frequencies and average relative load.

import psutil

# Collect CPU usage percentage over the last interval (default 1 second)
perc = psutil.cpu_percent() * 100

# Get the CPU frequency in MHz (current, min, max)
freq = psutil.cpu_freq()

# Get the average load on the CPU over 1, 5, and 15 minutes,
# and convert to a percentage relative to the number of CPU cores
load_perc = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]

def run():
    print("========== CPU DETAILS ==========")
    
    # Display CPU percentage (rounded to two decimal places)
    print(f"CPU Percentage: {perc:.2f}%")
    
    # Display CPU frequency details (current, min, and max frequencies)
    print("CPU Frequency:")
    print(f"\tCurrent: {freq[0]:.2f}MHz")  # Current CPU frequency
    print(f"\tMin: {freq[1]:.2f}MHz")      # Minimum CPU frequency
    print(f"\tMax: {freq[2]:.2f}MHz")      # Maximum CPU frequency
    
    # Display CPU average load over different time periods (in percentages)
    print("CPU Average Load Percentage:")
    print(f"\tOver the last 1 min: {load_perc[0]:.2f}%")
    print(f"\tOver the last 5 min: {load_perc[1]:.2f}%")
    print(f"\tOver the last 15 min: {load_perc[2]:.2f}%")
    
    print("================================\n")
