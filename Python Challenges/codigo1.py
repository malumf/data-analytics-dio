# funcao
def Verifica_Passos(numero):
  while numero<0:
    numero=int(input())
  return numero
# Entrada
quantidade_passos = int(input())

quantidade_passos= Verifica_Passos(quantidade_passos)

if quantidade_passos==0:
  print("Nenhum passo dado na floresta.")
else:
  for i in range(1, quantidade_passos+1):
    if i==1:
      print("Explorador: 1 passo")
    else:
      print(f"Explorador: {i} passos")

'''
Desafio
Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

Entrada
Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta. .

Saída
O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
'''
