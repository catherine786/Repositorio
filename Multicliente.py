import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Conexión establecida desde {client_address[0]}:{client_address[1]}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Recibido desde {client_address[0]}:{client_address[1]}: {data.decode()}")
        print(f"Conexión cerrada desde {client_address[0]}:{client_address[1]}")
        client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"El servidor esta escuchando en {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


HOST = 'localhost' 
PORT = 12345 

start_server(HOST, PORT)
