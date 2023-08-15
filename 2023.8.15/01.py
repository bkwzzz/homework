import socket
import time

host = '192.168.28.130'
port = 80

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 设置连接超时时间为1秒
        sock.connect((host, port))
        sock.close()
        print(f"HTTP（TCP/80）服务已经被打开")
        break
    except (socket.timeout, ConnectionRefusedError):
        print(f"等待一秒重新开始监控！")
        time.sleep(1)
