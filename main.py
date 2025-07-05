
from entidades.voo import Voo
from entidades.assento import Assento
from gerador import gerar_cliente_faker, gerar_tripulante_faker
import random
import os

def clear_screen() -> None:
    """
    Limpa a tela do terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

destinos = ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza",
    "Belo Horizonte", "Manaus", "Porto Alegre", "Curitiba", "Recife"]
voos: list[Voo] = []

 # Criaando 10 voos ja com tods as infrmacoes completas
for numero_voo in range(10):

    id_voo = f"V{numero_voo+1:03d}"
    destino = destinos[numero_voo]
    voo = Voo(id_voo, destino)
# ta sendo gerado aqui ja dentro
    piloto = gerar_tripulante_faker("piloto")
    copiloto = gerar_tripulante_faker("copiloto")
    comissarios = [gerar_tripulante_faker("comissario") for _ in range(3)]

    voo.adicionar_tripulante(piloto)
    voo.adicionar_tripulante(copiloto)
    for comissario in comissarios:
        voo.adicionar_tripulante(comissario)

    assentos_livres = [assento for assento in voo.assentos if not assento.ocupado]
    assentos_escolhidos = random.sample(assentos_livres, 10)

    for assento in assentos_escolhidos:
        cliente = gerar_cliente_faker() # ta sendo gerado aqui ja dentro
        assento.reservar(cliente)
        cliente.adicionar_reserva(voo.id_voo, voo.destino, assento.numero)

    voos.append(voo)

print(" Todos os voos foram criados com sucesso!!")
clear_screen()

#menu principal
def menu_principal() -> None:
    """
    Exibe o menu principal e direciona o usuário para os submenus.
    """
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Acessar como Cliente")
        print("2. Acessar como Administrador")
        print("3. Visualizar Voos (modo leitura)")
        print("4. Sair")

        opcao: str = input("Escolha uma opção: ")

        if opcao == "1":
            clear_screen()
            print("[!] Menu de cliente ainda em construção.")
        elif opcao == "2":
            clear_screen()
            #enu_administrador()
        elif opcao == "3":
            clear_screen()
            #menu_visualizacao()
        elif opcao == "4":
            print("Sistema encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
#menu visu
def menu_visualizacao() -> None:
    """
    Menu público com opções básicas de consulta.
    """
    while True:
        print("\n=== VISUALIZAÇÃO DE VOOS ===")
        print("1. Listar voos")
        print("2. Ver destino de um voo")
        print("3. Ver ocupação geral")
        print("0. Voltar")

        escolha: str = input("Escolha uma opção: ")

        if escolha == "1":
            clear_screen()
            listar_voos()
        elif escolha == "2":
            clear_screen()
            ver_destino()
        elif escolha == "3":
            clear_screen()
            ver_ocupacao()
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")
#menu adm
def menu_administrador() -> None:
    """
    Menu exclusivo do administrador com acesso a dados completos.
    """
    while True:
        print("=== MENU ADMINISTRADOR ===")
        print("1. Listar voos")
        print("2. Ver tripulação de um voo")
        print("3. Ver relatório de ocupação")
        print("4. Ver passageiros do voo")
        print("0. Voltar")

        opcao: str = input("Escolha uma opção: ")

        if opcao == "1":
            clear_screen()
            listar_voos()
        elif opcao == "2":
            clear_screen()
            ver_tripulacao()
        elif opcao == "3":
            clear_screen()
            ver_ocupacao()
        elif opcao == "4":
            clear_screen()
            ver_passageiros()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
#menu cliente
def menu_cliente() -> None:
    """
    Menu destinado ao cliente (em construção).
    """
    while True:
        print("=== MENU CLIENTE ===")
        print("1. Ver voos disponíveis")
        print("2. Reservar assento")
        print("3. Ver histórico de reservas")
        print("0. Voltar")

        opcao: str = input("Escolha uma opção: ")

        if opcao == "1":
            clear_screen()
            listar_voos()
        elif opcao == "2":
            clear_screen()
            print("[!] Função de reserva ainda em construção.")
        elif opcao == "3":
            clear_screen()
            print("[!] Histórico ainda em construção.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def listar_voos() -> None:
    """
    Exibe a lista de todos os voos com seus destinos.
    """
    print("\n=== VOOS DISPONÍVEIS ===")
    for i, voo in enumerate(voos):
        print(f"{i} - Voo {voo.id_voo} para {voo.destino}")

def ver_destino() -> None:
    """
    Permite consultar o destino de um voo específico.
    """
    listar_voos()
    try:
        idx: int = int(input("\nDigite o número do voo: "))
        voo: Voo = voos[idx]
        print(f"Destino do voo {voo.id_voo}: {voo.destino}")
    except (ValueError, IndexError):
        print("Entrada inválida.")

def ver_tripulacao() -> None:
    """
    Mostra a tripulação completa de um voo.
    """
    listar_voos()
    try:
        idx: int = int(input("\nDigite o número do voo: "))
        voo: Voo = voos[idx]
        print(f"\nTripulação do voo {voo.id_voo}:")
        for membro in voo.tripulacao:
            print(f"{membro.funcao}: {membro.nome} (CPF: {membro.cpf})")
    except (ValueError, IndexError):
        print("Entrada inválida.")

def ver_ocupacao() -> None:
    """
    Mostra a ocupação geral de assentos de um voo.
    """
    listar_voos()
    try:
        idx: int = int(input("\nDigite o número do voo: "))
        voo: Voo = voos[idx]
        voo.relatorio_ocupacao()
    except (ValueError, IndexError):
        print("Entrada inválida.")

def ver_passageiros() -> None:
    """
    Mostra os passageiros alocados em um voo.
    """
    listar_voos()
    try:
        idx: int = int(input("\nDigite o número do voo: "))
        voo: Voo = voos[idx]
        print(f"\nPassageiros do voo {voo.id_voo}:")
        for assento in voo.assentos:
            if assento.ocupado:
                cliente = assento.cliente
                print(f"Assento {assento.numero} - {cliente.nome} (CPF: {cliente.cpf})")
    except (ValueError, IndexError):
        print("Entrada inválida.")

menu_principal()