# Solicita os dois números
num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Verifica o operador e realiza a operação
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero."
else:
    resultado = "Operador inválido."

# Exibe o resultado
print("Resultado:", resultado)