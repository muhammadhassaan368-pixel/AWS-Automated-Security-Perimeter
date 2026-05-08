# AWS-Automated-Security-Perimeter
Automating enterprise cloud infrastructure with Python/Boto3 and performing defensive validation via Nmap.

# AWS Automated Security Perimeter & Audit 🛡️

## 🎯 Project Vision
Applying a meticulous auditing mindset to Cloud Security. This project demonstrates my ability to use **Infrastructure as Code (IaC)** to automate a secure perimeter and perform a defensive audit to ensure compliance.

## 🏗️ Phase 1: The Build (Automation)
I developed a Python-based automation engine using the **Boto3 SDK** to provision a custom AWS network. This bypasses manual configuration errors and ensures a repeatable, hardened environment.

* **VPC:** Isolated 10.0.0.0/16 network.
* **Firewall:** Custom Security Group enforcing "Least Privilege" (Allowing only SSH and ICMP).

### **Network Topology Audit**
<img width="836" height="351" alt="8" src="https://github.com/user-attachments/assets/910f0201-cc22-4bc1-865f-401bde8512ac" />



## 🛡️ Phase 2: The Audit (Security Validation)
Building the wall is only half the job. To verify the security posture, I deployed a target instance and performed a reconnaissance scan from an external Kali Linux attack node.

* **Port 22 (SSH):** OPEN (Verified for authorized maintenance).
* **Port 80 (HTTP):** **FILTERED** (Verified: Unauthorized web traffic was successfully dropped by the firewall).

### **Nmap Validation Results**
<img width="405" height="92" alt="1" src="https://github.com/user-attachments/assets/6f6253b4-cbb1-45b0-811c-eac49bc7eb38" />


## 💻 Operational Environment
The lab was engineered and tested within a virtualized Kali Linux environment.
<img width="1600" height="1200" alt="9" src="https://github.com/user-attachments/assets/7ed417c0-ea2c-4dc7-9c9d-1e7f21ebbbdc" />

