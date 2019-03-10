'''
EXERCICIO:
FaÃ§a um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela estÃ¡ apta a ser do Exercito
Para entrar no exercito Ã© preciso ter mais de 18 anos
pesar mais ou igual  60 kilos
e medir mais ou igual 1,70 metros
'''

idade = int(input('Escreva sua idade: '))
peso = float(input('Escreva seu peso: '))
altura = float(input('Escreva sua altura: '))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Voce esta apto a servir o exercito')
else:
    print('Voce nao esta apto')
