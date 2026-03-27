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
    soma = 0
    for letra in nome.upper():
        if letra != ' ': # ignorar espacos
            soma += ord(letra)
    return soma%tamanho_tabela

def le_arquivo():
    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        nomes = [linha for linha in arquivo]
    #print(nomes[:10])
    return nomes

# busca na hash!
def busca(nome_chave, tabela, tamanho_tabela):
    # a categoria provavel
    print("----- busca na tabela hash -----")
    cat = hash_completa(nome_chave, tamanho_tabela)
    lista_nomes = tabela[cat]
    passos = 0
    # busca sequencial
    for nome in lista_nomes:
        passos = passos + 1 # contador de passos na busca
        if nome_chave == nome:
            print(f"numero de comparacoes {passos}")
            print(f"{nome_chave} encontrado na categoria {cat}")
            return nome # registros
    print(f"numero de comparacoes {passos}")
    print(f"{nome_chave} NAO encontrado na categoria {cat}")
    return None  # null

def busca_sequencial_na_lista(nome_chave, lista_nomes):
    passos = 0
    print("----- busca na lista unidimensional (vetor) -----")
    for nome in lista_nomes:
        passos += 1 # passos = passos + 1,     ou passos++ do c
        if nome_chave == nome:
            print(f"numero de comparacoes {passos}")
            print(f"{nome_chave} encontrado")
            return nome
    print(f"numero de comparacoes {passos}")
    print(f"{nome_chave} NAO encontrado")
    return None  # null

if __name__ == "__main__":
    # salva_arquivo(1000000)
    lista_nomes = le_arquivo()
    tamanho_M = 107
    tabela = {}
    lista_unica = [] # alternativa unidimensional
    # inicializando a tabela
    for i in range(tamanho_M):
        tabela[i] = []

    # percorrer os nomes da lista e armazenar na categoria correta
    for nome in lista_nomes:
        # categoria = hash_inicial(nome, tamanho_M)
        nome = nome.replace("\n","")
        categoria = hash_completa(nome, tamanho_M)
        # print(f"{nome} - {categoria}")
        tabela[categoria].append(nome)
        # somente pra comparar hash com lista unidimensional
        lista_unica.append(nome)

    # copiei do exemplo001.py
    for categoria in tabela:
        total = len(tabela[categoria])
        print(f"categoria: {categoria} - {int(total/100)*'*'}")

    fator_carga = 20000/tamanho_M
    print(f"fator carga: {int(fator_carga)}")
    print("Visualizar alguns nomes")
    for categoria in tabela:
        elementos = tabela[categoria][:3]
        print(f"{categoria} = {elementos}")

    nome_procurado = "Cebolinha"
    pesquisa = busca(nome_procurado, tabela, tamanho_M)
    pesquisa = busca_sequencial_na_lista(nome_procurado, lista_unica)