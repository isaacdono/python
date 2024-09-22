import psutil


metrics = psutil.virtual_memory()
swap = psutil.swap_memory()

def run():
    print("======== MEMORY DETAILS ========")
    print(f"RAM Usage: {metrics[2]}%")
    print(f"Total RAM: {metrics[0] / 10**9:.0f}GB")
    print(f"Swap Usage: {swap[3]}%")
    print(f"Total Swap: {swap[0] / 10**9:.0f}GB")
    print("================================\n")