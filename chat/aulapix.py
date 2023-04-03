import socket
import ssl
from Crypto.PublicKey import RSA

# Dados da transferência
valor = 500.00
chave_pix = '6f952cfc-22f3-4621-bc72-d96bf2c92628'
banco_destino = 'c6bank.com.br'

# Carregando chave pública RSA
with open('chave_publica_rsa.pem', 'rb') as f:
    chave_publica = RSA.import_key(f.read())

# Conexão com o servidor do banco A
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers="HIGH")

banco_a_ip = 'bancointer.com.br'
banco_a_porta = 80
sock.connect((banco_a_ip, banco_a_porta))

# Envio dos dados via protocolo iso 20022
mensagem = f'TRANSFER {valor:.2f} PIX {chave_pix} PARA BANCO {banco_destino}'
mensagem_cifrada = chave_publica.encrypt(mensagem.encode(), 0)[0]

sock.send(mensagem_cifrada)

# Encerrando conexão com o servidor do banco A
sock.shutdown(socket.SHUT_RDWR)
sock.close()

# Conexão com o servidor do banco B
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers="HIGH")
sock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1_2, ciphers="HIGH")

banco_b_ip = '162.159.152.26'
banco_b_porta = 80
sock.connect((banco_b_ip, banco_b_porta))

# Recebimento dos dados via protocolo iso 20022
dados_cifrados = sock.recv(1024)
dados = chave_publica.decrypt(dados_cifrados).decode()

print('Dados recebidos: ', dados)

# Encerrando conexão com o servidor do banco B
sock.shutdown(socket.SHUT_RDWR)
sock.close()
