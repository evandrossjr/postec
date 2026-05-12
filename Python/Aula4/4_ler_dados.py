import random


movies = ["John Wick", "Mad Max: Estrada da Fúria", "Missão Impossível", "Gladiador", "Velozes e Furiosos","As Branquelas", "Gente Grande", "Se Beber, Não Case", "Todo Mundo em Pânico", "Debi & Loide","Invocação do Mal", "Hereditário", "O Exorcista", "It: A Coisa", "A Freira"]




def ler_dados():
    arquivo = open("dados.txt", 'w')

    arquivo.write(f"Filme: {random.choice(movies)}\n")
    arquivo.write(f"Filme: {random.choice(movies)}\n")
    arquivo.write(f"Filme: {random.choice(movies)}\n")
    print("Dados salvos com sucesso!")
    arquivo.close()

    arquivo = open("dados.txt", 'r')
    dados = arquivo.read()
    

    print(dados)

ler_dados()