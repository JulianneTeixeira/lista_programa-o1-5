nome = input("Nome:")
salario_bruto = float(input("Digite o salário bruto:"))
valor_imposto = float(input("Digite o valor do imposto:"))
salario_liquido = salario_bruto - valor_imposto
print(f"Nome: {nome}")
print(f"Salário Líquido: R$ {salario_liquido}")
