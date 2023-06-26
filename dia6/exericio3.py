import os
import time
print("============= SISTEMA DE MENU ======================")

contador = 1
while True:
  print("============= SISTEMA DE MENU ======================")
  
  opcao = int(input("Digite sua opção: \n 1- execute a tabuada \n 2 - Execute a Tabuada com Iterador \n 3 - Saia do programa \n"))
  
  if opcao == 1:
    numero = int(input('Digite um numero para calcular sua tabuada: '))    
    print("========================= TABUADA ==================================")
    while contador <= 10:
      print(f"{contador} X {numero} = { contador * numero}")
      contador += 1
  elif opcao == 2:
    numero = int(input('Digite um numero para calcular sua tabuada: '))
    iterador = int(input('Digite um numero para ser o iterador de sua tabuada: '))
    while contador <= iterador:
      print(f"{contador} X {numero} = { contador * numero}")
      contador += 1
  else:
    print("========================= ATE MAIS ================================== ")
    break
  
  time.sleep(3)
  os.system("clear")
  