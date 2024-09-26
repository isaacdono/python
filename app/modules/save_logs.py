import os
import csv
import time
import psutil

def run():
    # Open the CSV file in append mode
    with open('./logs/system_metrics.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the header row if the file is empty
        file.seek(0, 2)  # Move to the end of the file
        if file.tell() == 0:  # Check if the file is empty
            writer.writerow(['Timestamp', 'CPU (%)', 'Memory (%)', 'Disk (%)'])

        # Infinite loop to keep logging metrics
        while True:
            # Collect system metrics
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent

            # Get current timestamp
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

            # Write metrics to the CSV file
            writer.writerow([timestamp, cpu, memory, disk])

            # Print to console for monitoring
            print(f'{timestamp} - CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%')

            # Sleep before the next logging interval (adjust as needed)
            time.sleep(10)
