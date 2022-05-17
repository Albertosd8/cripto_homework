import socket
import encrypt

HOST = "127.0.0.1"
PORT = 65432

def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            file_data = b"" 
            data_decrypted = b""
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file_data += encrypt.encrypt2(data) # Guardamos los datos recibidos para escribirlos en el archivo de servidor
                data_decrypted += encrypt.decrypt2(file_data) # Guardamos los datos recibidos para escribirlos en el archivo de servidor

    with open("file_r.txt", "wb") as file: 
        file.write(file_data)
    with open("file_d.txt", "wb") as file: 
        file.write(file_data)

if __name__ == "__main__":
    main()