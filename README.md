# GTFO binaries
The script will scan for SUID binaries on the system and check them against GTFOBins for potential vulnerabilities and privilege escalation techniques.

## What are GTFO Binaries
Gtfobins has made a significant impact on the cybersecurity landscape by providing a comprehensive collection of “gtfo” binaries and associated techniques. Accoring to [DotComMagazine]( https://dotcommagazine.com/2023/07/gtfobins-top-ten-things-you-need-to-know/) Gtfobins are a collection of Unix-binaries. These binaries can be leveraged to escalate privileges, bypass security restrictions, and gain unauthorized access to systems.

Thus empowers security professionals to test the security of their systems and identify potential vulnerabilities. It serves as a valuable resource for penetration testing, vulnerability assessments, and red teaming exercises. Additionally, system administrators can leverage Gtfobins to better understand the risks associated with certain binaries and implement appropriate security measures to protect their systems. This tool will help you do just that.

# GTFOBins Vulnerability Scanner
![Walkthrough](https://github.com/vinal-2/GTFObins/assets/97253630/c5f2848f-c8b6-469e-ae98-38d2ba6bfccc)

## Overview

The GTFOBins Vulnerability Scanner is a tool designed to identify potential vulnerabilities and privilege escalation techniques in SUID binaries on a Linux system. It leverages information from GTFOBins, a curated list of Unix binaries that can be exploited by an attacker to bypass local security restrictions. This tool will help you identify the low hanging fruits in your system which you can then place security controls over.

## Features

- Scans the system for SUID binaries.
- Checks identified SUID binaries against GTFOBins for potential vulnerabilities.
- Displays potential privilege escalation techniques for vulnerable binaries such as e.g. SUDO, SUID, SHELL, FILE-READ, FILE-WRITE, FILE-DOWNLOAD, REVERSE SHELL, FILE-UPLOAD, LIMITED SUID, LIBRARY LOAD.
- Provides information on binaries that are not present in the local system.
- Welcome screen with ASCII art.

## Dependencies
- curl (Ensure it is installed on your system)
- latest version of python
- gitpython is used for Git operations
- pyyaml is used for parsing YAML content.
- subprocess: os, threading, argparse, and sys are built-in Python libraries

## Options
-v, --verbose: Enable verbose mode.
-o, --output <file>: such as result.txt

## License
This tool is licensed under the GPL-3.0 License - see the LICENSE file for details.

## Acknowledgments and Special Thanks:
GTFOBins ([gtfobins.github.io](https://github.com/GTFOBins/GTFOBins.github.io/tree/master)) - A fantastic resource for binary exploitation techniques.
Credits to this repository for providing the main source for ALL the GTFO Binaries inforamtion.

# Contributing
Contributions are welcome! Please fork the repository and create a pull request with your enhancements.

## Issues and Support
For bug reports or feature requests, please open an issue on GitHub.

## Author
Vinal-2 - Author of GTFOBins Vulnerability Scanner

## Installation

Clone repository:
```bash
git clone https://github.com/vinal-2/GTFObins
```
Install the tool using pip:
```bash
pip install gtfobins-scan
```
Python:
```
python -m pip install --upgrade pip
```
## Example use:

## Bash:

Identify SUID binaries and check for privilege escalation techniques:
```bash
gtfobins-scan
```

Enable verbose mode:
```bash
gtfobins-scan -v
```

Specify an output file for the scan results:
```bash
gtfobins-scan -o output.txt
```

Enable verbose mode and specify an output file:
```bash
gtfobins-scan -v -o output.txt
```
## Python:
Identify SUID binaries and check for privilege escalation techniques:
```python
python gtfobins_scan.py
```
```python
python3 gtfobins_scan.py
```
Enable verbose mode and specify an output file:
```python
python gtfobins_scan.py -v
```
```python
python3 gtfobins_scan.py -v
```
Specify an output file for the scan results:
```python
python gtfobins_scan.py -o output.txt
```
```python
python3 gtfobins_scan.py -o output.txt
```
Enable verbose mode and specify an output file:
```python
python gtfobins_scan.py -v -o output.txt
```
```python
python3 gtfobins_scan.py -v -o output.txt
```
