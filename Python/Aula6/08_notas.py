def notas():


    for i in range(2):
        nota = int(input('Digite a nota: '))

        arquivo = open("notas.txt", 'a')
        arquivo.write(str(nota) + '\n')
        arquivo.close() 




notas()