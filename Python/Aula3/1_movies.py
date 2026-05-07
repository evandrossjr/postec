import random


actionMovies = ["John Wick", "Mad Max: Estrada da Fúria", "Missão Impossível", "Gladiador", "Velozes e Furiosos"]
comedyMovies = ["As Branquelas", "Gente Grande", "Se Beber, Não Case", "Todo Mundo em Pânico", "Debi & Loide"]
terrorMovies = ["Invocação do Mal", "Hereditário", "O Exorcista", "It: A Coisa", "A Freira"]


def movieIndicator():

    print("O que assistiri hoje?")
    genre = input("Digite o gênero do filme (Ação, Comédia, Terror): ")
    

    match genre.lower():
        case  "ação" | "acao":
            print(f"Filme de ação selecionado. O filme indicado é: {random.choice(actionMovies)}")

        case "comédia" | "comedia":
            print(f"Filme de comédia selecionado. O filme indicado é: {random.choice(comedyMovies)}")    
        case "terror":
            print(f"Filme de terror selecionado. O filme indicado é: {random.choice(terrorMovies)}")
        case _:
            print("Gênero inválido. Por favor, escolha entre Ação, Comédia ou Terror.")



movieIndicator()