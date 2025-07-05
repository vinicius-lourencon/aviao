
from entidades.voo import Voo
from entidades.assento import Assento
from gerador import gerar_cliente_faker, gerar_tripulante_faker
import random

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

print(" Todos os voos foram criados com sucesso!")