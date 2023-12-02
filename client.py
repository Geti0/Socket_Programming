import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    connected = True

    while connected:
        msg = input("Type for something you want to search> ")

        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
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
    type = input("Choose read, write or execute: ")
    print(file_type(type))