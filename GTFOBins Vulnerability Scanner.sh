#!/bin/bash

# Define the welcome message
WELCOME_MSG="GTFObins Scan"

# Define the colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'

# Define the ASCII art
ART=$(cat << "EOF"
    /\_/\
   ( o   o )
    > ^ <
EOF
)

# Print the welcome message and ASCII art
echo -e "${GREEN}$WELCOME_MSG\n${ART}"

# Define the command prompt
PS1="${CYAN}\u@\h ${YELLOW}\w ${PURPLE}\$ ${WHITE}"

# Configuration
GTFOBINS_URL="https://gtfobins.github.io/gtfobins"
GTFOBINS_EXEC_DIR="_gtfobins"
GTFOBINS_EXEC_EXT=".md"

declare -A suid_binaries_map

# Functions

highlight() {
  echo -e "\e[1;32m$1\e[0m"
}

check_gtfo() {
  local binary=$1
  local gtfo_results=$(curl -s "$GTFOBINS_URL/$binary/" | grep -o '<pre.*</pre>')

  if [ -n "$gtfo_results" ]; then
    highlight "Potential privilege escalation techniques for $binary:"
    echo "$gtfo_results"
    echo "----------------------------------------"
  fi
}

runtime_progress() {
  local pid=$1
  local delay=0.1
  local spin=("-" "/" "|" "\\")

  echo -n "Scanning GTFOBins... "

  while [ -d "/proc/$pid" ]; do
    for i in "${spin[@]}"; do
      echo -n -e "\b$i"
      sleep $delay
    done
  done

  echo -e "\bDone!"
}

# Main script

echo "Scanning for SUID binaries..."
suid_binaries=$(find / -type f -perm -4000 2>/dev/null)

if [ -z "$suid_binaries" ]; then
  echo "No SUID binaries found."
  exit 1
fi

echo "----------------------------------------"
highlight "SUID Binaries:"
echo "$suid_binaries"
echo "----------------------------------------"

# Populate associative array for easy lookup
for binary in $suid_binaries; do
  suid_binaries_map["$binary"]=1
done

# Check if curl is available
if ! command -v curl &>/dev/null; then
  echo "Error: curl command not found. Please install curl."
  exit 1
fi

# Display runtime progress
(sleep 1; echo "----------------------------------------") & runtime_progress $!

# Check SUID binaries against GTFOBins
for binary in "${!suid_binaries_map[@]}"; do
  check_gtfo "$binary"
done
