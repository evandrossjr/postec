from time import localtime


def salvar_sem_apagar():

    username = input('Digite o seu nome de usuário: ')


    data_agora = localtime().tm_mday, localtime().tm_mon, localtime().tm_year, localtime().tm_hour, localtime().tm_min, localtime().tm_sec
    arquivo = open("sem_apagar.txt", 'a')

    arquivo.write(f"{data_agora}\n")
    arquivo.write(f"Usuário: {username}\n")

    print("Usuário salvo com sucesso!")
    arquivo.close()

    arquivo = open("sem_apagar.txt", 'r')
    dados = arquivo.read()
    

    print(dados)

salvar_sem_apagar()