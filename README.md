# Memory Forensics Lab – Insider Threat Detection

A Python script that automates common memory forensics tasks using Volatility 3.

## Features

- List running processes from a memory dump.
- Scan for network connections and sockets.
- Extract loaded DLLs and modules for each process.
- Search memory for a specific keyword.

## Requirements

- Python 3
- [Volatility 3](https://github.com/volatilityfoundation/volatility3)
- A Windows memory dump image (e.g., from a `.vmem` or `.img` file)

## Usage

1.  Place your memory dump in the project root and rename it to `memory.img`.
2.  Update the `PROFILE` variable in the script with the correct Volatility profile for your memory image.
3.  Run the script:
    ```bash
    python memory_forensics.py
    ```
4.  Follow the on-screen menu to choose an analysis option.

## Important Note

This repository does **not** include the `memory.img` file due to its large size and potential sensitivity. You must provide your own memory image.
