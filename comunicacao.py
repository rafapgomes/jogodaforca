def envia_mensagem(prefixo, mensagem, destinatario):
    destinatario.sendall(f"{prefixo}:{mensagem}".encode())   


def recebe_mensagem(socket):
    dados_cliente = socket.recv(1024)
    prefixo, mensagem = dados_cliente.decode().split(':')
    return prefixo, mensagem

