# echo-client.py
import random
import primo
import socket

# função para gerar número primo
#p = primo.gerar_primo()
#q = primo.gerar_primo()

# números primos conhecido pelo server e client, chaves públicass
p = 97
q = 67

a = random.randrange(1, 100)  # chave privada
x = pow(q, a) % p  # x = q^a mod p
HOST = "127.0.0.1"  # Endereço de interface de loopback padrão (localhost)
PORT = 65432  # Porta usada pelo server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str(x).encode('utf8'))
    # if p != q:
    #s.send((str(p) + " ").encode('utf8'))
    #s.send((str(q) + " ").encode('utf8'))
    data = s.recv(1024)
    strings = data.decode('utf8')

print(f"Recebido {strings!r}\n")

# computando chave simétrica
y = int(strings)
ka = pow(y, a) % p
print(f"Chave privada {ka}")
