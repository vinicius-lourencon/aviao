
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
            
#menu adm
def menu_administrador() -> None:
    """
    Menu do administrador com acesso a funções de leitura do sistema.
    """
    while True:
        clear_screen()
        print("\n=== MENU ADMINISTRADOR ===")
        print("1. Listar todos os voos")
        print("2. Ver tripulação de um voo")
        print("3. Ver ocupação de um voo")
        print("0. Voltar ao menu principal")

        opcao: str = input("Escolha uma opção: ")

        if opcao == "1":
            clear_screen()
            #listar_voos()
        elif opcao == "2":
            clear_screen()
            #ver_tripulacao()
        elif opcao == "3":
            clear_screen()
            #ver_ocupacao()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
