#calculadora simples

numero1 = 0
numero2 = 0
resultado = 0
operacao = ''

numero1 = float(input("digite o primeiro numero: "))
operacao = input("digite a operação: ")
numero2 = float(input("digite o segundo numero: "))

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
     resultado = numero1 - numero2
elif operacao == '/':
     resultado = numero1 / numero2
elif operacao == '*':
     resultado = numero1 * numero2
else: 'operação invalida'


print(str(numero1) + '' + str(operacao) + '' + str(numero2) + ' = ' + str(resultado))
