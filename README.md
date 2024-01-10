# GTFObins
The script will scan for SUID binaries on the system and check them against GTFOBins for potential vulnerabilities and privilege escalation techniques.

# GTFOBins Vulnerability Scanner

![GTFOBins Vulnerability Scanner]
![image](https://github.com/vinal-2/GTFObins/assets/97253630/4fd0d000-1c8c-4be6-ba9e-5d4ecbef8a40)

## Overview

The GTFOBins Vulnerability Scanner is a tool designed to identify potential vulnerabilities and privilege escalation techniques in SUID binaries on a Linux system. It leverages information from GTFOBins, a curated list of Unix binaries that can be exploited by an attacker to bypass local security restrictions.

## Features

- Scans the system for SUID binaries.
- Checks identified SUID binaries against GTFOBins for potential vulnerabilities.
- Displays potential privilege escalation techniques for vulnerable binaries.
- Provides a runtime progress indicator.
- Welcome screen with ASCII art.


## Dependencies
curl (Ensure it is installed on your system)

## License
This tool is licensed under the GPL-3.0 License - see the LICENSE file for details.

## Acknowledgments
GTFOBins (link-to-gtfobins-github) - A fantastic resource for binary exploitation techniques.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your enhancements.

## Issues and Support
For bug reports or feature requests, please open an issue on GitHub.

## Author
Vinal-2 - Author of GTFOBins Vulnerability Scanner

## Installation
Install the tool using pip:

```bash
pip install gtfobins-scan==1.0.0

Python:

python -m pip install gtfobins-scan==1.0.0

python -m pip install --upgrade pip


