import psutil

# Get CPU information
cpu_info = {
    "Physical cores": psutil.cpu_count(logical=False),
    "Total cores": psutil.cpu_count(logical=True),
    "Max frequency": f"{psutil.cpu_freq().max:.2f}Mhz",
    "Min frequency": f"{psutil.cpu_freq().min:.2f}Mhz",
    "Current frequency": f"{psutil.cpu_freq().current:.2f}Mhz",
    "CPU usage": f"{psutil.cpu_percent()}%"
}

# Get memory information
memory_info = {
    "Total memory": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
    "Available memory": f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
    "Used memory": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB",
    "Memory usage": f"{psutil.virtual_memory().percent}%"
}

# Print CPU information
print("CPU Information:")
for key, value in cpu_info.items():
    print(f"{key}: {value}")

# Print memory information
print("\nMemory Information:")
for key, value in memory_info.items():
    print(f"{key}: {value}")