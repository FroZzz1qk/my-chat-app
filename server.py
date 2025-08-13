import socket
import threading

def handle_client(client_socket, addr):
    print(f"Connected to {addr}")
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
                break
            print(f"Received from {addr}: {msg}")
            # Отправляем эхо обратно клиенту
            client_socket.send(f"Server received: {msg}".encode('utf-8'))
        except ConnectionResetError:
            break
    print(f"Connection with {addr} closed")
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # чтобы избежать ошибки адреса занятости
    server.bind(('0.0.0.0', 10000))
    server.listen(5)
    print("Server listening on port 10000")

    while True:
        client_sock, address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_sock, address))
        client_thread.start()

if __name__ == "__main__":
    main()
