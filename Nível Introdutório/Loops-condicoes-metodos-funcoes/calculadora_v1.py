# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

#Resolver a saída da calculadora.
def soma(x, y):
    res = x + y
    print(x, " + ", y, " = ", res)

def sub(x, y):
    res = x - y
    print(x, " - ", y, " = ", res)

def mult(x, y):
    res = x * y
    print(x, " * ", y, " = ", res)

def div(x, y):
    res = x / y
    print(x, " / ", y, " = ", res)
          
print("\n******************* Calculadora em Python *******************")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input('Informe a operação desejada: '))
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

if op == 1:
    soma(num1, num2)
elif op == 2:
    sub(num1, num2)
elif op == 3:
    mult(num1, num2)
elif op == 4 and num2 != 0:
    div(num1, num2)
else:
    print("Operação Inválida. Tente novamente.")
