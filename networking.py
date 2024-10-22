import selectors
import socket


# The size of a bytes buffer containing an int.
integer_length = 64


class NetworkClient:

    def __init__(self, ip_address=None, port=None):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connection_established = False

        if ip_address is not None and port is not None:
            self.open_connection(ip_address, port)

    def open_connection(self, ip_address, port):
        self._socket.connect(ip_address, port)
        self._connection_established = True

    def send(self, data):
        """
        Send a message
        """
        if not isinstance(data, bytes):
            raise Exception("Sent data must be of type 'bytes'.")

        if self._connection_established:
            message_length = len(data)
            message_length_bytes = message_length.to_bytes(
                integer_length, "big")
            self._socket.sendall(message_length_bytes)
            self._socket.sendall(data)

    def receive(self):
        message_length_bytes = bytes()
        while len(message_length_bytes) < integer_length:
            message_length_bytes += self._socket.recv(
                integer_length - len(message_length_bytes))
        message_length = int.from_bytes(message_length_bytes)

        incoming_bytes = bytes()
        while len(incoming_bytes < message_length):
            incoming_bytes += self._socket.recv(
                message_length - len(incoming_bytes))
        return incoming_bytes


class NetworkServer:
    def __init__(self):
        self._socket
