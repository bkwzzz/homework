import re
str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
protocol_pattern = r'[UDPTCP]{3}'
protocol = re.match(protocol_pattern, str1).group()   #TCP

server_pattern = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}'
server = re.findall(server_pattern, str1)[0]      #172.16.1.101:443
localserver = re.findall(server_pattern, str1)[1]

idle_pattern = r'\d{1,2}:\d{1,2}:\d{1,2}'
idle = re.search(idle_pattern, str1).group()
idle_h = re.findall(r'\d{1,2}', idle)[0]
idle_min = re.findall(r'\d{1,2}', idle)[1]
idle_sec = re.findall(r'\d{1,2}', idle)[2]

bytes_pattern = r'\d+'
bytes = re.findall(bytes_pattern, str1)[-1]

flags_pattern = r'[A-Z]+'
flags = re.findall(flags_pattern, str1)[-1]

line1 = '{:<19}: {}'.format('protocol', protocol)
line2 = '{:<19}: {}'.format('server', server)
line3 = '{:<19}: {}'.format('localserver', localserver)
line4 = '{:<19}: {:<2}小时 {:<2}分钟 {:<2}秒'.format('idle', idle_h, idle_min, idle_sec)
line5 = '{:<19}: {}'.format('bytes', bytes)
line6 = '{:<19}: {}'.format('flags', flags)

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)












