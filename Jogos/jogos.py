import forca
import advinhacao


print("#################################")
print("Escolha seu jogo!")
print("#################################")

print("(1)Forca (2) Adivinhação")

jogo = int(input("Qual jogo?"))

if(jogo==1):
    print("Jogando forca")
    forca.forca()
elif(jogo==2):
    print("Jogando advinhação")
    advinhacao.advinhacao()
else:
    print("Escolha uma opção válida")