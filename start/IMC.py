#Calculadora de IMC

height = float(input("Digite a sua altura: "))
weight = float(input("Digite o sue peso: "))

imc = weight / height ** 2

if imc < 18.5 :
    print("Seu IMC é de: ", imc, " e está abaixo do peso normal")
elif 18.5 <= imc < 24.9 :
    print("Seu IMC é de: ", imc, " e está dentro do peso normal")
elif 25 <= imc < 29.9 :
    print("Seu IMC é de: ", imc, " e está acima do peso normal")
elif 30 <= imc < 34.9 :
    print("Seu IMC é de: ", imc, " e está como obesidade classe 1")
elif 35 <= imc < 39.9 :
    print("Seu IMC é de: ", imc, " e está como obesidade classe 2")
else :
    print("Seu IMC é de: ", imc, " e está como obesidade classe 3")