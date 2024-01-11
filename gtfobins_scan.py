#!/usr/bin/env python3
import os
import requests
import subprocess
import sys
import threading
import argparse

# Define the welcome message
WELCOME_MSG = "GTFObins Scan"

# Define the colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"

# Define the ASCII art
ART = r"""
    /\_/\
   ( o   o )
    > ^ <
"""

# Print the welcome message and ASCII art
print(f"{GREEN}{WELCOME_MSG}\n{ART}")

# Configuration
GTFOBINS_URL = "https://gtfobins.github.io/gtfobins"
GTFOBINS_EXEC_DIR = "_gtfobins"
GTFOBINS_EXEC_EXT = ".md"

suid_binaries_map = {}


def highlight(msg):
    print(f"\033[1;32m{msg}\033[0m")


def check_gtfo(binary):
    response = requests.get(f"{GTFOBINS_URL}/{binary}/")
    gtfo_results = (
        response.text.split("<pre")[1].split("</pre>")[0] if response.ok else None
    )

    if gtfo_results:
        highlight(f"Potential privilege escalation techniques for {binary}:")
        print(gtfo_results)
        print("----------------------------------------")


def runtime_progress(pid):
    delay = 0.1
    spin = ["-", "/", "|", "\\"]
    sys.stdout.write("Scanning GTFOBins... ")

    while os.path.exists(f"/proc/{pid}"):
        for char in spin:
            sys.stdout.write("\b" + char)
            sys.stdout.flush()
            subprocess.call(["sleep", str(delay)])

    print("\bDone!")


def main():
    parser = argparse.ArgumentParser(
        description="Scan for SUID binaries and check against GTFOBins."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose mode"
    )
    args = parser.parse_args()

    try:
        suid_binaries = subprocess.check_output(
            [
                "find",
                "/",
                "-type",
                "f",
                "-perm",
                "-4000",
                "!",
                "-path",
                "/proc*",
                "-prune",
                "!",
                "-path",
                "/run/user*",
                "-prune",
            ],
            stderr=subprocess.PIPE,
            universal_newlines=True,
        ).strip()
    except subprocess.CalledProcessError as e:
        suid_binaries = ""
        print(f"Error occurred while finding SUID binaries: {e.stderr}")

    suid_binaries = suid_binaries.strip().split("\n")

    if not suid_binaries:
        print("No SUID binaries found.")
        sys.exit(1)

    if args.verbose:
        print("----------------------------------------")
        highlight("SUID Binaries:")
        print("\n".join(suid_binaries))
        print("----------------------------------------")

    # Populate dictionary for easy lookup
    for binary in suid_binaries:
        suid_binaries_map[binary] = 1

    # Check if curl is available
    try:
        subprocess.check_output(["curl", "--version"])
    except subprocess.CalledProcessError:
        print("Error: curl command not found. Please install curl.")
        sys.exit(1)

    # Display runtime progress
    threading.Thread(target=runtime_progress, args=(os.getpid(),)).start()

    # Check SUID binaries against GTFOBins
    for binary in suid_binaries_map:
        check_gtfo(binary)


if __name__ == "__main__":
    main()
