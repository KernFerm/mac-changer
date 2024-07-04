# Network Interface Utility

This utility provides a simple Python script for listing network interfaces and changing the MAC address on Windows and Linux systems.

## Features

- **List Network Interfaces**: Easily list all network interfaces available on your system.
- **Change MAC Address**: Change the MAC address of a specified network interface.

# MUST RUN CMD.EXE IN ADMIN MODE

## Requirements

- Python 3.x
- Works on Windows and Linux

## Usage

### Listing Network Interfaces

To list all network interfaces on your system, simply run:

```bash
python main.py --list
```

### Changing MAC Address

To change the MAC address of a specific interface, use:

```bash
python main.py --interface "Your Interface Name" --mac "New MAC Address"
```

Replace `"Your Interface Name"` with the name of your network interface and `"New MAC Address"` with the new MAC address you wish to set.

## Supported Operating Systems

- Windows
- Linux

## Disclaimer

This tool is for educational purposes only. Use it at your own risk. The author is not responsible for any misuse or damage caused by this program. `IF YOUR ISP COMES AFTER YOU THAT IS ON YOU, I AM NOT HELD RESPSONIBLE`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
