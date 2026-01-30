# Network Auditing Fundamentals

## How this Scanner Works
This tool operates at the **Transport Layer (Layer 4)** of the OSI Model. It utilizes the Python `socket` library to perform **TCP Connect Scans**.

### The TCP Three-Way Handshake
To determine if a port is open, the scanner attempts a full connection:
1. **SYN**: Our scanner sends a Synchronize packet to the target port.
2. **SYN-ACK**: If the port is open, the target responds with a Synchronize-Acknowledgment.
3. **ACK**: Our scanner sends an Acknowledgment to complete the connection (and then immediately closes it).



### Error Handling & Timeouts
- **Socket Timeout**: Set to 1 second to prevent the script from hanging on "Filtered" ports (ports protected by a firewall that drops packets).
- **Socket Error (111)**: Connection Refused (Port is closed).
- **Socket Error (0)**: Success (Port is open).
