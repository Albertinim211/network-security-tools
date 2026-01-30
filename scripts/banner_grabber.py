import socket

# --- Project: Service Fingerprinter (Banner Grabber) ---
# Purpose: Identifies software versions on open ports.
# Skills: Protocol Analysis, Vulnerability Assessment, Python Socket Programming.

def get_banner(ip, port):
    try:
        # Create a socket and set a timeout for efficiency
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))

        # Some services (like HTTP) need a request before they send a banner
        if port == 80:
            s.send(b'GET / HTTP/1.1\r\nHost: target\r\n\r\n')
        
        # Receive up to 1024 bytes of the server's response
        banner = s.recv(1024)
        return banner.decode(errors='ignore').strip()
    except Exception as e:
        return f"No banner detected: {str(e)}"
    finally:
        s.close()

def main():
    target_ip = "127.0.0.1" # Change to your target IP
    ports = [21, 22, 25, 80, 443] # Common service ports

    print(f"--- Initiating Service Fingerprinting on {target_ip} ---")
    for port in ports:
        banner = get_banner(target_ip, port)
        if "No banner detected" not in banner:
            print(f"[+] Port {port}: {banner}")
        else:
            print(f"[-] Port {port}: No signature found.")

if __name__ == "__main__":
    main()
