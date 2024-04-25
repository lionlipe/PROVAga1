def main():
    # Estoque 
    estoque = {
        'Pó de Fênix': 100,
        'Essência Celestial': 50,
        'Raiz de Dragão': 45,
        'Orvalho Lunar': 30,
        'Flores secas': 200,
        'Elixir amargo': 20,
        'Lágrimas de unicórnio': 15
    }

    #  Quantidade necessária das poções
    receitas = {
        1: {'Pó de Fênix': 30, 'Essência Celestial': 20, 'Flores secas': 20, 'Lágrimas de unicórnio': 10}, #Poção de Cura
        2: {'Orvalho Lunar': 20, 'Raiz de Dragão': 30, 'Flores secas': 30},#Poção Força da Floresta
        3: {'Essência Celestial': 30, 'Pó de Fênix': 50},#Poção Sabedoria daRiqueza
        4: {'Orvalho Lunar': 10, 'Flores secas': 50, 'Lágrimas de unicórnio': 5},#Poção Sorte no Amor
        5: {'Elixir amargo': 10, 'Raiz de Dragão': 15}#Poção Malvada
    }

    while True: # se for falso, terminar o while
        print(" O que você deseja? ")
        print("1. Preparar uma poção")
        print("2. Consultar os ingredientes disponíveis")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            escolherPocao = int(input("Digite APENAS o número da poção que você deseja preparar, (pocão 1:Poção de Cura, pocão 2:Poção Força da Floresta, pocão 3:Poção Sabedoria daRiqueza, pocão 4:Poção Sorte no Amor, pocão 5:Poção Malvada. ): "))
            if escolherPocao in receitas:
                podeCriar = True
                for ing, quantidade in receitas[escolherPocao].items():
                    if estoque[ing] < quantidade:
                        podeCriar = False
                        print(f"Falta do ingrediente: {ing}")
                if podeCriar:
                    for ing, quantidade in receitas[escolherPocao].items():
                        estoque[ing] -= quantidade
                    print("Poção criada com sucesso!")
            else:
                print("Número de poção inválido.")
        elif opcao == '2':
            for ing, quantidade in estoque.items():
                print(f"{ing}: {quantidade}")
        elif opcao == '3':
            break
        else:
            print("Opção inválida, tente novamente.")

main()