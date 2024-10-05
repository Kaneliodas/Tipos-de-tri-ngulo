#Faça um Programa que peça os 3 lados de um triângulo;
#O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno;
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
L1 = float(input("Digite o 1° lado do Triângulo: "))
L2 = float(input("Digite o 2° lado do Triângulo: "))
L3 = float(input("Digite o 3° lado do Triângulo: "))

if (L1 + L2 > L3 and L1 + L3 > L2 and L3 + L2 > L1):
    print("O triangulo é um Triângulo verdadeiro.")
    
if (L1 == L2 and L1 == L3 and L2 == L3):
    triangulo = 'Triângulo Equilátero'
    
elif (L1 == L2 or L2 == L1 or L3 == L2 ):
    triangulo = 'Triângulo Isósceles'
    
elif (L1 != L2 and L2 != L3 and L1 != L3):
    triangulo = 'Triângulo Escaleno'
else:
    triangulo = 'Triângulo não indentificado'
print("O Triângulo é um : ",triangulo)
