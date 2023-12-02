


import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 1235
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    connected = True

    # Receive access granted message
    access_msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER] {access_msg}")

    while connected:
        msg = input("Type for something you want to search or enter '!GET_FILE filename' to request a file> ")

        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        elif msg.startswith("!GET_FILE "):
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
            f.write("Now the file has more content!")
            f.close()

            f = open("read.txt", "r")
            print(f.read())
        case 'execute':
            print("Execute..")


if __name__ == "__main__":
    main()
    type = input("Choose read, write or execute: ").lower()
    print(file_type(type))
