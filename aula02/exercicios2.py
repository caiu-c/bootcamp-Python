
def VerificaInteiro(n1, n2):

    while True:
        try: 
            n1, n2 = int(n1), int(n2)

            return n1, n2
        except:
            print("\n")
            print("Por favor, digite dois números inteiros.")
            print("Exemplo: 1, 2, 3, 4, 5")
            print("Não digite números quebrados como 9.2, nem letras 'A, B, C, D'")
            print("\n")
            print("Vamos tentar dnv")

            n1 = input('Digite o 1° n° novamente: ')
            n2 = input('Digite o 2° n° novamnete: ')

def VerificaFloat(n1, n2):

    while True:
        try: 
            n1, n2 = float(n1), float(n2)

            return n1, n2
        except:
            print("\n")
            print("Por favor, digite dois números quaisquer.")
            print("Exemplo: 1, 2.5, 3, 4.2, 522.1")
            print("Não digitee letras 'A, B, C, D'")
            print("\n")
            print("Vamos tentar dnv")

            n1 = input('Digite o 1° n° novamente: ')
            n2 = input('Digite o 2° n° novamnete: ')

# 1. Soma de dois números inteiros inseridos pelo usuário.
# n1 = input('Digite o 1° n° a ser somado: ')
# n2 = input('Digite o 2° n° a ser somado: ')

# n1, n2 = VerificaInteiro(n1, n2)
# soma = n1 + n2
# print(f"{n1} + {n2} = {soma}")

# 2. Resto da divisão entre dois números inteiros
# n3 = input('Digite o 1° n° a ser dividido por 5: ')

# n3, n4 = VerificaInteiro(n3, 5)
# resto = n3 % 5
# print(f"O resto da divisão {n3} / {5} = {resto}")

# Programa que multiplica 2 números

# n5 = input('Digite o 1° n° a ser multiplicado: ')
# n6 = input('Digite o 2° n° a ser multiplicado: ')
# n5, n6 = VerificaInteiro(n5, n6)

# resultado = n5 * n6

# print(f"Resultado = {resultado}")

# 4. Programa que divide 2 números

# n7 = input('Digite o 1° n° a ser dividido: ')
# n8 = input('Digite o 2° n° a ser dividido: ')
# n7, n8 = VerificaInteiro(n7, n8)

# divisao_inteira = n7 // n8

# print(f"Resultado = {divisao_inteira}")

# 5. Programa que calcula quadrado

# n9 = input('Digite o 1° n° a ser elevado ao quadrado: ')
# n9 = float(n9)
# quadrado = n9**2

# print(f"Resultado = {quadrado}")

# 6. Adição de dois floats

# n10 = input('Digite o 1° n° a ser somado: ')
# n11 = input('Digite o 2° n° a ser somado: ')

# n10, n11 = VerificaFloat(n10, n11)

# soma2 = n10 + n11

# print(f"O resultado = {soma2}")

# 7. Média 

# n12 = input('Digite o 1° n°: ')
# n13 = input('Digite o 2° n°: ')

# n12, n13 = VerificaFloat(n12, n13)

# media = (n12 + n13) / 2

# print(f"O resultado = {media}")

# 8. Potência

# n14 = input('Digite o 1° n°: ')
# n15 = input('Digite o 2° n°: ')

# n14, n15 = VerificaFloat(n14, n15)

# pot = n14 ** n15

# print(f"O resultado = {pot}")

# 9. Celsius to Fahrenheit

# n16 = float(input('Digite a temperatura em celsius: '))



# F = (n16 * 1.8) +  32

# print(f"{n16}°C é = {F}°F")

# 10. área do círculo 
# from math import pi

# n17 = float(input("Digite o raio: "))

# area = pi * n17 ** 2

# print(f"A área do círcula de raio {n17} = {area:.2f}m²")

# 11. String convert to UPPERCASE

palavra = input("Digite aqui sua string: ")

palavra = palavra.upper()

print(palavra)