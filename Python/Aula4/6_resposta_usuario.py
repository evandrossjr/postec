from time import localtime


def resposta_usuario():

    message = input('Digite uma resposta: ')


    data_agora = localtime().tm_mday, localtime().tm_mon, localtime().tm_year, localtime().tm_hour, localtime().tm_min, localtime().tm_sec
    arquivo = open("respostas.txt", 'a')

    arquivo.write(f"Criado em: {data_agora}\n")
    arquivo.write(f"Resposta: {message}\n")

    print("Resposta salva com sucesso!")
    arquivo.close()

    arquivo = open("respostas.txt", 'r')
    dados = arquivo.read()
    

    print(dados)

resposta_usuario()