import subprocess
import re
import platform

def get_interface():
    try:
        if platform.system() == "Windows":
            output = subprocess.check_output("wmic nic where NetEnabled=true get NetConnectionID", shell=True).decode()
            interfaces = output.split('\n')[1:-1]
            return [iface.strip() for iface in interfaces if iface.strip()]
        elif platform.system() == "Linux":
            output = subprocess.check_output("ls /sys/class/net", shell=True).decode()
            interfaces = output.split('\n')[:-1]
            return interfaces
        else:
            print("Unsupported operating system.")
            return []
    except subprocess.CalledProcessError as e:
        print(f"Error listing interfaces: {e}")
        return []

def change_mac_address(interface, new_mac):
    try:
        if platform.system() == "Windows":
            subprocess.run(f"netsh interface set interface name='{interface}' admin=disable", shell=True, check=True)
            subprocess.run(f"netsh interface set interface name='{interface}' admin=enable", shell=True, check=True)
            print(f"MAC address for {interface} changed to {new_mac} (Please verify manually on Windows)")
        elif platform.system() == "Linux":
            subprocess.run(f"sudo ifconfig {interface} down", shell=True, check=True)
            subprocess.run(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True, check=True)
            subprocess.run(f"sudo ifconfig {interface} up", shell=True, check=True)
            print(f"MAC address for {interface} changed to {new_mac}")
    except subprocess.CalledProcessError as e:
        print(f"Error changing MAC address: {e}")

def validate_mac(mac):
    return bool(re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac))

def main():
    interfaces = get_interface()
    if not interfaces:
        return

    print("Available Network Interfaces:")
    for i, iface in enumerate(interfaces):
        print(f"{i}: {iface}")

    try:
        choice = int(input("Select the interface number: "))
        if choice < 0 or choice >= len(interfaces):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    new_mac = input("Enter new MAC address (format: XX:XX:XX:XX:XX:XX): ")
    if not validate_mac(new_mac):
        print("Invalid MAC address format.")
        return

    change_mac_address(interfaces[choice], new_mac)

if __name__ == "__main__":
    main()
