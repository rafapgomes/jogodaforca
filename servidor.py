import socket
import comunicacao

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
        #Avisar para os clientes quem é o 1 e quem é o 2:
        cliente = {"cliente_socket": cliente_socket, "apelido": apelido}
        comunicacao.envia_mensagem("cliente",str(clientes_conectados + 1),cliente_socket)
        clientes.append(cliente)
        clientes_conectados += 1
            
    cliente_socket1, cliente_socket2 = clientes[0]['cliente_socket'], clientes[1]['cliente_socket']
    print('Dois clientes conectados.')
    
    for cliente in clientes:
         mensagem_broadcast = str(1)
         comunicacao.envia_mensagem("cliente",mensagem_broadcast,cliente['cliente_socket'])

    return cliente_socket1, cliente_socket2

def controle_jogo(cliente_socket1,cliente_socket2):
    mensagem = comunicacao.recebe_mensagem(cliente_socket1)
    print(mensagem)

    
    return

def main():
    servidor = inicializaservidor()
    cliente1, cliente2 = cria_conexoes_clientes(servidor)
    controle_jogo(cliente1,cliente2)
    

main()

