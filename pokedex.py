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
        print("1️⃣  Listar todos os Pokémon")
        print("2️⃣  Ver detalhes de um Pokémon")
        print("3️⃣  Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_pokemon()
        elif opcao == "2":
            buscar_pokemon()
        elif opcao == "3":
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

# Executar o menu
menu()
