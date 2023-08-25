import socket
import comunicacao
import forca


def inicializaservidor():
    # Definir a porta e o endereço do servidor
        
    porta = 2000
    endereco_servidor = 'localhost'
        
    # Criar o socket do servidor
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    # Vincular o socket do servidor à porta e endereço definidos
    servidor_socket.bind((endereco_servidor, porta))
        
    # Habilitar o servidor para ouvir conexões
    servidor_socket.listen(2)
    print('Servidor pronto para receber conexões!')
    return servidor_socket


clientes = []


def cria_conexoes_clientes(servidor_socket):
    clientes_conectados = 0
    
    while clientes_conectados < 2:
        # Esperar por conexões de clientes
        cliente_socket, endereco_cliente = servidor_socket.accept()
        apelido = comunicacao.recebe_mensagem(cliente_socket)[1]
        print(f'Cliente {apelido} conectado de:', endereco_cliente)
        # Avisar para os clientes quem é o 1 e quem é o 2:
        cliente = {"cliente_socket": cliente_socket, "apelido": apelido}
        comunicacao.envia_mensagem("cliente", str(clientes_conectados + 1), 
                                   cliente_socket)
        clientes.append(cliente)
        clientes_conectados += 1
            
    cliente_socket1, cliente_socket2 = clientes[0]['cliente_socket'], clientes[1]['cliente_socket']
    print('Dois clientes conectados.')
    
    for cliente in clientes:
        mensagem_broadcast = str(1)
        comunicacao.envia_mensagem("cliente", mensagem_broadcast, cliente
                                   ['cliente_socket'])

    return cliente_socket1, cliente_socket2


def controle_jogo(cliente_socket1, cliente_socket2):
    chances = 5
    palavra = "python"
    letras_usuario = []
    fim = 0
    vez = 1
    #informa aos dois jogadores qual a palavra para ser descoberta

    comunicacao.envia_mensagem("palavra","python",cliente_socket1)

    comunicacao.envia_mensagem("palavra","python",cliente_socket2)

    
    while not fim :
            jogada_valida = 0 
            print("teste")
            if(vez == 1):
                comunicacao.envia_mensagem('sua_vez','1',cliente_socket1)
                cliente_atual = cliente_socket1
            elif(vez == 2): 
                comunicacao.envia_mensagem('sua_vez','2',cliente_socket2)
                cliente_atual = cliente_socket2
            # jogo
            print("teste2")
            while not jogada_valida:
                id_cliente, letra = comunicacao.recebe_mensagem(cliente_atual)
                print(letras_usuario)
                letras_usuario, chances = forca.jogo_da_forca(letras_usuario, chances, 
                                                            palavra, letra)
                
                # envia a jogada para o jogador
                comunicacao.envia_mensagem(chances,letras_usuario,cliente_atual)
                # informa ao jogador quantas chances ele tem
                # ps: apenas para fim de informaçao pq o servidor faz o controle

                ganhou = forca.verifica_fim(palavra,chances,letras_usuario)
                jogada_valida = 1
                vez = vez%2 +1
                print(vez)
                if(ganhou):
                        comunicacao.envia_mensagem("fim","ganhou",cliente_socket1)
                        
                        comunicacao.envia_mensagem("fim","ganhou",cliente_socket2)
                        fim = 1

                        break
                if(chances == 0):
                    if(ganhou):
                        comunicacao.envia_mensagem("fim","ganhou",cliente_socket1)

                        comunicacao.envia_mensagem("fim","ganhou",cliente_socket2)
                        fim = 1

                        break
                    comunicacao.envia_mensagem("fim","perdeu",cliente_socket1)

                    comunicacao.envia_mensagem("fim","perdeu",cliente_socket2)
                    fim = 1

                    break
                else:
                    comunicacao.envia_mensagem("fim","nao_fim",cliente_atual)


        
def main():
    servidor = inicializaservidor()
    cliente1, cliente2 = cria_conexoes_clientes(servidor)
    controle_jogo(cliente1,cliente2)
    

main()

