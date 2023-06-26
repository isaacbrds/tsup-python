print("============= SISTEMA CALCULA MÉDIA ======================")

numero = int(input('Digite um numero para calcular sua tabuada: '))
iterador = int(input('Digite um numero para ser o iterador de sua tabuada: '))
print("====================================================================")
print("========================= TABUADA ==================================")
contador = 1

while contador <= iterador:
  print(f"{contador} X {numero} = { contador * numero}")
  contador += 1
  
