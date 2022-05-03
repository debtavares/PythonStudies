
def saudacao():
    nome = input('Qual o seu nome? ')
    print(f'Olá, {nome}')

print(saudacao())


nome = input('Qual o seu nome? ')           #saudacao com parametro

def saudacao_com_parametro(nome_da_pessoa):
  print(f'Olá, {nome_da_pessoa}')

print(saudacao_com_parametro(nome))