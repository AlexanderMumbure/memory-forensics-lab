
import os
import subprocess

MEMORY_IMAGE = "memory.img"
PROFILE = "Win10x64_22H2"
VOL_COMMAND = "vol.py"
OUTPUT_DIR = "forensics_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_volatility(plugin, extra_args=""):
    output_file = os.path.join(OUTPUT_DIR, f"{plugin}.txt")
    command = f"{VOL_COMMAND} -f {MEMORY_IMAGE} --profile={PROFILE} {plugin} {extra_args}"
    print(f"[+] Running: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        with open(output_file, "w") as f:
            f.write(result.stdout)
        print(f"[+] Output saved to {output_file}\n")
    except Exception as e:
        print(f"[-] Error running {plugin}: {e}")

def list_processes():
    run_volatility("windows.pslist")

def dump_network_connections():
    run_volatility("windows.netscan")

def extract_loaded_modules():
    run_volatility("windows.dlllist")

def search_strings(keyword):
    run_volatility("windows.strings", f"--string={keyword}")

def main():
    print("=== Memory Forensics Lab – Insider Threat Detection ===\n")
    print("[1] List all processes")
    print("[2] Scan network connections")
    print("[3] Extract loaded modules")
    print("[4] Search memory for keyword")
    print("[5] Run all analyses\n")
    choice = input("Choose an option (1-5): ").strip()
    if choice == "1":
        list_processes()
    elif choice == "2":
        dump_network_connections()
    elif choice == "3":
        extract_loaded_modules()
    elif choice == "4":
        keyword = input("Enter keyword to search: ").strip()
        search_strings(keyword)
    elif choice == "5":
        list_processes()
        dump_network_connections()
        extract_loaded_modules()
    else:
        print("[-] Invalid choice.")

if __name__ == "__main__":
    main()
