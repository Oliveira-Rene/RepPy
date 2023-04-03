from socket import *

def main():
    host = "localhost"
    port = 5000

    server = (host, port)

    conexão = socket(AF_INET, SOCK_DGRAM)
    conexão.bind((host, port))

    msg = input("->")
    while msg != 's':
        conexão.sendto(msg.encode(), server)

        data, endereço = conexão.recvfrom(1024)

        print("recebida ->", str(data))

        msg = input("->")

    conexão.close()

if __name__ == '__main__':
    main()
