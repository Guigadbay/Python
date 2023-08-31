# Print!
print('Olá, mundo!')
print(2 + 3)
print('2 + 3')
print('2' + '3')
print('O resultado da soma de 2 + 3 é:', 2 + 3)

# Matemática!
print(10*(5 + 7)/4)
print(10*(5 + 7/4))

# Dados e Variáveis!
nota = 10
disciplina = 'Lógica de Progamação e Algoritimos'
print(nota)
print(disciplina)
print(nota, disciplina)

# Comparação!
a = 1
b = 4
resposta1 = a == b
print(resposta1)
resposta2 = a != b
print(resposta2)

# Soma e Multiplicação!
# Tem como fazer soma de caracteres.
s1 = 'Logica de Progamação'
s1 = s1 + ' e Algoritimos'
print(s1)
# Tem como multiplicar um caractere.
s1 = 'A ' + '#' * 10 + ' B'
print(s1)

# Composição!
# Tem como colocar o valor de uma variavel dentro de uma outra variavel.
nota = 8.5
disciplina = 'Algoritimos'
s1 = 'Você tirou {} na disciplica de {}' .format(nota, disciplina)
print(s1)

# Fatiamento!
# Dá para printar somente algumas partes de uma variavel, colocando por exemplo print(s1[0:6]), sendo 0 o primenro caractere e 6 o quinto caractere, ou assim print(s1[:6]) o progama ja entende que tem que colocar do 0 ao quinto caractere.
s1 = 'Lógica de Progamação e Algorítimos'
print(s1[0:6])
print(s1[:6])
print(s1[24:34])

# Tamanho!
# Tem como descobri quantos caracteres tem uma variavel. Cria-se uma variavel e da o valor de les(variavel que quer descobrir o tamanhor) e pede para printar.
s1 = 'Lógica de Progamação e Algorítimos'
tamanho = len(s1)
print(tamanho)
