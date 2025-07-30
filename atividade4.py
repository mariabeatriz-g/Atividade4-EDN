# Inicializa contadores
pares = 0
impares = 0

# Solicita a quantidade de números a serem inseridos
quantidade = int(input("Quantos números você deseja digitar? "))

# Loop para receber e classificar os números
for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        pares += 1
        print(f"{numero} é par.")
    else:
        impares += 1
        print(f"{numero} é ímpar.")

# Exibe o resultado final
print("\nResumo:")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")