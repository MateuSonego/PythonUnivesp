# Tipos de Listas
numbers = [1, 2, 3, 4]
text = ["Ana", "João", "Carlos"]
mixed = [10, "Python", True]

#Acessando elementos de uma lista
numbers[0]      # primeiro elemento
numbers[-1]     # último elemento

#Modificando
numbers[1] = 20

#Métodos importantes
numbers.append(5)       # adiciona no final
numbers.insert(0, 99)   # adiciona em posição específica
numbers.remove(3)       # remove pelo valor
numbers.pop()           # remove último
numbers.sort()          # ordena
numbers.reverse()       # inverte

#Tuplas(São imutáveis)
coordinates = (10, 20)
names = ("Ana", "João")
single = (5,)   # precisa da vírgula
