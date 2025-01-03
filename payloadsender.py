import socket
import sys
import time
from tqdm import tqdm

def display_banner():
    banner = r"""
                ___    __        
     ____  _  _<  /___/ /__      
    / __ \| |/_/ / __  / _ \     
   / /_/ />  </ / /_/ /  __/     
   \____/_/|_/_/\__,_/\___/      
    """
    print(banner)
    print("Author  : Ox1d3x3")
    print("Version : 0.4")
    print("Disclaimer: This fuzzer is made based on THM Brainpan 1 room.\n")

# Function to send the pattern to a target
def send_pattern(ip, port, pattern):
    try:
        print(f"[+] Sending pattern to {ip}:{port}")
        for _ in tqdm(range(100), desc="Sending payload", unit="%"):
            time.sleep(0.01)  # Simulating progress
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send((pattern + "\r\n").encode())
        s.close()
        print("[+] Payload sent successfully")
    except Exception as e:
        print(f"[!] Error sending Payload: {e}")

# Main function
def main():
    try:
        display_banner()
        print("\n[!] Welcome to the Payload Sender")
        print("[!] Generate payload using msf-pattern_create. Example: msf-pattern_create -l <crash bytes>")

        has_pattern = input("Do you already have a pattern? (Y/N): ").strip().lower()
        if has_pattern in ["y", "yes"]:
            pattern = input("Enter your existing pattern: ").strip()
        else:
            print("[!] Exiting. Please generate a pattern first using the instructions above.")
            sys.exit()

        user_input = input("\nDo you want to send this pattern to a target? (Y/N): ").strip().lower()
        if user_input in ["y", "yes"]:
            target_ip = input("Enter target IP address: ").strip()
            target_port = int(input("Enter target port: ").strip())
            send_pattern(target_ip, target_port, pattern)
        else:
            print("[!] Exiting without sending the payload.")
    except ValueError:
        print("[!] Invalid input. Please enter valid numbers for bytes and port.")
        sys.exit()

if __name__ == "__main__":
    main()
