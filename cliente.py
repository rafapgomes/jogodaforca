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
    # peca ao servidor para te informar se voce é o servidor 1 ou o 2
    mensagem = comunicacao.recebe_mensagem(servidor_socket)[1]
    cliente_id = int(mensagem)
    print(f"cliente {cliente_id} conectado")
    return servidor_socket, cliente_id


def partida(servidor_socket, cliente_id):

    fim_jogo = False
    while True:
        mensagem = comunicacao.recebe_mensagem(servidor_socket)[1]
        print(mensagem)
        break
    # servidor informa qual a palavra para o jogo
    palavra = comunicacao.recebe_mensagem(servidor_socket)[1]
    while not fim_jogo:
        letra = input("\nDigite uma letra")
        # envia a letra pro servidor
        servidor_socket.sendall(f"{cliente_id}:{letra}".encode())
        # recebe a mensagem do servidor depois de jogar
        mensagem = comunicacao.recebe_mensagem(servidor_socket)[1]
        forca.imprime_palavra(palavra,mensagem)
        prefixo, mensagem= comunicacao.recebe_mensagem(servidor_socket)
        if(prefixo == 'fim' and mensagem == "fim"):
            print("Voce ganhou")
            fim_jogo = True
        elif(prefixo == 'fim' and mensagem == "nao_fim"):
            continue
    return


def main():
    servidor_socket, cliente_id = inicializa_sockets()
    partida(servidor_socket, cliente_id)


main()



