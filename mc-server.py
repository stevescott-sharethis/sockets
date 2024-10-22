import selectors
import socket

macbook = '192.168.86.91'
nerd = '192.168.86.51'
nerd = '192.168.86.165'

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


sel = selectors.DefaultSelector()
# ...
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((nerd, PORT))
lsock.listen()
print('listening on', (nerd, PORT))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)
