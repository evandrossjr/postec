# TABUADA

numeroTabuada = int(input("Digite um número para a tabuada: "))

print(f"Tabuada do {numeroTabuada}:")
for i in range(1, 11):
    resultado = numeroTabuada * i
    print(f"{numeroTabuada} x {i} = {resultado}")
