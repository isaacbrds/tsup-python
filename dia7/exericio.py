print("============= SISTEMA CALCULA MÉDIA ======================")

alunos = []
quantidade_de_alunos = int(input('Digite a quantidade de alunos: '))

for contador in range(quantidade_de_alunos):
  nome = input(' Digite o nome do Aluno: ')
  alunos.append(nome)

media = []

for contador in range(quantidade_de_alunos):
  print(f'Dados do aluno {alunos[contador]}')
  nota_um = int(input('Digite uma nota: '))
  nota_dois = int(input('Digite uma nota: '))
  nota_tres = int(input('Digite uma nota: '))
  media.append( (nota_um + nota_dois + nota_tres)/3 ) 

for contador in range(quantidade_de_alunos):
  if media[contador] < 5:
    print("====================================================================")
    print(f"O aluno: {alunos[contador]}\n está com média: {media[contador]:.2f}\n e com Situação: Reprovado!")
    print("====================================================================")
  elif media[contador] >= 5 and media[contador] < 7:
    print("====================================================================")
    print(f"O aluno: {alunos[contador]}\n está com média: {media[contador]:.2f}\n e com Situação: em Recuperação!")
    print("====================================================================")
  else:
    print("====================================================================")
    print(f"O aluno: {alunos[contador]}\n está com média: {media[contador]:.2f}\n e com Situação: em Aprovado!")
    print("====================================================================")

