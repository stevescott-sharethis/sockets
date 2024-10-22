import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

sock = socket.socket()


macbook = '192.168.86.91'
# external =  '136.24.104.254'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()


sock.bind(nerd)
