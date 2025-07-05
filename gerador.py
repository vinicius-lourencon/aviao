from faker import Faker
import random
from entidades.cliente import Cliente
from entidades.tripulacao import Piloto, Copiloto, Comissario
from typing import Union

fake = Faker('pt_BR')

def gerar_cliente_faker() -> Cliente:
    """
    Gera um cliente fictício com dados realistas usando a biblioteca Faker.
    """
    nome = fake.name()
    cpf = fake.cpf()
    id_cliente = f"CL{random.randint(1000, 9999)}"
    data_nasc = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%d/%m/%Y')
    return Cliente(nome, cpf, id_cliente, data_nasc)


def gerar_tripulante_faker(funcao: str) -> Union[Piloto, Copiloto, Comissario]:
    """
    Gera um tripulante fictício com dados realistas para a função escolhida.

    """
    nome = fake.name()
    cpf = fake.cpf()
    id_trip = f"T{random.randint(1000, 9999)}"
    data_nasc = fake.date_of_birth(minimum_age=30, maximum_age=65).strftime('%d/%m/%Y')

    match funcao.lower():
        case "piloto":
            return Piloto(nome, cpf, id_trip, data_nasc)
        case "copiloto":
            return Copiloto(nome, cpf, id_trip, data_nasc)
        case "comissario":
            return Comissario(nome, cpf, id_trip, data_nasc)
        case _:
            raise ValueError("Função inválida para tripulante.")