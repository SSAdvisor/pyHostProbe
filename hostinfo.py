import platform
import os
import socket
import psutil
from tabulate import tabulate

# Function to get the local IP address
def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return str(e)

# Function to get the external IP address
# This function uses a system command that might not work in all environments
def get_external_ip():
    try:
        external_ip = os.popen('curl -s http://whatismyip.akamai.com/').read()
        return external_ip
    except Exception as e:
        return str(e)

# Collecting extensive information
info = {
    "Operating System": platform.system(),
    "OS Release": platform.release(),
    "Platform": platform.platform(),
    "Architecture": platform.architecture()[0],
    "Processor": platform.processor(),
    'Machine': platform.machine(),
    'Node': platform.node(),
    "CPU Cores": psutil.cpu_count(logical=False),
    "CPU Threads": psutil.cpu_count(logical=True),
    "Total RAM": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
    "Hostname": socket.gethostname(),
    "Local IP": get_local_ip(),
    "External IP": get_external_ip(),
    # Add more system details as needed
    "Python Version": platform.python_version(),
}

# Preparing for tabulate
data = [[key, value] for key, value in info.items()]

# Print in 2-column format
print(tabulate(data, headers=["Information", "Value"], tablefmt="grid"))
