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
    vez_jogador = 0 
    while True:
        mensagem = comunicacao.recebe_mensagem(servidor_socket)[1]
        print(mensagem)
        break
    # servidor informa qual a palavra para o jogo
    palavra = comunicacao.recebe_mensagem(servidor_socket)
    
    print(palavra)
    
    while not fim_jogo:
            if  vez_jogador == 0:
                    print("Aguarde")
            prefixo,mensagem = comunicacao.recebe_mensagem(servidor_socket)
            if(prefixo == "sua_vez" and int(mensagem) == cliente_id):
                    vez_jogador = 1

            elif(prefixo == "fim" and mensagem == "ganhou" ):
                 print("Cliente 1 ganhou")
                 break
            while vez_jogador:
    
                    letra = input("\nDigite uma letra")
                    # envia a letra pro servidor
                    servidor_socket.sendall(f"{cliente_id}:{letra}".encode())
                    # recebe a mensagem do servidor depois de jogar
                    chance,mensagem = comunicacao.recebe_mensagem(servidor_socket)
                    forca.imprime_palavra(palavra,mensagem)

                    # recebe a mensagem informando quantas chances o cliente tem
                    print("Voce tem ",chance,"chances")

                    # recebe a mensagem informando sobre o estado do jogo
                    prefixo, mensagem= comunicacao.recebe_mensagem(servidor_socket)
                    # recebe a mensagem informando sobre as chances que o cliente ainda tem
                    # verifica se o jogador ganhou, caso contrário ele continua jogando
                    if(prefixo == 'fim' and mensagem == "ganhou"):
                        print("Voce ganhou")
                        fim_jogo = True
                        break
                    
                    # verifica se o jogador perdeu
                    elif(prefixo == "fim" and mensagem == "perdeu"):
                        print("Suas chances acabaram")
                        print("A palavra era ",palavra)
                        fim_jogo = True
                        break

                    # caso o jogador nao tenha perdido e nem ganhado, continua jogando
                    elif(prefixo == 'fim' and mensagem == "nao_fim"):
                        continue
                    
                
                      
            

def main():
    servidor_socket, cliente_id = inicializa_sockets()
    partida(servidor_socket, cliente_id)


main()



