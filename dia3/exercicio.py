print("============= SISTEMA DE COMBUSTÍVEIS ======================")
quantidade_do_tanque_do_posto = input('Digite a quantidade total de litros do tanque: ')
quantidade_a_abastecer_no_posto = input('Digite a quantidade de litros a abastecer: ')

quantidade_apos_abastecimento = int(quantidade_do_tanque_do_posto) + int(quantidade_a_abastecer_no_posto)
print(f'A quantidade de litros que ficou no posto foi: {quantidade_apos_abastecimento}')

print("Chegou cliente bora vender?")

nome = input('Olá senhor qual o seu nome? ')
valor_combustivel = int(input(f'Qual o valor que o senhor(a) {nome} deseja colocar? '))

resultado = quantidade_apos_abastecimento - valor_combustivel

porcentagem = float(quantidade_apos_abastecimento - valor_combustivel)/100

print(f'O posto ficou com {resultado} no tanque do posto após retirada de {valor_combustivel} litros')
print(f'O posto ficou com {porcentagem*100:.0f}% de sua capacidade ')
