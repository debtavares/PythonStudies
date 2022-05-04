import random

def adivinhacao():
    print("#################################")
    print("Bem vindo ao jogo de Adivinhação!")
    print("#################################")

    numero_secreto = round(random.random()*100)
    rodada = 1

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Defina o nível: "))
    if(nivel==1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    while(rodada <= total_de_tentativas):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))

        print("Você digitou ", chute)

        if numero_secreto == chute:
            print("Você acertou!") 
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi maior que o número secreto.")

        rodada += 1

    print("Fim de jogo!")

print(adivinhacao())