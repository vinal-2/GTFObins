#!/usr/bin/env python3
import os
import subprocess
import sys
import threading
import argparse
import yaml

# Define the welcome message
WELCOME_MSG = "GTFObins Scan"

# Define the colors
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"

# Define the ASCII art
ART = r"""
    /\_/\ 
   ( o   o )
    > ^ <
"""

# Print the welcome message and ASCII art
print(f"{GREEN}{WELCOME_MSG}\n{ART}")

suid_binaries_map = {}


def clone_gtfo():
    # Create a new directory for the repository and navigate into it
    os.makedirs("GTFOBins", exist_ok=True)
    os.chdir("GTFOBins")

    # Initialize an empty Git repository and add your remote repository
    subprocess.run(["git", "init"])
    subprocess.run(
        [
            "git",
            "remote",
            "add",
            "-f",
            "origin",
            "https://github.com/GTFOBins/GTFOBins.github.io.git",
        ]
    )

    # Enable the sparse checkout feature
    subprocess.run(["git", "config", "core.sparseCheckout", "true"])

    # Define the files or folders you want to check out by adding them to `.git/info/sparse-checkout`
    with open(".git/info/sparse-checkout", "w") as f:
        f.write("_gtfobins/")

    # Pull the data from the remote repository
    subprocess.run(["git", "pull", "origin", "master"])

    # Change back to the original directory
    os.chdir("..")


def highlight(msg):
    print(f"\033[1;32m{msg}\033[0m")


def check_binary(binary):
    # Check if the binary exists in the system's PATH
    binary_path = subprocess.run(
        ["which", binary], capture_output=True, text=True
    ).stdout.strip()

    if binary_path:
        return True
    else:
        return False


def check_gtfo(binary):
    # specify the path to the directory containing the .md files
    directory_path = "GTFOBins/_gtfobins/"

    # specify the path to the .md file for the binary
    file_path = os.path.join(directory_path, f"{binary}.md")

    try:
        # open the .md file
        with open(file_path, "r") as file:
            file_content = file.read()

        # parse the YAML content
        documents = yaml.safe_load_all(file_content)

        for doc in documents:
            if doc is not None and "functions" in doc:
                functions = doc["functions"]

                # print the potential privilege escalation techniques for the binary
                for function, details in functions.items():
                    highlight(
                        f"Potential privilege escalation techniques for {binary} using {function}:"
                    )
                    for detail in details:
                        print(detail["code"])
                    print("----------------------------------------")

    except FileNotFoundError:
        print(f"No .md file found for {binary}.")


def main():
    parser = argparse.ArgumentParser(
        description="Scan for SUID binaries and check against GTFOBins."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose mode"
    )
    parser.add_argument("-o", "--output", type=str, help="Specify output file")
    args = parser.parse_args()

    # Clone the _gtfobins directory from the GTFOBins/GTFOBins.github.io repository
    clone_gtfo()

    # specify the path to the directory containing the .md files
    directory_path = "GTFOBins/_gtfobins/"

    # Get all .md files in the specified directory
    files = [f[:-3] for f in os.listdir(directory_path) if f.endswith(".md")]

    # Redirect stdout to the output file if specified
    if args.output:
        sys.stdout = open(args.output, "w")

    print("## Binary Identified\n")
    for binary in files:
        if check_binary(binary):
            print(f"The binary {binary} exists in the system's PATH.")
            check_gtfo(binary)

    print("\n## Binaries not on local system\n")
    for binary in files:
        if not check_binary(binary):
            print(f"The binary {binary} does not exist in the system's PATH.")


if __name__ == "__main__":
    main()

    # Restore standard output
    sys.stdout = sys.__stdout__
