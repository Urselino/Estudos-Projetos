def menu():
    print()
    print("--------------------")
    print("1. Verificar quantas palavras tem: ")
    print("2. Sair")
    print("--------------------")
    print()
while True:
    menu()
    escolha = input("Digite sua opção: ")
    print()
    if escolha == '1':
        frase = input("Digite sua frase: ")
        quant = frase.split(" ")
        print("Quantida de palabras é igual a:",len(quant))
    elif escolha == '2':
        print("Saindo do programa.")
        break
    else:
        print("Error")
    print()    
    input("Pressione Enter para continuar...")
    print()