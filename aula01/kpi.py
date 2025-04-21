nome = input("Olá, qual é o seu nome? ")

salario = input(f"Muito bem, {nome}. Agora me diga o seu salário: ")
salario = float(salario)
bonus = input(f"Entendi, {nome}. R${salario} é um bom salário!\nQual o bônus desejado? ")
bonus = float(bonus)

KPI = 1000 + (salario * bonus)

print(f"Olá {nome}, o seu valor bônus foi de {KPI}.")