import random
import socket

# números primos conhecido pelo server e client
p = 97
q = 67

b = random.randrange(1, 100)
y = pow(q, b) % p  # y = q^b mod p
HOST = "127.0.0.1"  # Endereço de interface de loopback padrão (localhost)
PORT = 65432  # Porta de escuta

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # O método .bind() é usado para associar o soquete a uma interface de rede e número de porta específicos
    s.bind((HOST, PORT))
    s.listen()  # .listen() permite que um servidor aceite conexões
    # .accept usada por um servidor para aceitar uma solicitação de conexão de um cliente.
    conn, addr = s.accept()
    with conn:

        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)  # dados recebidos do client
            strings = data.decode('utf8')  # decodificando utf-8
            print(f"Recebido {strings!r}\n")

            if not data:
                break

            # enviando dados encodados (utf-8) para client
            conn.sendall(str(y).encode('utf-8'))

            # computando chave simétrica
            x = int(strings)
            kb = pow(x, b) % p
            print(f"Chave privada {kb}")
