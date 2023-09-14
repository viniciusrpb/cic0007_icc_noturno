n = input() # leitura de uma linha da entrada
n = int(n)  # converte n (string) para inteiro
'''n = int(input())'''
resto = n % 2  # resto da divisao de n por 2
if resto == 0:
    # comandos executados caso comparacao seja True
    print('par')
else:
    # se o resto for diferente de zero
    print('impar')

print('fim')
