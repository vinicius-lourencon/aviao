
from typing import List
from entidades.cliente import Cliente
from entidades.voo import Voo
from entidades.assento import Assento
from pagamento.pagamento import Pagamento
from pagamento.forma_pagamento import FormaPagamento
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
clientes: List[Cliente] = []

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
        print("=== MENU PRINCIPAL ===")
        print("1. Acessar como Cliente")
        print("2. Acessar como Administrador")
        print("3. Visualizar Voos (modo leitura)")
        print("4. Sair")

        opcao: str = input("Escolha uma opção: ")

        if opcao == "1":
            clear_screen()
            menu_cliente()
        elif opcao == "2":
            clear_screen()
            menu_administrador()
        elif opcao == "3":
            clear_screen()
            menu_visualizacao()
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
        print("=== VISUALIZAÇÃO DE VOOS ===")
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
            clear_screen()
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
            clear_screen()
            break
        else:
            print("Opção inválida.")
#menu cliente
def menu_cliente() -> None:
    """
    Menu destinado ao cliente, com opções de consulta e reserva de assentos.
    """
    while True:
        print("=== MENU CLIENTE ===")
        print("1. Ver voos disponíveis")
        print("2. Reservar assento")
        print("3. Ver histórico de reservas")
        print("4. Fazer Cadastro")
        print("0. Voltar")

        opcao: str = input("Escolha uma opção: ")

        if opcao == "1":
            clear_screen()
            listar_voos()
        elif opcao == "2":
            clear_screen()
            reservar_assento()
        elif opcao == "3":
            clear_screen()
            ver_historico_cliente()
        elif opcao == "4":
            clear_screen()
            cadastrar_cliente()
        elif opcao == "0":
            clear_screen()
            break
        else:
            print("Opção inválida.")

def listar_voos() -> None:
    """
    Exibe a lista de todos os voos com seus destinos.
    """
    print("=== VOOS DISPONÍVEIS ===")
    for i, voo in enumerate(voos):
        print(f"{i} - Voo {voo.id_voo} para {voo.destino}")

def ver_destino() -> None:
    """
    Permite consultar o destino de um voo específico.
    """
    listar_voos()
    try:
        idx: int = int(input("Digite o número do voo: "))
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
        idx: int = int(input("Digite o número do voo: "))
        voo: Voo = voos[idx]
        print(f"Tripulação do voo {voo.id_voo}:")
        for membro in voo.tripulacao:
            print(f"{membro.funcao}: {membro.nome} (CPF: {membro.cpf})")
    except (ValueError, IndexError):
        print("Entrada inválida.")

def ver_ocupacao() -> None:
    """
    Exibe todos os assentos de um voo com indicação visual de ocupação.
    """
    listar_voos()
    try:
        idx: int = int(input("Digite o número do voo: "))
        voo: Voo = voos[idx]

        print(f"=== Ocupação dos assentos no voo {voo.id_voo} para {voo.destino} ===")

        for assento in voo.assentos:
            status = "LIVRE" if not assento.ocupado else "OCUPADO"
            print(f"[{assento.numero:03}] {status}")

        ocupados = sum(1 for a in voo.assentos if a.ocupado)
        livres = 250 - ocupados
        print(f"Resumo: {ocupados} ocupados | {livres} livres")

    except (ValueError, IndexError):
        print(" Entrada inválida.")

def ver_passageiros() -> None:
    """
    Mostra os passageiros alocados em um voo.
    """
    listar_voos()
    try:
        idx: int = int(input("Digite o número do voo: "))
        voo: Voo = voos[idx]
        print(f"Passageiros do voo {voo.id_voo}:")
        for assento in voo.assentos:
            if assento.ocupado:
                cliente = assento.cliente
                print(f"Assento {assento.numero} - {cliente.nome} (CPF: {cliente.cpf})")
    except (ValueError, IndexError):
        print("Entrada inválida.")

