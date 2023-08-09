import os
import re

ifconfig_result = os.popen('ifconfig ' + 'ens160').read()

ipv4_add = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', ifconfig_result)[0]
netmask = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', ifconfig_result)[1]
broadcast = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', ifconfig_result)[2]
mac_addr = re.findall(r'[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}', ifconfig_result)[0]

format_string = '{:<10}:{}'
print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_addr', mac_addr))

ipv4_gw = str(ipv4_add).split('.')[0] + '.' + str(ipv4_add).split('.')[1] + '.' + str(ipv4_add).split('.')[2] + '.' + '2'

print('\n我们假设网关地址为第二位为2，因此网关为:' + ipv4_gw + '\n')

ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.search(r'ttl', ping_result)

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')

