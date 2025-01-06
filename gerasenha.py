import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if comprimento < 1:
        print("O comprimento da senha deve ser maior que 0.")
        return ""

    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def menu():
    print("\n--- Gerador de Senhas Seguras ---")
    comprimento = int(input("Digite o comprimento desejado para a senha (padrão: 12): ") or 12)
    incluir_maiusculas = input("Incluir letras maiúsculas? (S/N, padrão: S): ").strip().upper() != "N"
    incluir_numeros = input("Incluir números? (S/N, padrão: S): ").strip().upper() != "N"
    incluir_simbolos = input("Incluir símbolos? (S/N, padrão: S): ").strip().upper() != "N"

    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_simbolos)
    print(f"\nSenha Gerada: {senha}")

# Executa o programa
menu()
