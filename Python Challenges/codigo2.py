# Lista para armazenar os itens
itens = []
for i in range(3):
  nome_item=input()
  itens.append(nome_item)

# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")
