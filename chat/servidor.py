from socket import *

meuHost = 'localHost'
minhaPort = 50007
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((meuHost, minhaPort))
sockobj.listen(5)

while True:
    conexão, endereço = sockobj.accept()
    print('server conectado por', endereço)

    while True:
        data = conexão.recv(1024)
        print("Ele", data.decode())

        resposta = input("Você: ")

        conexão.send(resposta.encode())
    conexão.close
