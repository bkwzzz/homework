import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    reply = sr1(ping_pkt, timeout=2, verbose=False)

    if reply:
        return f'通'
    else:
        return

if __name__ == '__main__':
    host = '192.168.48.16'
    ping_result = qytang_ping(host)
    print(host + ' ' + ping_result + '!')

# from kamene.all import *
# import logging
#
# logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


# def ping(ip):
#     ping_pkt = IP(dst=ip) / ICMP()
#     ping_result = sr1(ping_pkt, timeout=15, verbose=False)
#     if ping_result:
#         print('主机' + ip + '可达!!!')
#     else:
#         print('主机' + ip + '不可达!!!')
#
#
# host = '192.168.28.2'
# ping(host)

