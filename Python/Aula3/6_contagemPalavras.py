
positivo = ["bom", "excelente", "ótimo", "incrível", "maravilhoso", "fantástico"]

negativo = [ "péssimo", "horrível", "fraco", "ruim", "terrível", "chato"]


def contagemdePalavras():
    positivas = 0
    negativas = 0

    while True:
        message = input("Digite sua mensagem: ")

        match message.lower():
            case c if c in positivo:
                positivas += 1
                print("Feedback positivo!")
                
            case c if c in negativo:
                negativas += 1
                print("Feedback negativo!")
            case "sair" | "adeus":
                print("Até mais! Tenha um ótimo dia!")
                print(f"Total de feedbacks positivos: {positivas}")
                print(f"Total de feedbacks negativos: {negativas}")
                break
            case _:
                print("Desculpe, não entendi sua mensagem. Por favor, tente novamente.")


contagemdePalavras()