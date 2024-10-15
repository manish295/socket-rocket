
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        try:
            data = s.recv(1024)
        except ConnectionError:
            print('SERVER CONNECTION LOST')
            break
        print(f"Received {data}")
    

