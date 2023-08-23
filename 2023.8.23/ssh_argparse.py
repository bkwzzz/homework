import paramiko
from argparse import ArgumentParser
def ssh(ip, username, passwd, port=22, cmd='sh ip int b'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username=username, password=passwd, timeout=2, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

def argparse_ssh(ipaddr, username, password, cmd):
    result = ssh(ipaddr, username, password, cmd=cmd)
    print(result)

if __name__ == '__main__':
    usage = 'usage: python3 ssh_argparse.py -i ipaddr -u username -p password -c cmd'
    parser = ArgumentParser(usage=usage)
    parser.add_argument('-i', '--ipaddr', dest='ipaddr', help='SSH Server', type=str)
    parser.add_argument('-u', '--username', dest='username', help='SSH Username', default='root', type=str)
    parser.add_argument('-p', '--password', dest='password', help='SSH Password', default='123', type=str)
    parser.add_argument('-c', '--command', dest='command', help='Shell Command', default='ls', type=str)
    args = parser.parse_args()
    argparse_ssh(args.ipaddr, args.username, args.password, args.command)

