# BOFfuzzer
Buffer Overflow Fuzzer 

# 🎯 Fuzzer for THM Brainpan 1

### **Description**
This fuzzer script is designed to help security enthusiasts test buffer overflow vulnerabilities in vulnerable services. Inspired by the TryHackMe Brainpan 1 room, the script dynamically sends increasing payload sizes to a specified target until the service crashes, identifying the exact crash point. 

## Please note that the Fuzzer may not work with all kind of buffer.

---

## 🚀 Features
- 📍 User Input for Target IP and Port
- 🔄 Dynamic Payload Generation
- 🛑 Identifies Crash Point with Payload Size

---

## 📂 How to Use

1. **Clone the Repository**
   ```bash
   https://github.com/ox1d3x3/BOFfuzzer.git
   cd BOFfuzzer
   ```

2. **Run the Script**
   ```bash
   python3 fuzzer.py
   ```

3. **Follow the Prompts**
   - Enter the target IP address.
   - Enter the target port.
   - Sit back and let the fuzzer do its magic! 🚀

4. **Example**
   ```
![image](https://github.com/user-attachments/assets/d8b90c4c-66da-4355-bdae-0993c7cfd069)

   ```

---

## 📋 Requirements
- Python 3.x
- A vulnerable service to test against (e.g., Brainpan 1)

---

## 🛠️ Configuration
The script dynamically asks for the target IP and port. Ensure the target service is up and running before starting the fuzzer.

---

## ⚠️ Disclaimer
This script is for educational purposes only. Always have permission before testing systems for vulnerabilities. The author is not responsible for misuse.

---

## 🖼️ Preview
```
![image](https://github.com/user-attachments/assets/e688f20e-b0e3-4d4d-a7a8-21ae47461352)

```

## Disclaimer

This program is provided "as-is" and without any warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability or fitness for a particular purpose. The author of this program is not liable for any direct, indirect, incidental, special, or consequential damages arising out of the use, misuse, or inability to use this software.

By using this program, you acknowledge and agree that you are solely responsible for any damage or loss that may occur as a result of its use, including but not limited to data loss, system failure, or any other kind of harm to your hardware, software, or personal well-being. You agree to hold the author harmless for any consequences, whether foreseeable or unforeseeable.

This program is intended solely for Capture The Flag (CTF) and educational purposes. It is your responsibility to ensure that you comply with all applicable laws and regulations when using this software. Any illegal or unauthorized use of this program, including but not limited to activities that involve hacking, unauthorized access, or any form of criminal activity, is strictly prohibited. The author is not responsible for any unlawful or harmful activities arising from the use of this software.

By using this program, you agree to assume full responsibility for your actions and comply with all applicable laws and regulations in your jurisdiction.




