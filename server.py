import socket
import threading
import os

IP = socket.gethostbyname(socket.gethostname())
PORT = 1235
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
ACCESS_GRANTED_MSG = "!ACCESS_GRANTED"
DIRECTORY_PATH = "C:/Users/Getuar/Documents/GitHub/Socket_Programming"  # Change this to the desired directory path

def send_file_contents(conn, filename):
    file_path = os.path.join(DIRECTORY_PATH, filename)
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            conn.send(contents.encode(FORMAT))
    except FileNotFoundError:
        conn.send("File not found.".encode(FORMAT))

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    # Send access granted message
    conn.send(ACCESS_GRANTED_MSG.encode(FORMAT))

    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            print(f"[{addr}] {msg}")

            # Check if the message is a request for file contents
            if msg.startswith("!GET_FILE "):
                filename = msg[len("!GET_FILE "):]
                send_file_contents(conn, filename)

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(4)
    print(f"[LISTENING] Server is listening on {IP}  :   {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

if __name__ == "__main__":
    main()
