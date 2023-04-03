import os
from multiprocessing import Process, Pipe

def sender(pipe):
    pipe.send(['spam'] + [42, 'ovos'])
    pipe.close()

def comunicador(pipe):
    pipe.send(dict(nome='joão', spam=42))
    resposta = pipe.recv()
    print('comunicador recebeu:', resposta)

if __name__== '__main__':
    (saidaPai, saidaFilho) = Pipe()
    Process(target=sender, args=(saidaFilho,)).start()
    print('pai recebeu', saidaPai.recv())
    saidaPai.close()

    (saidaPai, saidaFilho) = Pipe()
    filho = Process(target=comunicador, args=(saidaFilho,))
    filho.start()
    print('pai recebeu:' , saidaPai.recv())
    saidaPai.send({x * 2 for x in 'spam'})
    filho.join()

    print('saiu de pai')
