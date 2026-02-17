import math

a = int(input("Digite o valor do cateto adjacente: "))
b = int(input("Digite o valor do cateto oposto: "))

c = math.sqrt(a ** 2 + b ** 2) 

print("A hipotenusa é: ", c)
