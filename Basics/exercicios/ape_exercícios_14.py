# -*- coding: utf-8 -*-
"""APE - EXERCÍCIOS 14

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xDeqz1CRETIEWx0-FFVPVwVGBitq1b9P

QUESTÃO 1
"""

#professor

def menor(a,b,c):  #podia estar até em uma biblioteca, elas são internas, não vistas na execução do programa
  if a < b and a < c:
    return a
  else:
    if b < c:
      return b
    else:
      return c

print('Um print simples:')
print(menor(1,2,3))
print()


print('Mais elaborado:')
print('Digite 3 números inteiros: ')
n1 = int(input('1º: '))
n2 = int(input('2º: '))
n3 = int(input('3º: '))
m = menor(n1, n2, n3)
print(f'O menor é: {m}')

"""QUESTÃO 2"""

def fatorial(n): #chama a função
  fat = n #define
  while n-1 != 0: #enquanto o valor inserido -1 for diferente de 0
    fat = fat*(n-1) #esse fatorial vai receber ele(n) multiplicado pelo número anterior a ele
    n = n-1 #esse n agora vai ser ele -1
  return fat #retorne o resultado

print('Digite um número: ') #instrução
n = int(input()) #insira um número
fat = fatorial(n) #pegue a função
print(f'O fatorial de {n} é {fat}') #print o resultado

"""QUESTÃO 3"""

#professor
#função vertical
def vertical(s):
    for letra in s:
        print(letra)

#programa principal
frase = input('Digite uma frase:\n')
print('\nSaída:')
vertical(frase)

"""QUESTÃO 4"""

#professor
def soma(v):
  s = 0 #inicie a variável
  for elem in v: #para cada elemento do vetor  #v é parâmetro (comunicação do programa principal e da função)
    s+= elem #adiciono ele ao soma
  return s #retorne a soma

vetor1 = [1,2,3,4] #vetor já definido #variável globlal se vetor
print(soma(vetor1)) #chama a função e o vetor
vetor2 = [8,7,6,5]
print(soma(vetor2))

print(soma(vetor1), soma(vetor2)) #chamar os dois em um só print

"""QUESTÃO 5"""

def media (n1,n2,n3): #define a media
 return soma(n1,n2,n3)/3

def soma (n1,n2,n3): #define a soma
 return n1+n2+n3

def conceito ():
   if media(n1,n2,n3) < 5: #define a função media entre esses
    return 'C' #chama uma string
   if media(n1,n2,n3) >=5 and media(n1,n2,n3) < 8:
    return 'B'
   if media(n1,n2,n3) >= 8:
    return 'A'

n1 = int(input('1ª nota: ')) #chama as variáveis
n2 = int(input('2ª nota: '))
n3 = int(input('3ª nota: '))
print('Média: ',media(n1,n2,n3)) #média entre essas variáveis
print('Conceito: ',conceito()) #função vazia, pois ele vai receber o resultado dos ifs