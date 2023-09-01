# Tem como somar string e multiplicar elas.
print('Oi' + 'Oi')
print('Oi'*5)
print('='*20)

# Tem como usar o codigo da substituição para difinir quantidade de caracteres que a resposta deve ter colocando {:20}, nesse caso são 20 caracteres.
# Se for digitado algo com menos caracteres que o solicitado, o programa preenche com espaços vazios e podemos escolher onde no espaço a digitação ficara ^ Centralizado, > Direita e < Esquerda. 
# Ex1
n = 'Prazer!'
print('{:20}'.format(n))
print('{:^20}'.format(n))
print('{:>20}'.format(n))
print('{:<20}'.format(n))
# Ex2
n = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}.'.format(n))
print('Prazer em te conhecer {:^20}'.format(n))
print('Prazer em te conhecer {:>20}'.format(n))
print('Prazer em te conhecer {:<20}'.format(n))

# Operações
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
p = n1 ** n2
rq1 = n1 ** 1/2
rq2 = n1 ** 1/3
print('A soma é {}, o produto {} e a divisão {}.'.format(s, m, d))
print('A divisão inteira é {} e o resto da divisão {}.'.format(di, r))
print('A potenciação é {}, a radiciação quadrática do primeiro número {} e a radiciação cúbica do segundo número {:.3f}.'.format(p, rq1, rq2))

# \n : quebra a linha. 
# end= ' ' : define que não é para quebra a linha no final em relação ao proximo print (junta os dois prints).
print('Hoje é segunda feira.', end = ' ')
print('Vou ir a academia.')
print('2 + 2 é \n')
print('4')
















