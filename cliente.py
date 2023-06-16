import socket

HOST = 'localhost' 
PORT = 3306 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

while True:

    message = input("Ingrese un mensaje para enviar al servidor (o 'salir' para finalizar): ")
    if message == 'salir':
        break
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print(f"Respuesta del servidor: {data.decode()}")

client_socket.close()
