import socket
from nacl.signing import SigningKey

HOST = "127.0.0.1"
PORT = 65432


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        with open("file_s.txt", "rb") as file: 
            read = file.read()
            signing_key = SigningKey.generate()# Generate a new random signing key 
            signed = signing_key.sign(read)# Sign a message with the signing key
            verify_key = signing_key.verify_key # Obtain the verify key for a given signing key
            verify_key_bytes = verify_key.encode()# Serialize the verify key to send it to a third party
            
            s.send(verify_key_bytes)
            s.send(signed.signature)
            s.send(read)


if __name__ == "__main__":
    main() # Codigo del cliente