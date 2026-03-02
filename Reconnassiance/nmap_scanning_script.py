import subprocess

def run_nmap():
    target = input("Enter the target IP or Domain:")
    scan_type = input("Enter the scan type (for example, -sS, -sV, -A): ")

    print("Running nmap...")
    subprocess.call(["nmap", scan_type, target])

    log_file = "nmap_scan_log.txt"
    print(f"Logging scan results to {log_file}...")
    subprocess.call(["nmap", scan_type, target], stdout=open(log_file, "w"))

if __name__ == "__main__":
    run_nmap()