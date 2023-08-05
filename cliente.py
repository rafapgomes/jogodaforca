import socket
import comunicacao
import forca

def inicializa_sockets():
    # Definir a porta e o endereço do servidor
    porta = 2000
    endereco_servidor = 'localhost'
    # Criar o socket do servidor e se conectar ao servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.connect((endereco_servidor, porta))
    apelido = input("Digite seu nome")
    prefixo = "cliente"
    servidor_socket.sendall(f"{prefixo}:{apelido}".encode())
    #peca ao servidor para te informar se voce é o servidor 1 ou o 2
    mensagem = comunicacao.recebe_mensagem(servidor_socket)[1]
    cliente_id = int(mensagem)
    print(f"servidor {cliente_id} conectado")
    return servidor_socket,cliente_id

def partida(servidor_socket,cliente_id):
    while True:
        mensagem = comunicacao.recebe_mensagem(servidor_socket)[1]
        print(mensagem)
        break
    while not chances == 0:
        letra  = input("Digite uma letra")
        servidor_socket.sendall(f"{cliente_id}:{letra}".encode())


    













inicializa_sockets()






