import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Enter server IP (e.g. 127.0.0.1): ")
    port = 8080
    client.connect((host, port))
    print("Connected to server")

    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")

    client.close()

if __name__ == "__main__":
    main()
