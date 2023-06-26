print("============= SISTEMA CALCULA MÉDIA ======================")

nota_um = int(input('Digite uma nota: '))
nota_dois = int(input('Digite uma nota: '))
nota_tres = int(input('Digite uma nota: '))


media  = (nota_um + nota_dois + nota_tres)/3 

if media < 5:
  print("====================================================================")
  print(f"O aluno está com média {media} e portanto reprovado!")
  print("====================================================================")
elif media >= 5 and media < 7:
  print("====================================================================")
  print(f"O aluno está com média {media} e portanto  recuperação!")
  print("====================================================================")
else:
  print("====================================================================")
  print(f"O aluno está com média {media} e portanto aprovado!")
  print("====================================================================")

