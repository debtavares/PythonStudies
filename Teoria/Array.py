# Estudando listas

Acessorios = [
    'Rodas de liga', 
    'Travas elétricas', 
    'Piloto automático',
    'Bancos de couro',
    'Ar condicionado'
]

Acessorios.append('Airbag')           #Adiciona na lista
Acessorios.sort()                     #Ordem alfabética
Acessorios.pop()                      #Remove da lista
Acessorios.pop(2)                     #Remove um em específico

print(Acessorios)

#################################################################################
# Instrução for

for item in Acessorios:
	print(item)

#################################################################################
# Instrução if

dados = [
    ['Jetta', 2003, False],
    ['Passt', 1991, False],
    ['Crossfox', 1990, False],
    ['A5', 2019, True]
]

for lista in dados:
    print(lista[2])                     #Acessar o terceiro item da lista.

for lista in dados:
    if(lista[2] == True):               #Condicional: acessar apenas os itens com valor true
     print(lista)

zero_km = []
for lista in dados:
    if(lista[2] == True):               #Outra forma
     zero_km.append(lista)
     print(zero_km)

############################################################
#Função recursiva: quando retorna ela mesma

def fatorial(n):
 if n == 1:
    return 1
 else:
    return n * fatorial(n-1)

print(fatorial(5))          # 5 * 4 * 3 * 2 * 1 = 120

###########################################################

