print("============= SISTEMA PEGA NÚMEROS ======================")

numero_um = int(input('Digite um número: '))
numero_dois = int(input('Digite um número: '))
numero_tres = int(input('Digite um número: '))
numero_quatro = int(input('Digite um número: '))

soma_dois_primeiros = numero_um + numero_quatro 
multiplica_dois_do_meio = numero_dois * numero_tres

resultado = soma_dois_primeiros + multiplica_dois_do_meio

if resultado > 100:
  print("====================================================================")
  print(f"O resultado alcançado foi {resultado} parabéns")
  print("====================================================================")
else:
  print("====================================================================")
  print(f"O resultado alcançado foi {resultado} e ficou abaixo da expectativa")
  print("====================================================================")

