import socket
import sys
from datetime import datetime

# --- Project: Project ScanLine - Network Auditor ---
# Purpose: Identifies open ports and potential entry points on a target host.
# Skills: Python, Networking (TCP/IP), Security Auditing.

def scan_target(target, start_port, end_port):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scanning started at: {str(datetime.now())}")
    print("-" * 50)

    try:
        # Loop through the range of ports provided
        for port in range(start_port, end_port + 1):
            # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) # Wait 1 second for a response
            
            # Returns 0 if connection is successful
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

# Usage
if __name__ == "__main__":
    # In a real scenario, you'd use input() or sys.argv
    # Example: Scanning a local web server (80-443)
    target_ip = "127.0.0.1" 
    scan_target(target_ip, 20, 1024)
