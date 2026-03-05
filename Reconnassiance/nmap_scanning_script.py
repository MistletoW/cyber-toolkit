import subprocess

def run_nmap():
    target = input("Enter the target IP or Domain:")
    scan_type = input("Enter the scan type (for example, -sS, -sV, -A): ")

    print("Running nmap...")
    
    result = subprocess.run(
        ["nmap", scan_type, target],
        capture_output= True,
        text = True
    )

    log_file = "nmap_scan_log.txt"
    print(f"Logging scan results to {log_file}...")

    with(log_file, "w") as f:
        f.write(result.stdout)

    print(f"Results saved to {log_file}")

if __name__ == "__main__":
    run_nmap()