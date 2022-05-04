import random

class forca():
    def mensagem_abertura():
        print("*********************************")
        print("***Bem vindo ao jogo da Forca!***")
        print("*********************************")


    def carrega_palavra_secreta():
        arquivo = open("palavras.txt", "r")
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

        numero = random.randrange(0,len(palavras))
        palavra_secreta = palavras[numero].upper()

        return palavra_secreta

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = ["_" for letra in palavra_secreta]  
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0


    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-tentativas))

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")

print(forca())