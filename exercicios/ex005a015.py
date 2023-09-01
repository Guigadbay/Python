# 005) Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor.
n = int(input('Digite um número inteiro: '))
a = n + 1
b = n - 1 
print('O sucessor do seu numero escolhido é {} e o antecessor {}'. format(a, b))

# 006) Faça um programa que leia um número e mostre o seu dobro, triplo e raiz quadratica.
n = int(input('Digite um número inteiro: '))
a = n * 2
b = n * 3
c = int(n ** (1 / 2))
print('O dobro do seu número escolhido é {}, o tripo {} e a raiz quadrada {}.'.format(a, b, c))

# 007) Faça um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
a = float(input('Digite a sua pimeira nota: '))
b = float(input('Digite a sua segunda nota: '))
media = (a + b) / 2
print('A sua média é: {:.2f}'.format(media))

# 008) Faça um programa que leia um valor em metros e o exiba convertido em centimetros.
n = float(input('Escrave um número em metros: '))
conversao = n * 100
print('Em centimetros, o seu número é: {}'.format(conversao))

# 009) Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número inteio: '))
a = n
b = n * 2
c = n * 3
d = n * 4
e = n * 5
f = n * 6
g = n * 7
h = n * 8
i = n * 9
j = n * 10
print('{} * 1 = {}\n {} * 2 = {}\n {} * 3 = {}\n {} * 4 = {}\n {} * 5 = {}\n {} * 6 = {}\n {} * 7 = {}\n {} * 8 = {}\n {} * 9 = {}\n {} * 10 = {}'.format(n, a, n, b, n, c, n, d, n, e, n, f, n, g, n, h, n, i, n, j))

# 010) Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere 1 dólar = 3.27 reais.
n = float(input('Digite quanto dinehrio você tem em rais na carteira: '))
m = n / 3.27
print('Você pode comprar {:.2f} dólares.'.format(m))

# 011) Faça um programa que leia a largura e altura em metros de uma parede, calcule a sua área e a quantidade de tinta necessária para pintá-la. Considere que cada litro de pinta 2m^2.
l = float(input('Digite a largura em metros da parede: '))
h = float(input('Digite a altura em metros da parede: '))
area = l * h
tinta = area / 5
print('A área da parede é {}m^2 e você precisa de {}L de tinta para poder pintá-la'.format(area, tinta))

# 012) Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
preco = float(input('Digite o valor do produto: '))
desconto = preco * 9.5
print('O valor do seu produto com 5% de desconto, fica: {}'.format(desconto))

# 013) Faça um programa que leia o salário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Digite o seu salário: '))
aumento = sal * 1.15
print('O valor do seu salário com os 15% de aumento, fica: {}'.format(aumento))

# 014) Faça um programa que leia a temperatura em ºC e transforme em ºF.
c = float(input('Digite a temperatura em ºC: '))
f = c * 1.8 + 32
print('A temperatura {}ºC vale {}ºF.'.format(c, f))

# 015) Faça um programa que leia a quantidade de Km percorridos por um carro alugado e de dias pelos quais ele foi alugado e calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0,15 reais por km rodado.
km = float(input('Quantos km você percorreu com o carro? '))
d = int(input('Quantos dias você alugou o carro: '))
total = (km * 0.15) + (d * 60)
print('O total a pagar pelo aluguel do carro é: {}'.format(total))





