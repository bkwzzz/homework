import os
import re
route_n_result = os.popen('route -n').read()

lines = route_n_result.split('\n')
for line in lines:
    if re.findall(r'[U][G]', line):
        gateway = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', line)[1]
        # 带有'UG'的这一行的第二个IP肯定是网关
        print('网关为:' + gateway)