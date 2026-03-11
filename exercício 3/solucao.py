salario_minimo = float(input("Coloque quanto vale o salário mínimo nos dias de hoje: "))
agua = float(input("Coloque o quanto de água foi consumida no mês, em litros: "))

valor_1000 = salario_minimo * 0.02
blocos = agua / 1000
valor_conta = blocos * valor_1000
valor_desconto = valor_conta * 0.85

print("O valor da conta vai ser de",valor_conta)
print("O valor da conta com desconto é de",valor_desconto)