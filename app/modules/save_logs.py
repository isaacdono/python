import os
import csv
import time
import psutil

def run():

    # Define the path to the 'logs' directory inside the 'app' directory
    log_directory = os.path.join(os.path.dirname(__file__), 'logs')

    # Ensure the 'logs' directory exists
    os.makedirs(log_directory, exist_ok=True)

    # Path to the log file inside 'app/logs/'
    log_file_path = os.path.join(log_directory, 'system_metrics.csv')

    # Open the CSV file in append mode
    with open(log_file_path, mode='a', newline='') as file:
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
