import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n " \
           "TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}

for conn in asa_conn.split('\n'):
    re_result = re.search(r'([A-Z]+\s)([a-zA-Z]+\s)(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,5})(\s[A-Za-z]+\s)'
                         r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,5})(,\s\w+\s\d+:\d+:\d+,\s\w+\s)(\d+)(,\s\w+\s)'
                         r'(\w+)', conn)

    asa_dict[(re_result.group(3), re_result.group(4), re_result.group(6), re_result.group(7))] = (re_result.group(9),
                                                                                                  re_result.group(11))
print('打印分析后的字典! \n')
print(asa_dict)

src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'
format_str1 = '{:^8}:{:^15}|{:^8}:{:^15}|{:^10}:{:^15}|{:^10}:{:^15}'
format_str2 = '{:^8}:{:^15}|{:^8}:{:^15}'

print('\n格式化打印输出\n')

for key, value in asa_dict.items():
    print(format_str1.format(src, key[0], src_ip, key[1], dst, key[2], dst_ip, key[3]))
    print(format_str2.format(bytes_name, value[0], flags, value[1]))
    print('==================================================================================================')