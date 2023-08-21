from qytang_ssh import ssh
import re
import hashlib
import time

def qytang_get_config(ip, username, password):
    try:
        full_config = ssh(ip, username, password)
        config = re.search(r'^hostname\s.*?^end', full_config, re.DOTALL | re.MULTILINE).group()
        config_md5 = hashlib.md5(config.encode()).hexdigest()
        return config_md5
    except Exception:
        return

def qytang_check_diff(ip, username, password):
    previous_md5 = qytang_get_config(ip, username, password)
    while True:
        current_md5 = qytang_get_config(ip, username, password)
        print(current_md5)
        time.sleep(5)
        if current_md5 != previous_md5:
            print('MD5 value changed')
            break

if __name__ == '__main__':
    qytang_check_diff('192.168.48.11', 'python', '123')