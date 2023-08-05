def jogo_da_forca(letra_cliente,chance):
    palavra = "python"

    letras_usuario = []

    chances = chance

    ganhou = False
    while True:

        # criar a nossa logica

        for letra in palavra:

            if letra.lower() in letras_usuario:

                print(letra, end=" ")

            else:

                print("_", end=" ")

        print(f"Você tem {chances} chances")

        tentativa = letra_cliente

        letras_usuario.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():

            chances -= 1

        ganhou = True

        for letra in palavra:

            if letra.lower() not in letras_usuario:

                ganhou = False

        if chances == 0 or ganhou:

            break

    if ganhou:

        print(f"Parabéns, você ganhou. A palavra era: {palavra}")

    else:

        print(f"Você perdeu! A palavra era: {palavra}")


