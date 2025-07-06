
# ✈️ Sistema de Reserva de Voos

Este projeto simula um sistema orientado a objetos de reserva de voos, com funcionalidades de cadastro de clientes, reserva de assentos, geração de tripulação e passageiros com dados realistas, além de um sistema de pagamento integrado.

## 📁 Estrutura do Projeto

```
projeto_reserva_voo/
│
├── main.py                      # Arquivo principal com menus e execução
├── gerador.py                   # Gera passageiros e tripulação com Faker
│
├── entidades/
│   ├── cliente.py               # Classe Cliente com histórico de reservas
│   ├── tripulacao.py            # Classe Tripulante
│   ├── pessoa_base.py           # Classe base para Cliente e Tripulante
│   ├── voo.py                   # Classe Voo com assentos, destino e ID
│   ├── assento.py               # Classe Assento com reserva e status
│
├── pagamento/
│   ├── pagamento.py             # Lógica do pagamento e status
│   ├── forma_pagamento.py       # Enum com tipos de pagamento (PIX, Crédito, Débito)
│   ├── status_pagamento.py      # Enum com status do pagamento (Aprovado, Recusado, Pendente)
```

## ✅ Funcionalidades

- 📌 **Menu Principal** com acesso a menus específicos:
  - Administrador
  - Cliente
  - Visualizações

- 👤 **Menu Cliente**:
  - Cadastro de novo cliente
  - Consulta de voos disponíveis
  - Reserva de assentos com pagamento (PIX, Crédito ou Débito)
  - Histórico de reservas (aprovadas ou recusadas)

- 🧑‍✈️ **Geração automática** de passageiros e tripulação com dados realistas (nome, CPF, data de nascimento, função etc.)

- 💳 **Sistema de pagamento**:
  - Simulação de pagamento com formas variadas
  - Registro de status (aprovado ou recusado)
  - Armazenamento da transação no assento e no cliente

- 📊 **Relatórios administrativos**:
  - Visualização de voos por destino
  - Relatório de ocupação dos assentos
  - Listagem de todos os clientes e tripulantes

## 🧪 Tecnologias utilizadas

- **Python 3.11+**
- **Faker** (para gerar dados realistas)
- Tipagem estática com `mypy` friendly (`List`, `Dict`, etc.)
- Modularização clara em pacotes `entidades/` e `pagamento/`

## 🚀 Como executar

1. Clone o repositório:

```bash
git clone https://github.com/vinicius-lourencon/aviao.git
cd aviao
```

2. Instale a dependência Faker:

```bash
pip install faker
```

3. Execute o sistema:

```bash
python main.py
```

## 💡 Exemplo de fluxo

1. Cadastre um novo cliente no menu "Cliente"
2. Visualize voos disponíveis
3. Selecione um voo e tente reservar um assento
4. Escolha a forma de pagamento
5. Veja o resultado da transação e o histórico de reservas

## 📌 Observações

- Todos os voos têm 250 assentos.
- O sistema mostra os assentos disponíveis com destaque para os já ocupados.
- O histórico do cliente é salvo mesmo se o pagamento for recusado.
- O terminal é limpo automaticamente após cada escolha de menu para melhor visualização.

## 🤝 Contribuição

Contribuições são bem-vindas! Sugestões, melhorias de código ou funcionalidades adicionais podem ser discutidas e enviadas via pull request ou issue.
