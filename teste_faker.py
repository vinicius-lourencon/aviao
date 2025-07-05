from gerador import gerar_cliente_faker, gerar_tripulante_faker

cliente = gerar_cliente_faker()
print(f"[CLIENTE] Nome: {cliente.nome}, CPF: {cliente.cpf}, Nasc: {cliente.data_nasc}")

tripulante = gerar_tripulante_faker("piloto")
print(f"[TRIPULANTE] Nome: {tripulante.nome}, Função: {tripulante.funcao}, CPF: {tripulante.cpf}")