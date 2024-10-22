#!/usr/bin/env python3

import socket

import numpy as np

macbook = '192.168.86.91'
nerd = '192.168.86.51'
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

num_numbers = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("connecting....")
    s.connect((nerd, PORT))
    print("sending...")

    numbytes = 64
    message = num_numbers.to_bytes(64, "big")

    s.sendall(message)
    print("receiving...")
    response_size_bytes = bytes()
    while len(response_size_bytes) < 64:
        response_size_bytes += s.recv(64 - len(response_size_bytes))
    response_size = int.from_bytes(response_size_bytes, "big")n

    response_bytes = bytes()
    while len(response_bytes) < response_size:

    data = s.recv(response_size_bytes)

print('Received', data.decode())
