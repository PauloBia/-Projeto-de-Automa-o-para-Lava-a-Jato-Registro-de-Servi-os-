# Projeto de Automação para Lava a Jato Registro de Serviços]

servicosGerais_lista = (
    '[1] Cadastro de Cliente e Veículo',
    '[2] Registro de Serviço',
    '[3] Cálculo de Custos',
    '[4] Histórico de Serviços',
    '[5] Relatórios Simples',
    '[6] Interface de Usuário',
    '[7] Armazenamento de Dados'
)
servicosGerais = int(input('Digite qual serviço você quer executar: '))
# Cadrasto do cliente

nome = str(input('Digite seu nome completo: '))
telefone = int(input('Digite seu número de telefone (COM DDD e sem espaçamento):'))
veiculo = str(input('Digite o modelo do seu veículo: '))

# Registro de serviço

servicos = (
    '[1] Lavagem simples 35,00',
    '[2] Enceramento 40,00',
    '[3] Lavagem detalhada de 50,00 por 35,00',
    '[4] Polimento de faróis 90,00',
    '[5] Cristalização de vidros 50,00',
    '[6] Limpeza técnica de motor 180,00',
    '[7] Higienização interna 350,00'
)
print(servicos)
escolha_servico = int(input('Digite o número correspondente do serviço: '))

# Calculo de custos
recibo = float(input('Digite o valor do pagamento: '))

pagamento_lavagemSimples = recibo - 35.00
pagamento_enceramento = recibo - 40.00
pagamento_lavagemDetalhada = recibo - 35.00
pagamento_polimentoFarois = recibo - 90.00
pagamento_cristalizacaoVidros = recibo - 50.00
pagamento_limpezaTecnicaMotor = recibo - 100.00
pagamento_higienizacaoInterna = recibo - 350.00

if escolha_servico == 1:
    print(f'Seu troco será de {pagamento_lavagemSimples}')

elif escolha_servico == 2:
    print(f'Seu troco será de {pagamento_enceramento}')

elif escolha_servico == 3:
    print(f'Seu troco será de {pagamento_lavagemDetalhada}')

elif escolha_servico == 4:
    print(f'Seu troco será de {pagamento_polimentoFarois}')

elif escolha_servico == 5:
    print(f'Seu troco será de {pagamento_cristalizacaoVidros}')

elif escolha_servico == 6:
    print(f'Seu troco será de {pagamento_limpezaTecnicaMotor}')

elif escolha_servico == 7:
    print(f'Seu troco será de {pagamento_higienizacaoInterna}')

else:
    print('Opção inválida, tente novamente')
