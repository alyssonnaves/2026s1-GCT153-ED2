# !pip install Faker

from faker import Faker

fake = Faker('pt_BR')

def salva_arquivo(quantidade: int):
    with open("nomes.txt", "w",  encoding="utf-8") as arquivo:
        for _ in range(quantidade):
            nome = fake.name()
            arquivo.write(nome+"\n")

def hash_inicial(nome, tamanho_tabela=26):
    letra_inicial = nome[0].upper()
    codigo_ascii = ord(letra_inicial)
    return (codigo_ascii+13)%tamanho_tabela

def hash_completa(nome, tamanho_tabela=26):
    pass

def le_arquivo():
    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        nomes = [linha for linha in arquivo]
    #print(nomes[:10])
    return nomes



if __name__ == "__main__":
    # salva_arquivo(20000)
    lista_nomes = le_arquivo()
    tabela = {}
    # inicializando a tabela
    for i in range(26):
        tabela[i] = []

    # percorrer os nomes da lista e armazenar na categoria correta
    for nome in lista_nomes:
        categoria = hash_inicial(nome)
        # print(f"{nome} - {categoria}")
        tabela[categoria].append(nome)

    # copiei do exemplo001.py
    for categoria in tabela:
        total = len(tabela[categoria])
        print(f"categoria: {categoria} - {int(total/100)*'*'}")