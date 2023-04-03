from socket import *

def main():
    host = "localhost"
    port = 5000

    server = socket(AF_INET, SOCK_DGRAM)

    print("servidor iniciado")

    while True:
        data, endereço = server.recvfrom(1024)

        print("mensagem recebida de:", str(endereço))
        print("recebemos do cliente:", str(data))

        resposta = "Eco=>" + str(data)
        server.sendto(data, endereço)

    server.close()

if __name__ == '__main__':
    main()
