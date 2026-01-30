# 🛡️ Network Security Tools
**Custom Python utilities for Network Discovery and Vulnerability Auditing.**

## 📌 Project Overview
Project **ScanLine** is a custom-built network reconnaissance tool designed to identify active services and potential entry points on a target host. This project demonstrates the intersection of **Software Development** and **Network Security**.

### Key Features
* **Full TCP Range Scanning:** Supports scanning of all 65,535 ports.
* **Service Identification:** Targets common ports (SSH, HTTP, FTP, RDP) to map the attack surface.
* **Robust Error Handling:** Manages DNS resolution failures, keyboard interrupts, and connection timeouts.
* **Logging:** Timestamps every scan for audit compliance and incident reporting.

---

## 🚀 Technical Deep Dive: Port Scanner
The core utility, `port_scanner.py`, uses the `socket` module to interface with the network stack directly.

### Performance & Optimization
* **Timeout Management:** Implemented a 1.0s timeout per port to balance speed with accuracy in high-latency environments.
* **Modular Design:** Built with clean functions to allow for future multi-threading implementation.



---

## ⚙️ Usage & Installation

### **Prerequisites**
* Python 3.x installed.
* Target IP or Hostname (Use only on systems you own or have permission to test!).

### **Running the Scanner**
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/yourusername/network-security-tools.git](https://github.com/yourusername/network-security-tools.git)
   cd network-security-tools/scripts

   🛡️ Ethical Use Warning
This tool is for educational and authorized security auditing purposes only. Unauthorized scanning of networks you do not own is illegal and unethical. Always obtain written consent before performing any security assessment.

Service Fingerprinting (Banner Grabbing)
While port scanning identifies "open doors," this tool performs Banner Grabbing to identify the software versioning behind those doors. This is critical for:

Vulnerability Mapping: Comparing service versions against CVE (Common Vulnerabilities and Exposures) databases.

Compliance Auditing: Ensuring only approved versions of SSH or Web Servers are deployed in the infrastructure.
