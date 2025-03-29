import netifaces

# Get all available network interfaces
interfaces = netifaces.interfaces()

for interface in interfaces:
    print(f"Interface: {interface}")
    addresses = netifaces.ifaddresses(interface)

    for family, addrs in addresses.items():
        for addr in addrs:
            print(f"  Address Family: {family}")
            print(f"  Address: {addr.get('addr')}")
            print(f"  Netmask: {addr.get('netmask')}")
            print(f"  Broadcast: {addr.get('broadcast')}")
            print()
