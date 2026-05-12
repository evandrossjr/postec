from time import localtime


def tarefas():

    tarefa1 = input('Digite uma tarefa: ')
    tarefa2 = input('Digite outra tarefa: ')
    tarefa3 = input('Digite mais uma tarefa: ')

    arquivo = open("tarefas.txt", 'a')

    arquivo.write(f"Tarefa: {tarefa1}\n")
    arquivo.write(f"Tarefa: {tarefa2}\n")
    arquivo.write(f"Tarefa: {tarefa3}\n")
    arquivo.write("---\n")


    print("Tarefas salvas com sucesso!")
    arquivo.close()

    arquivo = open("tarefas.txt", 'r')
    dados = arquivo.read()
    

    print(dados)

tarefas()