#condicional

idade = int(input("Escreva sua idade: "))

def maioridade():
 if idade >= 18:
  print(f"A idade é {idade} e, portanto, é maior de idade")
 else:
  print(f"A idade é {idade} e, Portanto, é menor de idade")

print(maioridade())

######################################################################
#Laços e Loops

velocidade = [(100,20), (50,30)]

def velocidade_media(espaco,tempo):
  v = espaco / tempo
  print(f'velocidade: {v} m/s')

for espaco,tempo in velocidade:
  velocidade_media(espaco,tempo)