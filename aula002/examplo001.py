import random as rnd


def hash(chave):
  tamanho_tabela = 17   # M - qual usar? 20 - arbitraria
  return chave%tamanho_tabela # % resto da divisao

tabela = {}
tamanho_tabela = 17
for i in range(tamanho_tabela):
  tabela[i]=[]

for _ in range(2000):
  numero = rnd.randint(5000, 10000)
  hashcode = hash(numero)
  #print(numero)
  tabela[hashcode].append(numero)


for categoria in tabela:
  total = len(tabela[categoria])
  print(f"categoria: {categoria} - {total}")

  for categoria in tabela:
    total = len(tabela[categoria])
    print(f"categoria: {categoria} - {total*'*'}")