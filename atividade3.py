import re

# Solicita a senha do usuário
senha = input("Digite sua senha: ")

# Verifica os critérios
erros = []

if len(senha) < 8:
    erros.append("A senha deve ter pelo menos 8 caracteres.")
if not re.search(r"[A-Z]", senha):
    erros.append("A senha deve conter pelo menos uma letra maiúscula.")
if not re.search(r"[a-z]", senha):
    erros.append("A senha deve conter pelo menos uma letra minúscula.")
if not re.search(r"[0-9]", senha):
    erros.append("A senha deve conter pelo menos um número.")
if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
    erros.append("A senha deve conter pelo menos um caractere especial.")

# Resultado
if not erros:
    print("Senha válida! ✅")
else:
    print("Senha inválida. Veja os problemas:")
    for erro in erros:
        print("-", erro)