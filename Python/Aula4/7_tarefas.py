from time import localtime


def tarefas():

   

    arquivo = open("tarefas.txt", 'a')

    for i in range(3):

        tarefa = input('Digite uma tarefa: ')
        arquivo.write(f"Tarefa: {tarefa}\n")
 


    print("Tarefas salvas com sucesso!")
    arquivo.close()

    arquivo = open("tarefas.txt", 'r')
    dados = arquivo.read()
    

    print(dados)

tarefas()