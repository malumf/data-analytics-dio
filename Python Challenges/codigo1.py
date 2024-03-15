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
