import sys
import re
import ipaddress
from collections import Counter

def count_private_ips(filename):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    counter = Counter()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            matches = re.findall(ip_pattern, line)
            for ip in matches:
                try:
                    ip_obj = ipaddress.IPv4Address(ip)
                    if ip_obj.is_private:  ### Əgər public IP istəsən "if ip_obj.is_global:"
                        counter[ip] += 1
                except ipaddress.AddressValueError:
                    pass

    for ip, count in sorted(counter.items(), key=lambda x: x[1], reverse=True):
        print(f"{count} {ip}")

if __name__ == "__main__":
    count_private_ips(sys.argv[1])