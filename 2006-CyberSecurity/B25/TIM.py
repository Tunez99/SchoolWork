
malicious_ips = {
    "185.220.101.1",
    "45.9.148.23",
    "103.45.67.89"
}

known_cves = {
    "CVE-2024-1234",
    "CVE-2023-9876"
}

def check_threat(ip, cve):
    if ip in malicious_ips:
        print(f"[ALERT] Malicious IP detected: {ip}")
    else:
        print(f"[OK] IP clean: {ip}")

    if cve in known_cves:
        print(f"[ALERT] Known vulnerable CVE detected: {cve}")
    else:
        print(f"[OK] CVE not flagged: {cve}")

check_threat("185.220.101.1", "CVE-2024-1234")
print("---")
check_threat("8.8.8.8", "CVE-2022-1111")