class Network:
    def __init__(self):
        self.subnets = {}
        self.vlans = {}

    def create_vlan(self, vlan_id, name):
        self.vlans[vlan_id] = {'name': name, 'subnets': []}
        print(f"VLAN {vlan_id} created with name '{name}'.")

    def add_subnet(self, vlan_id, subnet):
        if vlan_id in self.vlans:
            self.vlans[vlan_id]['subnets'].append(subnet)
            self.subnets[subnet] = vlan_id
            print(f"Subnet {subnet} added to VLAN {vlan_id}.")
        else:
            print(f"VLAN {vlan_id} does not exist.")

    def troubleshoot(self, ip):
        for subnet, vlan in self.subnets.items():
            if ip in subnet:
                return f"IP {ip} is in VLAN {vlan}."
        return "IP not found in any VLAN."


# Example usage:
if __name__ == "__main__":
    network = Network()
    network.create_vlan(10, "Sales")
    network.add_subnet(10, "192.168.1.0/24")
    print(network.troubleshoot("192.168.1.10"))
