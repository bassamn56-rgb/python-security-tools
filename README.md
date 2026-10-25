# python-security-tools

A small collection of Python tools I'm building to practice networking and security concepts.

## Port Checker (`port_checker.py`)

A simple TCP port scanner I wrote while relearning Python.

**What it does:**
- Asks the user which ports to scan (e.g. `80,443,22`)
- Tries to connect to each port using Python's `socket` library
- Prints only the open ports
- Saves the results to `results.txt` so they can be reviewed later without re-running the scan

**What I learned:**
-The first version printed every closed port, which was noisy, so I changed it to show only open ports.

**How to run it:**
  python port_checker.py just type this in the terminal

**Notes:**
- The scanner currently targets `127.0.0.1` (my own machine).
- It uses TCP connections only. UDP scanning would need a different approach and is a possible future improvement.

**Disclaimer:** This tool is for learning purposes. Only scan your own machine or systems you have explicit permission to test.
