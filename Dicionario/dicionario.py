
#Dicionário montado por tupla

contatos_lista = [
('Yan', '1234-5678'),     #0
('Pedro', '9999-9999'),   #1
('Ana', '8765-4321'),     #2
('Marina', '8877-7788')   #3
]

print(contatos_lista[3])     #('Marina', '8877-7788')
print(contatos_lista[3][1])  #8877-7788


#Dicionário transformado de tupla para tipo dict
#Torna possível achar o número através do nome

contatos = dict(contatos_lista)             #{'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'Marina': '8877-7788'}
print(contatos['Yan'])                      #Mostra o número do Yan
print('Yan' in contatos)                    #boolean - só é possível para chaves
print('9999-9999' in contatos.values())     #boolean para valores

contatos['João'] = '8887-7778'              #adicionando joão em contatos
print(contatos)

del contatos['Marina']                      #deletando Marina dos contatos
print(contatos)

#Adicionando mais contatos

contatos_novos = {
'Yan': '1234-5678', 
'Fernando': '4345-5434',
'Luiza': '4567-7654'}

for nome in contatos_novos:
    contatos[nome] = contatos_novos[nome]

print(contatos)

#Adicionando o prefixo 9

meus_contatos_novo = {nome: '9' + contatos[nome] for nome in contatos}
print(meus_contatos_novo)

