import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 1235
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "modify"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    connected = True

    # Receive access granted message
    access_msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER] {access_msg}")

    while connected:
        msg = input("Type modify to read,write or execute or search 'GET_FILE (type ur file name)' to request a file> ").lower()

        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        elif msg.startswith("GET_FILE "):
            file_contents = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] File contents:\n{file_contents}")
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")


def file_type(type):
    match type:
        case 'read':
            f = open("read.txt", "r")
            print(f.read())
        case 'write':
            f = open("read.txt", "a")
            a = input("What do u want to add? :")
            f.write(a)
            f.close()

            f = open("read.txt", "r")
            print(f.read())
        case 'execute':
            print("Execute..")


if __name__ == "__main__":
    main()
    type = input("Choose read, write or execute: ").lower()
    print(file_type(type))
