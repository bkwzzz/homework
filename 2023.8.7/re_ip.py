str1 = 'Port-channel1.189     192.168.189.254   Yes   CONFIG   up'
import re
ip_pattern = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
ip = re.search(ip_pattern, str1).group()
print('=================================================')
line1 = '{:<8}: {}'.format('接口', 'Port-channel1.189')
line2 = '{:<8}: {}'.format('IP地址', ip)
line3 = '{:<8}: {}'.format('状态', 'up')
print(line1)
print(line2)
print(line3)
print('=================================================')
print(line1)
print(line2)
print(line3)
