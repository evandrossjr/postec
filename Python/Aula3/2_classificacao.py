positivo = ["bom", "excelente", "ótimo", "incrível", "maravilhoso", "fantástico"]

negativo = [ "péssimo", "horrível", "fraco", "ruim", "terrível", "chato"]

neutro = ["mais ou menos", "médio", "simples"]

def feedbackCliente():
    print("Sistema de classificação de atendimento")

    rating = input("Deixe o seu comentário com uma unica palavra: ")

    if rating in positivo:
        print("Feedback positivo!")
    elif rating in negativo:
        print("Feedback negativo!")   
    elif rating in neutro:
        print("Feedback neutro!")
    else:        
        print("Feedback inválido.")

    feedbackCliente()

feedbackCliente()


