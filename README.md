# 🔍 Smart Network Recon Tool

A Python-based network reconnaissance tool that automates scanning using Nmap and provides structured security analysis with service/version detection, CVE-based vulnerability mapping, and intelligent suggestions.

---

## 🚀 Overview

This tool automates network reconnaissance and transforms raw Nmap output into meaningful security insights.

Instead of just listing open ports, it:

* Identifies services and versions
* Maps known vulnerabilities (CVE)
* Provides risk-based analysis
* Suggests next security actions

---

## 🎯 Why This Project?

Most beginners can run Nmap but struggle to interpret results.

This tool bridges that gap by converting raw scan data into actionable insights, simulating how real security tools assist analysts.

---

## ⚙️ Features

* Automated Nmap scanning
* Service and version detection
* CVE-based vulnerability mapping
* Risk scoring system
* Smart security suggestions
* CLI-based execution
* JSON report generation

---

## 🛠️ Tech Stack

* Python
* Nmap
* XML Parsing
* JSON

---

## 🧠 How It Works

1. User provides target via CLI
2. Tool runs Nmap scan (`-sT`, `-sV`)
3. Output is saved as XML
4. XML is parsed to extract services
5. Versions are matched with CVEs
6. Risk analysis + suggestions are displayed
7. Results are saved in JSON format

---

## ▶️ Usage

### Run the tool:

```bash
python main.py scanme.nmap.org
```

---

## 📸 Output Preview

![Output](screenshot.png)

---

## 📌 Example Output

```
[+] Port 22 → SSH (OpenSSH 6.6.1)
    ⚠️ CVEs Found:
       - CVE-2016-0777 → HIGH
    🔥 Risk: HIGH


    → Suggestion: Check for brute-force or weak credentials

[+] Port 80 → HTTP (Apache 2.4.7)
    ✓ No known vulnerabilities
    → Suggestion: Run web vulnerability scan
```

---

## 📂 Generated Report

After execution, a JSON report is created:

```
report.json
```

This file contains structured scan results for further analysis or integration.

---

## 🔍 CVE Mapping

The tool uses a local CVE database to map service versions to known vulnerabilities.

This demonstrates how real-world vulnerability scanners correlate software versions with publicly known security issues.

---

## 📚 Learning Outcomes

* Understood network reconnaissance workflow
* Learned automation using Python
* Gained insight into vulnerability analysis
* Built a CLI-based security tool
* Improved structured output and reporting

---

## ⚠️ Limitations

* Uses a static CVE database
* No real-time vulnerability lookup
* Not a full vulnerability scanner

---

## 🔮 Future Improvements

* Integrate real-time CVE APIs (NVD)
* Add severity classification system
* Automate follow-up scans
* Build GUI interface

---

## ⚠️ Disclaimer

This tool is for educational purposes only.
Do not scan systems without proper authorization.

---

## 👨‍💻 Author

**Sraban Kumar Singh**
B.Tech CSE | Cybersecurity Enthusiast

GitHub: https://github.com/ig-rajput
