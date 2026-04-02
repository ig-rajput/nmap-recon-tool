import subprocess
import xml.etree.ElementTree as ET
import argparse
import json

# Simple local CVE database
CVE_DB = {
    "OpenSSH 6": [
        "CVE-2016-0777",
        "CVE-2015-5600"
    ],
    "Apache 2.4.6": [
        "CVE-2017-3169",
        "CVE-2017-15715"
    ]
}


def get_target():
    parser = argparse.ArgumentParser(description="Smart Network Recon Tool")
    parser.add_argument("target", help="Target IP or domain")
    return parser.parse_args().target


def run_nmap_scan(target):
    print(f"[+] Scanning target: {target}")

    command = [
        r"C:\Program Files (x86)\Nmap\nmap.exe",
        "-sT",
        "-sV",
        "-oX", "scan.xml",
        target
    ]

    subprocess.run(command)


def parse_nmap_xml(file):
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
    found = []
    full_text = f"{product} {version}"

    for key in CVE_DB:
        if key in full_text:
            found.extend(CVE_DB[key])

    return found


def save_report(results):
    with open("report.json", "w") as f:
        json.dump(results, f, indent=4)


def analyze_results(results):
    print("\n[+] Analysis Report:\n")

    risk_score = 0

    for r in results:
        port = r['port']
        service = r['service']
        product = r['product']
        version = r['version']

        full_service = f"{product} {version}".strip()

        print(f"[+] Port {port} → {service.upper()} ({full_service})")

        cves = check_cve(product, version)

        if cves:
            print("    ⚠️ CVEs Found:")
            for cve in cves:
                print(f"       - {cve} → HIGH")
            print("    🔥 Risk: HIGH")
            risk_score += 3
        else:
            print("    ✓ No known vulnerabilities")

        # Smart suggestions
        if service == "http":
            print("    → Suggestion: Run web vulnerability scan (Burp Suite / dirsearch)")
        elif service == "ssh":
            print("    → Suggestion: Check for brute-force or weak credentials")
        elif service == "smtp":
            print("    → Suggestion: Check for open relay")

    print(f"\n[!] Overall Risk Score: {risk_score}")


def main():
    target = get_target()

    run_nmap_scan(target)
    results = parse_nmap_xml("scan.xml")
    save_report(results)
    analyze_results(results)


if __name__ == "__main__":
    main()