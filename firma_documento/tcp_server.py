import socket
import encrypt
from nacl.signing import VerifyKey

HOST = "127.0.0.1"
PORT = 65432

def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        key_bytes = conn.recv(32)
        cliente_signeture = conn.recv(64)
        with conn, open("file_r.txt", "wb") as file: 
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                file.write(data)
                if not data:
                    break
                verifyKey = VerifyKey(key_bytes)
        with open("file_r.txt", "rb") as file:
            verifyKey.verify(file.read(), cliente_signeture)
        with open("file_d.txt", "wb") as file: # Creamos el archivo y escribimos en el
            data = encrypt.encrypt2(data)
            file.write(data)

if __name__ == "__main__":
    main()