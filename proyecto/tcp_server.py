import socket
from nacl.signing import VerifyKey
from abc import ABC
import base64
import nacl.secret
import nacl.utils

HOST = "127.0.0.1"
PORT = 65432


_key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

def random() -> bytes:
  return base64.b64encode(nacl.utils.random())

def encrypt2(message: bytes) -> bytes:
  box = nacl.secret.SecretBox(_key)
  encrypted = box.encrypt(message)
  return encrypted

def decrypt2(message: bytes) -> bytes:
  box = nacl.secret.SecretBox(_key)
  desencrypt = box.decrypt(message)
  return desencrypt

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
            data = encrypt2(data)
            file.write(data)

if __name__ == "__main__":
    main()