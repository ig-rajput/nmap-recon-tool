import subprocess
import xml.etree.ElementTree as ET

# Simple local CVE database (demo purpose)
CVE_DB = {
    "OpenSSH 6": [
        "CVE-2016-0777 (Information Leak)",
        "CVE-2015-5600 (Authentication Bypass)"
    ],
    "Apache 2.4.6": [
        "CVE-2017-3169 (Authentication Bypass)",
        "CVE-2017-15715 (Input Validation Issue)"
    ]
}


def run_nmap_scan(target):
    # Run Nmap and save output as XML
    print(f"[+] Scanning target: {target}")
    
    command = [
        r"C:\Program Files (x86)\Nmap\nmap.exe",
        "-sT",   # works without admin
        "-sV",   # service + version detection
        "-oX", "scan.xml",
        target
    ]

    subprocess.run(command)


def parse_nmap_xml(file):
    # Parse XML output from Nmap
    tree = ET.parse(file)
    root = tree.getroot()

    results = []

    for host in root.findall('host'):
        for port in host.findall(".//port"):
            state = port.find('state').get('state')

            if state != "open":
                continue

            service = port.find('service')

            results.append({
                "port": port.get('portid'),
                "service": service.get('name') if service is not None else "unknown",
                "product": service.get('product') if service is not None else "",
                "version": service.get('version') if service is not None else ""
            })

    return results


def check_cve(product, version):
    # Match service with known CVEs
    found = []

    full_text = f"{product} {version}"

    for key in CVE_DB:
        if key in full_text:
            found.extend(CVE_DB[key])

    return found


def analyze_results(results):
    print("\n[+] Analysis Report:\n")

    risk_score = 0

    for r in results:
        port = r['port']
        service = r['service']
        product = r['product']
        version = r['version']

        full_service = f"{product} {version}".strip()

        print(f"[+] Port {port} → {service} ({full_service})")

        # CVE lookup
        cves = check_cve(product, version)

        if cves:
            print("    ⚠️ Known Vulnerabilities:")
            for cve in cves:
                print(f"       - {cve}")
            risk_score += 3
        else:
            print("    ✓ No known CVEs found")

        # Extra basic logic
        if service == "ssh":
            print("    → Check for brute-force / weak credentials")
        elif service == "http":
            print("    → Test for XSS, SQLi, directory issues")
        elif service == "smtp":
            print("    → Check for open relay")

    print(f"\n[!] Overall Risk Score: {risk_score}")


def main():
    target = input("Enter target IP or domain: ")

    run_nmap_scan(target)
    results = parse_nmap_xml("scan.xml")
    analyze_results(results)


if __name__ == "__main__":
    main()