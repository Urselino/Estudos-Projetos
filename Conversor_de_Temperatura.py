def exibir_menu():
    print("Menu:")
    print("1. Fahrenheit para Celsius")
    print("2. Celsius para Fahrenheit")
    print("3. Sair")
    print()

def fahrenheit_para_celsius(temp_f):
    return (temp_f - 32) * 5 / 9

def celsius_para_fahrenheit(temp_c):
    return (temp_c * 9 / 5) + 32

# Loop do menu
while True:
    exibir_menu()
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        temp_f = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_para_celsius(temp_f)
        print(f"{temp_f} Fahrenheit equivale a {resultado:.2f} Celsius.")
    elif escolha == '2':
        temp_c = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(temp_c)
        print(f"{temp_c} Celsius equivale a {resultado: .2f} Fahrenheit.")
    elif escolha == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Por favor, digite um número válido.")

    input("Pressione Enter para continuar...")
    print()  # Adiciona uma linha em branco para separar visualmente as execuções

print("Programa encerrado.")