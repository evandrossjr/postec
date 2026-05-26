def chatbot(username):

    message = input(f'{username}, "digite uma mensagem: ')


    arquivo = open("historico_ia.txt", 'w')
    arquivo.write(message + '\n')
    arquivo.close()

    print("Mensagem salva com sucesso!")


chatbot("X899")