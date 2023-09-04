import ipaddress
import os.path
import sys
import argparse
​
def check_ip_in_cidr(ip, cidr_list):
    ip_obj = ipaddress.ip_address(ip)
    for cidr in cidr_list:
        network = ipaddress.ip_network(cidr, False)
        if ip_obj in network:
            return cidr
    return None
​
def read_file_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]
​
def main():
    cidr_list = read_file_lines(cidr_file)
    ip_list = read_file_lines(ip_file)
​
    for ip in ip_list:
        matching_cidr = check_ip_in_cidr(ip, cidr_list)
        if matching_cidr:
            print(f"Remove: IP {ip} is within {matching_cidr}.")
        else:
            print(f"Keep: IP {ip} is not within any CIDR ranges.")
​
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cidr", help="List of CIDR ranges", required=True)
    parser.add_argument("--ip", help="List of IP addresses", required=True)
    args = parser.parse_args()
​
    cidr_file = args.cidr
    ip_file = args.ip
​
    if not os.path.exists(cidr_file):
        print("{} not found".format(cidr_file))
        sys.exit(0)
    if not os.path.exists(ip_file):
        print("{} not found".format(ip_file))
        sys.exit(0)
​
    main()
