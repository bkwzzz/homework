import paramiko
import re
def ssh(ip, username, passwd, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username=username, password=passwd, timeout=2, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    route_n = ssh('192.168.28.129', 'root', '123', cmd='route -n')
    lines = route_n.split('\n')
    for line in lines:
        if re.findall(r'[U][G]', line):
            gateway = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', line)[1]
            # 带有'UG'的这一行的第二个IP肯定是网关
            print('网关为:\n' + gateway)