# -*- coding: utf-8 -*-
"""APE - EXERCÍCIOS 6

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17lQa87qSHiLbqPXeRuEagCF93LWzn2mq

QUESTÃO 1
começa com u1 pq é menor ou igual, só o menor seria 0
"""

quant = 30
cont = 1
soma = 0
while cont <= quant:
  n = int(input())
  soma = soma + n
  cont = cont + 1
print('Soma =', soma)

"""QUESTÃO 2"""

soma = 0
cont = 0
n = int(input('Digite um número inteiro: '))
while n != 999:
 cont = cont + 1
 soma = soma + n
 n = int(input('Digite um número interiro: '))
media = soma/cont
print(f'A média entre os números é {media:.1f}')

flag = 999
soma = 0
cont = 0
print('Digite vários números.')
print(f'Para finalizar digite {flag}.')
n = int(input('Digite um número inteiro: '))
while n != flag:
 cont = cont + 1
 soma = soma + n
 n = int(input('Digite um número interiro: '))
media = soma/cont
print(f'A média entre os números é {media:.1f}')

soma = 0
cont = 0
n = int(input('Digite um número inteiro: '))
while n != 999:
 cont = cont + 1
 soma = soma + n
 n = int(input('Digite um número inteiro: '))
media = soma/cont
print(f'A média entre os números é {media:.1f}')

"""QUESTÃO 3"""

flag = 0
print('Digite vários números.')
n = int(input('Digite um número inteiro: '))
maior = n
menor = n
while n != flag:
 if n > maior:
    maior = n
 if n < menor:
   menor = n
 n = int(input('Digite um número inteiro: '))
print(f'{maior}, {menor}')

"""QUESTÃO 4"""

flag = 0
print(f'Informe os dados dos alunos. Para encerrar, digite a matrícula {flag}.')
mat = int(input('\nMatrícula: '))
while mat != flag:
    nome = input('Nome: ')
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    if media >= 7.0:
        sit = 'Aprovado'
    else:
        sit = 'Reprovado'
    print(f'\nMatrícula: {mat}')
    print(f'Nome: {nome}')
    print(f'Média: {media:.1f}')
    print(f'Situação: {sit}')
    mat = int(input('\nMatrícula: '))
print('Fim do programa.')

flag = 0
print(f'Informe os dados dos alunos. Para encerrar, digite a matrícula {flag}')
matricula = int(input('Digite o número da sua matrícula: '))
while matricula != flag:
 nome = input('Digite seu nome: ')
 nota1 = float(input('Digite sua primeira nota: '))
 nota2 = float(input('Digite sua segunda nota: '))
 if (nota1 + nota2/2) >= 7:
  media = 'aprovado'
 else:
  media = 'reprovado'
 print()
 print(f'Nome: {nome}')
 print(f'Matrícula: {matricula}')
 print(f'1º Nota: {nota1}')
 print(f'2º Nota: {nota2}')
 print(f'Situação: {media}')
 print()
 matricula = int(input('Digite o número da sua matrícula: '))
print('Fim do programa.')

"""QUESTÃO 5
a parte de controle é por pergunta não flag
"""

pergunt = 'sim'
while pergunt == 'sim':
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
       print('par')
    else:
       print('ímpar')
    pergunt = input('Você desje continuar (sim/não)? ').lower()
    print()
print('Fim do programa.')

resp = 'S'
while resp == 'S':
  num = int(input('Digite um número inteiro: '))
  if num % 2 == 0:
    print('par')
  else:
    print('ímpar')
  resp = input('Deseja continuar(S/N?').upper()
  print()
print('Fim do programa.')

"""QUESTÃO 6"""



"""QUESTÃO 7
ler vários números
zero é o flag
média
porcentagem = o específico pelo geral
o menor
"""

flag = 0
print(f'Informe as idades, para encerrar digite: {flag}')
idade = int(input('Digite a idade do visitante: '))
cont = 0
soma = 0
menor = idade
total

while idade != flag:
 if idade < menor:
  menor = idade
 if idade <= 21 and idade >= 18:
 media = soma/cont+1

 idade = int(input('Digite a idade do visitante: '))
 print()
print('Fim do programa.')

"""QUESTÃO 8
ler vários intens
x para
"""

flag = 'x'
cod = 0
soma = 0
qtd = 0
valor = 0

cod = input('Digite o código correspondente: ')
qtd = int(input('Digite a quantidade desejada: '))

while cod != flag:
  if cod == 'H':
   valor = qtd * 5
  elif cod =='C':
   valor = qtd * 6
  elif cod == 'B':
   valor = qtd * 7
  else:
   valor = qtd * 4
  soma = soma + valor
  cod = input('Digite o código correspondente: ')
print(soma)

flag = 'x'
soma = 0
codigo = input('código:').upper()
while codigo != flag:
  quant = int(input('Quatidade: '))
  if codigo == 'H':
   valor = 5
  elif codigo =='C':
   valor = 6
  elif codigo == 'B':
   valor = 7
  else:
   valor = 4
  soma = soma + (quant * valor)
  codigo = input('código:').upper()
print(f'O total a pagar: R${soma:.2f}')