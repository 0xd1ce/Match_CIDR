import ipaddress

def check_ip_in_cidr(ip, cidr_list):
    ip_obj = ipaddress.ip_address(ip)
    for cidr in cidr_list:
        network = ipaddress.ip_network(cidr, false)
        if ip_obj in network:
            return cidr
    return None

def read_file_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def main():
    cidr_list = read_file_lines("cidr_ranges.txt")
    ip_list = read_file_lines("ip_addresses.txt")

    for ip in ip_list:
        matching_cidr = check_ip_in_cidr(ip, cidr_list)
        if matching_cidr:
            print(f"IP {ip} is within the CIDR range {matching_cidr}.")
        else:
            print(f"IP {ip} is not within any of the provided CIDR ranges.")

if __name__ == "__main__":
    main()
