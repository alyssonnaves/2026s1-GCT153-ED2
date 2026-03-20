import random as rnd

# github.com/alyssonnaves
tamanho_tabela = 10 # M - qual usar? 20 - arbitraria
def hash(chave):
  
  return chave%tamanho_tabela # % resto da divisao

tabela = {}

for i in range(tamanho_tabela):
  tabela[i]=[]

for _ in range(20000):
  numero = rnd.randint(5000, 10000)
  hashcode = hash(numero)
  #print(numero)
  tabela[hashcode].append(numero)


for categoria in tabela:
  total = len(tabela[categoria])
  print(f"categoria: {categoria} - {total}")
print("-----")
for categoria in tabela:
  total = len(tabela[categoria])
  print(f"categoria: {categoria} - {int(total/100)*'*'}")