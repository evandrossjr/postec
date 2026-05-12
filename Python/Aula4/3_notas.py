def notas():

    nota1  = int(input('Digite a primeira nota: '))
    nota2  = int(input('Digite a segunda nota: '))


    arquivo = open("notas.txt", 'w')
    arquivo.write(str(nota1) + '\n')
    arquivo.write(str(nota2) + '\n')
    arquivo.close()

    print("Notas salvas com sucesso!")


notas()