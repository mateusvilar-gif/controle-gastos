def mostrar_menu():
    print("\n=== Controle de Gastos ===")
    print("1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Sair")


def main():
    gastos = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do gasto: ")
            valor = float(input("Valor: "))
            gastos.append({"nome": nome, "valor": valor})
            print("Gasto adicionado com sucesso!")

        elif opcao == "2":
            print("\n--- Lista de Gastos ---")
            for g in gastos:
                print(f"{g['nome']} - R${g['valor']}")

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
