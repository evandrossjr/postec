def criar_arquivo():

    username = input('Digite o seu nome de usuário: ')


    arquivo = open("usuarios.txt", 'w')
    arquivo.write(username + '\n')
    arquivo.close()

    print("Usuário salvo com sucesso!")


criar_arquivo()