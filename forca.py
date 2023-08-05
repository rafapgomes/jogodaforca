def jogo_da_forca(letras_usuario, chances, palavra, letra_user):
    # criar a nossa logica
    
    imprime_palavra(palavra, letras_usuario)

    tentativa = letra_user
    letras_usuario.append(tentativa.lower())
        
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    
    return letras_usuario, chances
        
        
def verifica_fim(palavra, chances, letras_usuario):
    ganhou = True

    for letra in palavra:

        if letra.lower() not in letras_usuario:

            ganhou = False

    if ganhou:
        return ganhou    


def imprime_palavra(palavra, letras_usuario):
    for letra in palavra:

        if letra.lower() in letras_usuario:

            print(letra, end=" ")

        else:
            print("_", end=" ")


