import subprocess
import re
import platform

def get_interface():
    if platform.system() == "Windows":
        # List all network interfaces on Windows
        output = subprocess.check_output("wmic nic get NetConnectionID", shell=True).decode()
        interfaces = output.split('\n')[1:-1]
        return [iface.strip() for iface in interfaces if iface.strip()]
    elif platform.system() == "Linux":
        # List all network interfaces on Linux
        output = subprocess.check_output("ls /sys/class/net", shell=True).decode()
        interfaces = output.split('\n')[:-1]
        return interfaces
    else:
        print("Unsupported operating system.")
        return []

def change_mac_address(interface, new_mac):
    if platform.system() == "Windows":
        command = f"wmic path win32_networkadapter where NetConnectionID='{interface}' call disable"
        subprocess.run(command, shell=True)
        command = f"wmic path win32_networkadapter where NetConnectionID='{interface}' call setmacaddress '{new_mac}'"
        subprocess.run(command, shell=True)
        command = f"wmic path win32_networkadapter where NetConnectionID='{interface}' call enable"
        subprocess.run(command, shell=True)
    elif platform.system() == "Linux":
        subprocess.run(f"sudo ifconfig {interface} down", shell=True)
        subprocess.run(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
        subprocess.run(f"sudo ifconfig {interface} up", shell=True)

def validate_mac(mac):
    if re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac):
        return True
    else:
        return False

def main():
    interfaces = get_interface()
    if not interfaces:
        return

    print("Available Network Interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i}: {iface}")

    choice = int(input("Select the interface number: "))
    if choice < 0 or choice >= len(interfaces):
        print("Invalid choice.")
        return

    new_mac = input("Enter new MAC address (format: XX:XX:XX:XX:XX:XX): ")
    if not validate_mac(new_mac):
        print("Invalid MAC address format.")
        return

    change_mac_address(interfaces[choice], new_mac)
    print(f"MAC address for {interfaces[choice]} changed to {new_mac}")

if __name__ == "__main__":
    main()
