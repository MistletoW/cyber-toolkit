import subprocess

def run_nmap():
    target = input("Enter the target IP or Domain: ")
    scan_type = input("Enter scan type (e.g. -sS, -sV, -A): ")

    # 1. Input validation (before we even try anything)
    if not target.strip() or not scan_type.strip():
        print("Error: target and scan type cannot be empty.")
        return

    print("Running nmap...")

    # 2. Handle nmap not being installed / execution failure
    try:
        result = subprocess.run(
            ["nmap", scan_type, target],
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        print("Error: nmap not found. Is it installed and in your PATH?")
        return

    # 3. Handle the file write failing
    log_file = "nmap_scan_log.txt"
    try:
        with open(log_file, "w") as f:
            f.write(result.stdout)
        print(f"Results saved to {log_file}")
    except OSError as e:
        print(f"Error: couldn't write to file — {e}")

if __name__ == "__main__":
    run_nmap()