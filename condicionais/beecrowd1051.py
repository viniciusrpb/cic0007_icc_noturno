salario = float(input())

#verifica a faixa de renda do salario lido da entrada
if salario > 4500.00:
    resto = salario - 4500.00
    # eh garantido que sera cobrado imposto em todas as faixas de renda
    # detalhamento:
    # valor restante acima de 4500 = resto do valor, taxa eh 28%
    # 3000 - 4500 = 1500, taxa eh 18%
    # 2000 - 3000 = 1000, taxa eh 8%
    irpf = resto*0.28 + 1500.00*0.18 + 1000.00*0.08
    print(f'R$ {irpf:.2f}')
elif salario > 3000.00:
    resto = salario  - 3000.00
    # eh garantido que sera cobrado imposto nas faixas
    # detalhamento:
    # valor restante acima de 3000.00 = resto do valor, taxa eh 18%
    # 2000 - 3000 = 1000, taxa eh 8%
    irpf = resto*0.18 + 1000*0.08
    print(f'R$ {irpf:.2f}')
elif salario > 2000.00:
    resto = salario - 2000.00
    # eh garantido que sera cobrado imposto apenas no valor que excede 2000
    irpf = resto*0.08
    print(f'R$ {irpf:.2f}')
else:
    print('Isento')

