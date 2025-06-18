# ==============================================
#  POKEDEX SIMPLES EM PYTHON 
# ==============================================
#  Desenvolvido como base para atividade prática
#  Objetivo: listar Pokémon e exibir informações
# ==============================================

# Lista de Pokémon representada por dicionários
pokedex = [
    {"nome": "Pikachu", "tipo": "Elétrico", "forca": 55},
    {"nome": "Charmander", "tipo": "Fogo", "forca": 52},
    {"nome": "Butterfree", "tipo": "inseto", "forca": 51},
    {"nome": "Bulbasaur", "tipo": "Grama", "forca": 49},
    {"nome": "Squirtle", "tipo": "Água", "forca": 48},
    {"nome": "Eevee", "tipo": "Normal", "forca": 50}
]

# Função principal que exibe o menu
def menu():
    while True:
        print("\n==============================")
        print("         POKEDEX PYTHON")
        print("==============================")
        print("1️⃣   LISTAR TODOS OS POKÉMONS")
        print("2️⃣   VER DETALHES DE UM POKÉMON")
        print("3️⃣   ADICIONAR UM NOVO POKÉMON")
        print("4️⃣   SAIR")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_pokemon()
        elif opcao == "2":
            buscar_pokemon()
        elif opcao == "3":
            adicionar_pokemon()
            break
        elif opcao == "4":
            print("\nSaindo da Pokedex. Até logo, treinador!")
            break
        else:
            print("\n Opção inválida. Tente novamente.")

# Função para listar todos os Pokémon
def listar_pokemon():
    print("\nLista de Pokémon:")
    print("------------------------------")
    for pokemon in pokedex:
        print(f"🔹 {pokemon['nome']} ({pokemon['tipo']})")
    print("------------------------------")

# Função para buscar detalhes de um Pokémon específico
def buscar_pokemon():
    nome = input("\nDigite o nome do Pokémon: ").capitalize()
    encontrado = False
    for pokemon in pokedex:
        if pokemon['nome'] == nome:
            print("\n==============================")
            print(f"Nome: {pokemon['nome']}")
            print(f"Tipo: {pokemon['tipo']}")
            print(f"Força: {pokemon['forca']}")
            print("==============================")
            encontrado = True
            break
    if not encontrado:
        print("\n Pokémon não encontrado na Pokedex.")

# Função para adicionar um novo Pokémon à Pokedex
def adicionar_pokemon():
    nome = input("Digite o nome do novo Pokémon: ").capitalize()
    tipo = input("Digite o tipo do novo Pokémon: ")
    while True: 
        try:
            forca = int(input("Digite a força do Pokémon (número inteiro):  "))
            if forca < 0:
                print("Força deve ser um número inteiro positivo. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a força.")

    # Adiciona o novo pokemón à lista
    pokedex.append({"nome": nome, "tipo": tipo, "forca" : forca})
    print(f"\n{nome} foi adicionado À Pokedex!")

    # Listar pokémon novamente para mostrar a atualização
    listar_pokemon()
    menu()

# Executar o menu
menu()