def reservar_assento() -> None:
    """
    Permite que o usuário escolha um voo e reserve um assento para um cliente já cadastrado.
    Realiza o pagamento da reserva e registra no histórico do cliente seja recusado ou aprovado.
    """
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente antes de continuar.")
        return

    listar_voos()

    try:
        idx_voo: int = int(input("Escolha o número do voo para reserva: "))
        voo: Voo = voos[idx_voo]
    except (ValueError, IndexError):
        print(" Voo inválido.")
        return

    # Seleciona cliente
    print("=== Clientes Cadastrados ===")
    for i, c in enumerate(clientes):
        print(f"[{i}] {c.nome} | CPF: {c.cpf}")
    try:
        idx_cliente: int = int(input("Escolha o cliente pelo número: "))
        cliente: Cliente = clientes[idx_cliente]
    except (ValueError, IndexError):
        print(" Cliente inválido.")
        return

    # Mostra assentos
    print("=== Assentos Disponíveis ===")
    for i, assento in enumerate(voo.assentos, start=1):
        status = "X" if assento.ocupado else str(assento.numero)
        print(f"{status:>3}", end="  ")
        if i % 10 == 0:
            print()
    print()

    try:
        numero_escolhido: int = int(input("Digite o número do assento desejado: "))
    except ValueError:
        print(" Número inválido.")
        return

    assento_encontrado = next((a for a in voo.assentos if a.numero == numero_escolhido), None)

    if not assento_encontrado:
        print("Assento não encontrado.")
        return

    if assento_encontrado.ocupado:
        print("Esse assento já está ocupado.")
        return

    # metodo de pagamento
    print("=== Escolha a forma de pagamento ===")
    for i, forma in enumerate(FormaPagamento):
        print(f"[{i}] {forma.value}")
    try:
        idx_pag = int(input("Forma de pagamento: "))
        forma_escolhida = list(FormaPagamento)[idx_pag]
    except (ValueError, IndexError):
        print("Opção inválida.")
        return

    pagamento = Pagamento(forma_escolhida)
    sucesso = pagamento.realizar_pagamento(voo.preco)

    # Associa cliente e pag ao assento
    assento_encontrado.reservar(cliente)
    assento_encontrado.pagamento = pagamento 

    # Add no historico do cliente
    cliente._historico_reservas.append({
    "voo": voo.id_voo,
    "assento": assento_encontrado.numero,
    "status": pagamento.status.value,
    "data": pagamento.data_transacao.strftime("%d/%m/%Y %H:%M:%S")
    })

    # Mensagem final
    print("=== Resultado da Reserva ===")
    if sucesso:
        print(f"Reserva confirmada para {cliente.nome} no assento {numero_escolhido}.")
    else:
        print(f"Pagamento recusado. Mesmo assim, reserva registrada no histórico com status de pagamento.")
    print(str(pagamento))
    print()
        
def ver_historico_cliente() -> None:
    """
    Permite consultar o histórico de reservas de um cliente a partir do CPF.
    """
    cpf: str = input("Digite o CPF do cliente: ")

    for voo in voos:
        for assento in voo.assentos:
            if assento.ocupado and assento.cliente.cpf == cpf:
                print(f"Reserva encontrada:")
                print(f"Nome: {assento.cliente.nome}")
                for r in assento.cliente.reservas:
                    print(f"- Voo {r['voo']} para {r['destino']} - Assento {r['assento']}")
                return

    print("Nenhum histórico encontrado para esse CPF.")

def cadastrar_cliente() -> None:
    """
    Cadastra um novo cliente no sistema.
    """
    print("=== Cadastro de Cliente ===")
    nome: str = input("Nome completo: ")
    cpf: str = input("CPF (apenas números): ")
    data_nasc: str = input("Data de nascimento (DD/MM/AAAA): ")

    from entidades.cliente import Cliente
    from uuid import uuid4

    id_ = str(uuid4())[:8]
    novo_cliente = Cliente(nome, cpf, id_, data_nasc)
    clientes.append(novo_cliente)

    print(f" Cliente {nome} cadastrado com sucesso!\n")

menu_principal()