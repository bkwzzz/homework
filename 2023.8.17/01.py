from qytang_ping import qytang_ping
from qytang_ssh import ssh
import re
import pprint

def qytang_get_if(*ips, username='python', password='123'):
    device_if_dict = {}
    if_info_dict = {}
    for ip in ips:
        if qytang_ping(ip):
            if_info = ssh(ip, username=username, passwd=password).split('\n')
            for line in if_info:
                if re.findall(r'\d+.\d+.\d+.\d+', line):
                    if_name = re.findall(r'\w+\S\d', line)[0]
                    ip_add = re.findall(r'\d+.\d+.\d+.\d+', line)[0]
                    if_info_dict[if_name] = ip_add
                    device_if_dict[ip] = if_info_dict
        else:
            device_if_dict[ip] = {}
    return device_if_dict

if __name__ == '__main__':
    pprint.pprint(qytang_get_if('192.168.48.12', '192.168.48.16'))


