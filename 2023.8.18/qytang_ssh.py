import paramiko
import re
def ssh(ip, username, passwd, port=22, cmd='sh run'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username=username, password=passwd, timeout=2, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    a = (ssh('192.168.48.11', 'python', '123'))
    b = re.search(r'^hostname\s.*?^end', a, re.DOTALL | re.MULTILINE).group()
    print(b)