
positivo = ["bom", "excelente", "ótimo", "incrível", "maravilhoso", "fantástico"]

negativo = [ "péssimo", "horrível", "fraco", "ruim", "terrível", "chato"]


def sentimentos():

    sentimento = input('Digite um sentimento: ')
    
    arquivo = open("sentimentos.txt", 'a')

    
    if sentimento in positivo:
        arquivo.write(f"Sentimento positivo: {sentimento}\n")
        print("Sentimento salvo com sucesso!")
    elif sentimento in negativo:
        arquivo.write(f"Sentimento negativo: {sentimento}\n")
        print("Sentimento salvo com sucesso!")
    else:        
        print("sentimento inválido.")


    
    arquivo.close()

    print("Exibindo sentimentos salvos:")
    arquivo = open("sentimentos.txt", 'r')
    dados = arquivo.read()
    

    print(dados)

sentimentos()