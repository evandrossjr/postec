#SEQUÊNCIA DE FIBONACCI

a,b = 2, 3
print("Sequ/ência de Fibonacci:")

for i in range(20):
    print(a, end=' ')
    a, b = b, a + b 