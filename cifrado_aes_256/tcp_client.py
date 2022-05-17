import socket

HOST = "127.0.0.1"
PORT = 65432


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        with open("file_s.txt", "rb") as file: 
            for line in file.readlines(): 
                s.sendall(line) 


if __name__ == "__main__":
    main() # Codigo del cliente