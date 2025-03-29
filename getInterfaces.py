import psutil

# Get network interface details
interfaces = psutil.net_if_addrs()

f = open(file="./interfaces", mode="w", encoding="utf-8")

# Print interface names
for interface, addresses in interfaces.items():
    print(f"Interface: {interface}", file=f)
    for addr in addresses:
        print(f"  Address Family: {addr.family.name}", file=f)
        print(f"  Address: {addr.address}", file=f)
        print(f"  Netmask: {addr.netmask}", file=f)
        print(f"  Broadcast: {addr.broadcast}", file=f)
        print(file=f)
