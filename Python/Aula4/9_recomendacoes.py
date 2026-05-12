import random



actionMovies = ["John Wick", "Mad Max: Estrada da Fúria", "Missão Impossível", "Gladiador", "Velozes e Furiosos"]
comedyMovies = ["As Branquelas", "Gente Grande", "Se Beber, Não Case", "Todo Mundo em Pânico", "Debi & Loide"]
terrorMovies = ["Invocação do Mal", "Hereditário", "O Exorcista", "It: A Coisa", "A Freira"]


def recomendacoes():


    arquivo = open("recomendacoes.txt", 'a')

    print("O que assistiri hoje?")
    genre = input("Digite o gênero do filme (Ação, Comédia, Terror): ")
    

    match genre.lower():
        case  "ação" | "acao":
            actionMovie = random.choice(actionMovies)
            print(f"Filme de ação selecionado. O filme indicado é: {actionMovie}")
            arquivo.write(f"Filme de ação selecionado. O filme indicado é: {actionMovie}\n")
        case "comédia" | "comedia":
            comedyMovie = random.choice(comedyMovies)
            print(f"Filme de comédia selecionado. O filme indicado é: {comedyMovie}")
            arquivo.write(f"Filme de comédia selecionado. O filme indicado é: {comedyMovie}\n")
        case "terror":
            terrorMovie = random.choice(terrorMovies)
            print(f"Filme de terror selecionado. O filme indicado é: {terrorMovie}")
            arquivo.write(f"Filme de terror selecionado. O filme indicado é: {terrorMovie}\n")
        case _:
            print("Gênero inválido. Por favor, escolha entre Ação, Comédia ou Terror.")

    arquivo.close()

    arquivo = open("recomendacoes.txt", 'r')
    dados = arquivo.read()
    print("Exibindo recomendações salvas:")
    print(dados)    

recomendacoes()