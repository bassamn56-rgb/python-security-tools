import socket


target = "127.0.0.1"  # this means your own computer
open_ports = []
user_input = input("Enter ports separated by commas (example: 80,443,22): ")
ports = [int(p) for p in user_input.split(",")]

print(f"Scanning {target}...")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)
    s.close()
    
with open("results.txt", "w") as f:
    f.write(f"Open ports on {target}: {open_ports}\n")

print("Done. Results saved to results.txt")