import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 1235
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
NEXT = "next"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    connected = True
    while connected:
        msg = input("Type next to choose your next move ")

        client.send(msg.encode(FORMAT))

        if msg.lower() == NEXT.lower():
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
            f = open("write.txt", "a")
            f.write("Hey Getuar, there is new text in the file")
            f.close()

            f = open("write.txt", "r")
            print(f.read())
        case 'execute':
            print("Execute..")


if __name__ == "__main__":
    main()
    type = input("Choose read, write or execute: ")
    print(file_type(type))