import re
str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
vlan_id_pattern =r'\d{1,4}'
vlan_id = re.match(vlan_id_pattern, str1).group()    #166

mac_pattern = r'[0-9a-f]{4}.[0-9a-f]{4}.[0-9a-f]{4}'
mac = re.search(mac_pattern, str1).group()          #54a2.74f7.0326

type_pattern = r'[A-Z]+'
type = re.search(type_pattern, str1).group()        #DYNAMIC

interface_pattern = r'[A-Z]{1}[a-z]{1}\d{1,2}/\d{1,2}/\d{1,2}'
interface = re.search(interface_pattern, str1).group()    #Gi1/0/11

line1 = '{:<11}: {}'.format('VLAN ID', vlan_id)
line2 = '{:<11}: {}'.format('MAC', mac)
line3 = '{:<11}: {}'.format('TYPE', type)
line4 = '{:<11}: {}'.format('Interface', interface)
print(line1)
print(line2)
print(line3)
print(line4)
