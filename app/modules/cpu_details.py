# This module shows the CPU % usage, its frequency and load.

import psutil


perc = psutil.cpu_percent() * 100
freq = psutil.cpu_freq()
load_perc = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]

def run():
    print("========== CPU DETAILS ==========")
    print(f"CPU Percentage: {perc:.2f}%")
    print("CPU Frequency:")
    print(f"\tCurrent: {freq[0]:.2f}")
    print(f"\tMin: {freq[1]:.2f}")
    print(f"\tMax: {freq[2]:.2f}")
    print("CPU Average Load Percentage:")
    print(f"\tOver the last 1 min: {load_perc[0]:.2f}")
    print(f"\tOver the last 5 min: {load_perc[1]:.2f}")
    print(f"\tOver the last 15 min: {load_perc[2]:.2f}")
    print("================================\n")