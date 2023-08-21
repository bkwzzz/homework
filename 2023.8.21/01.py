import paramiko
import time

def ssh(ip, username, passwd, port=22, cmd_list=[], enable='', wait_time=2, verbose=True):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username=username, password=passwd, timeout=2, compress=True)
    chan = ssh.invoke_shell()
    time.sleep(1)
    x = chan.recv(65535).decode()
    if x[-1] == '>':
        chan.send('enable\n')
        chan.send(enable + '\n')
        chan.send('terminal length 0\n'.encode())
        chan.send('conf t\n')
        for cmd in cmd_list:
            chan.send(cmd.encode())
            chan.send(b'\n')
            time.sleep(wait_time)
        if verbose:
            output = chan.recv(65535).decode()
            print(output)
    else:
        chan.send('terminal length 0\n'.encode())
        chan.send('conf t\n')
        for cmd in cmd_list:
            chan.send(cmd.encode())
            chan.send(b'\n')
            time.sleep(wait_time)
        if verbose:
            output = chan.recv(65535).decode()
            print(output)

if __name__ == '__main__':
    ssh(ip='192.168.48.11', username='python', passwd='123', port=22,
              cmd_list=['do show ver', 'router ospf 1', 'network 0.0.0.0 0.0.0.0 area 0'], enable='123')

