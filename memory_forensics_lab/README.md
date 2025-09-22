
# Memory Forensics Lab – Insider Threat Detection

This project demonstrates **memory forensics** using Python and **Volatility 3**.  
It is designed to analyze RAM images to detect potential insider threats.

## Features
- List running processes
- Scan network connections
- Extract loaded modules (DLLs)
- Search memory for specific keywords
- Save output to files for forensic analysis

## Requirements
- Python 3.x
- Volatility 3 installed
- RAM image file (e.g., `memory.img`)

## Usage
1. Place your memory image in the project folder or update the `MEMORY_IMAGE` path in `memory_analysis.py`.
2. Run the script:
```bash
python memory_analysis.py
```
3. Choose an analysis option:
   - List processes
   - Scan network connections
   - Extract loaded modules
   - Search memory for keywords
   - Run all analyses

4. Results will be saved in the `forensics_output/` folder.

## Example
```
=== Memory Forensics Lab – Insider Threat Detection ===
[1] List all processes
[2] Scan network connections
[3] Extract loaded modules
[4] Search memory for keyword
[5] Run all analyses

Choose an option (1-5): 1
[+] Running: vol.py -f memory.img --profile=Win10x64_22H2 windows.pslist
[+] Output saved to forensics_output/windows.pslist.txt
```
