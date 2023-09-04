# Match_CIDR
A simple Python script that notates if a list of IPs, fall within a list of CIDR ranges.

## Usage
python3 match.py --cidr .\cidr_ranges.txt --ip .\ip_addresses.txt

Remove: IP 192.168.1.10 is within 192.168.1.0/24.
Keep: IP 8.8.8.8 is not within any CIDR ranges.
