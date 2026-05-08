# AWS-Automated-Security-Perimeter
Automating enterprise cloud infrastructure with Python/Boto3 and performing defensive validation via Nmap.

# AWS Automated Security Perimeter & Audit 🛡️

## 🎯 Project Vision
Transitioning from a career in Finance and Accounting, I apply a meticulous auditing mindset to Cloud Security. This project demonstrates my ability to use **Infrastructure as Code (IaC)** to automate a secure perimeter and perform a defensive audit to ensure compliance.

## 🏗️ Phase 1: The Build (Automation)
I developed a Python-based automation engine using the **Boto3 SDK** to provision a custom AWS network. This bypasses manual configuration errors and ensures a repeatable, hardened environment.

* **VPC:** Isolated 10.0.0.0/16 network.
* **Firewall:** Custom Security Group enforcing "Least Privilege" (Allowing only SSH and ICMP).

### **Network Topology Audit**
*(DRAG AND DROP Image 8.png HERE)*

## 🛡️ Phase 2: The Audit (Security Validation)
Building the wall is only half the job. To verify the security posture, I deployed a target instance and performed a reconnaissance scan from an external Kali Linux attack node.

* **Port 22 (SSH):** OPEN (Verified for authorized maintenance).
* **Port 80 (HTTP):** **FILTERED** (Verified: Unauthorized web traffic was successfully dropped by the firewall).

### **Nmap Validation Results**
*(DRAG AND DROP Image 1.png HERE)*

## 💻 Operational Environment
The lab was engineered and tested within a virtualized Kali Linux environment.
*(DRAG AND DROP Image 9.jpg HERE)*
