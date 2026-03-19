
def exibe_dados(registro):
    print(f"Nome: {registro['nome']}")
    print(f"Idade: {registro['idade']}")


if __name__ == "__main__":
    nomes = {}
    nomes["123"] = {"nome": "Pele", "idade": 80}
    nomes["456"] = {"nome": "Maradona", "idade": 70}   


    print("Recuperar dados pela chave")
    chave = input("digite chave")
    exibe_dados(nomes[chave])
