import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import sr1
from kamene.layers.inet import ICMP, IP, Raw

class QYTPING:
    def __init__(self, dstip):
        self.dstip = dstip
        self.len = 100
        self.srcip = ''

    def __str__(self):
        if self.srcip:
            return 'QYTPING => srcip: {}, dstip: {}, size: {}>'.format(self.srcip, self.dstip, self.len)
        else:
            return 'QYTPING => dstip: {}, size: {}>'.format(self.dstip, self.len)

    def one(self):
        ping_payload = self.len
        if self.srcip:
            ping_echo = IP(src=self.srcip, dst=self.dstip) / ICMP() / Raw(load=b"X" * ping_payload)
            ping_result = sr1(ping_echo, timeout=2, verbose=False)
        else:
            ping_echo = IP(dst=self.dstip) / ICMP() / Raw(load=b"X" * ping_payload)
            ping_result = sr1(ping_echo, timeout=2, verbose=False)
        if ping_result:
            print(self.dstip + '可达!')
        else:
            return None

    def ping(self):
        ping_payload = self.len
        if self.srcip:
            ping_echo = IP(src=self.srcip, dst=self.dstip) / ICMP() / Raw(load=b"X" * ping_payload)
        else:
            ping_echo = IP(dst=self.dstip) / ICMP() / Raw(load=b"X" * ping_payload)
        for n in range(5):
            ping_result = sr1(ping_echo, timeout=2, verbose=False)
            if ping_result:
                result = '!!!!!'
            else:
                result = '.....'
        print(result)

class NewPing(QYTPING):
    def __str__(self):
        if self.srcip:
            return '<NewPing => srcip: {}, dstip: {}, size: {}'.format(self.srcip, self.dstip, self.len)
        else:
            return '<NewPing => dstip: {}, size: {}'.format(self.dstip, self.len)

    def ping(self):
        ping_payload = self.len
        if self.srcip:
            ping_echo = IP(src=self.srcip, dst=self.dstip) / ICMP() / Raw(load=b"X" * ping_payload)
        else:
            ping_echo = IP(dst=self.dstip) / ICMP() / Raw(load=b"X" * ping_payload)
        for n in range(5):
            ping_result = sr1(ping_echo, timeout=2, verbose=False)
            if ping_result:
                result = '+++++'
            else:
                result = '?????'
        print(result)

if __name__ == '__main__':
    ping = QYTPING('192.168.28.2')
    total_len = 70

    def print_new(word, s='-'):
        print('{0}{1}{2}'.format(s * int((70 - len(word))/2), word, s * int((70 - len(word))/2)))
    print_new('print class')
    print(ping)
    print_new('ping one for sure reachable')
    ping.one()
    print_new('ping five')
    ping.ping()
    print_new('set payload length')
    ping.len = 200
    print(ping)
    ping.ping()
    print_new('set ping src ip address')
    ping.srcip = '192.168.28.130'
    print(ping)
    ping.ping()
    print_new('new class NewPing', '=')
    newping = NewPing('192.168.28.2')
    newping.len = 300
    print(newping)
    newping.ping()
