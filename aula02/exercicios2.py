import sys

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

# palavra = input("Digite aqui sua string: ")

# palavra = palavra.upper()

# print(palavra)

# 12. Recebe o nome completo do user e retorna todo lowercase()

# nome_user = input("Digite o seu nome completo: ")

# nome_user_lower = nome_user.lower()

# print(nome_user_lower)

# 13. Recebe uma frase e aplica um trim/clean

# frase = input("Digite uma frase com espaços no começo e no fim:")

# frase_trim_clean = frase.strip()

# print(f"Essa é a frase com espaços {frase}!")
# print(f"Essa é a frase sem espaços {frase_trim_clean}!")

# 14. Recebe string no formato dd/mm/aaa e retorna separadamente o dia, o mês e o ano

# interesse = ["Dia", "Mês", "Ano"]

# data = input("Digite a data no formato dd/mm/aaaa: ")

# elementos = data.split("/")


# completo = dict(zip(interesse, elementos))


# for chave, valor in (completo.items()):

#     print(f"{chave}: {valor}")

# 15. Concatenar duas strings

# string1 = input("String 1: ")
# string2 = input("String 2: ")

# string3 = string1+string2

# print(string3)

# verdade = ['verdade', 'v', 'verdadeiro', 'sim', 's', 'si', 'sí','true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']
# 16. AND
# bln1 = (input("Digite uma empressao booleana: "))
# bln2 = (input("Digite uma empressao booleana: "))

# bln1 = bln1.lower() in verdade
# bln2 = bln2.lower() in verdade

# result_and = (bln1 and bln2)
# print(f"O resultado da operação AND entre {bln1} e {bln2} é {result_and}")

# 17. OR
# result_or = bln1 or bln2
# print(f"O resultado da operação OR entre {bln1} e {bln2} é {result_or}")
# 18. NOT
# invert_first = not(bln1)
# print(f'A inversão de {bln1} é {invert_first}')

# 19. TWO equal numbers
# n18 = input('Digite o 1° n°: ')
# n19 = input('Digite o 2° n°: ')

# n18, n19 = VerificaFloat(n18, n19)

# iguais_ = n18 == n19

# if iguais_:
#     print(f'O n° {n18} é igual ao n° {n19}! ')
#     print(iguais_)
# 20. Diff
# else:
#     print(f'O n° {n18} é diferente do {n19} :( ')
#     print(iguais_)


# 21. Conversor de temperatura

# graus_celsius = input("Digite a temperatura em °C [Digite 'exit' para sair]: ")

# controle = 0
# while True:

#     if graus_celsius.lower() == 'exit':
#         print("Programa finalizado pelo usuário" )
#         break

#     try:
#         graus_celsius = float(graus_celsius)
#         graus_f = graus_celsius * 1.8 + 32
#         controle = 0


#     except ValueError as e:
#         print(f"{e}")
#         controle = 1

#     finally:
#         if controle == 0:
#             print(f"A °C {graus_celsius} = °F {graus_f} ")
#             print("Programa terminou")
#             break
#         else:
#             graus_celsius = input("Digite a temperatura em °C: ")

# 22. Verificador de Palíndromo

# frase = input("Digite a frase para verificar [Digite 'exit' para sair]: ")
# while True:

#     if frase.lower == 'exit':
#         print("Programa encerrado pelo usuário")
#     try:
#         frase_float = float(frase)
#         print("Por favor, digite uma frase e não números! ")
#         frase = input("Digite a frase para verificar [Digite 'exit' para sair]: ")

#     except ValueError:
#         if isinstance(frase, str):
#             esarf = (''.join(reversed(frase)))
#             if frase == esarf:
#                 print("Palíndromo!")
#                 break
#             else:
#                 print("Não palíndromo!")
#                 break
#         else:
#             print("Outro tipo de erro desconhecido! ")

# 23. Calculadora simples

# def verifica_float(n):
#     try:
#         n = float(n)
#         return n
#     except ValueError as e:
#         print(e)
#         n = input("Digite novamente o número: ")
#         return verifica_float(n)
      
# def verifica_operador(operador):
#     operadores = ['+', "-", '*', "/"]
#     if operador in operadores:
#         return operador
#     else:
#         operador = input(f"Por favor, digite um dos {operadores}")
#         return verifica_operador(operador)

# def calculo(n1:float, n2:float, operador:str) -> float:
#     if operador == '+':
#         return n1 + n2
#     elif operador == '-':
#         return n1 - n2
#     elif operador == '*':
#         return n1 * n2
#     elif operador == '/':
#         if n2 == 0:
#             raise ValueError("Divisão por zero não é permitida.")
        
#         return n1 / n2
#     else:
#         raise ValueError("Operador inválido.")

# n1, n2, operador = [None for i in range(3)]
# print(n1)
# print(n2)
# print(operador)
# while True:
    
#     print('Digite "exit" a qualquer momento para sair')
#     n1 = input("1° número: ")
#     if n1.lower() == 'exit':
#         print("Saiu")

#         break
#     n1 = verifica_float(n1)

#     operador = input("Digite um operador:\t'+'\n\t\t\t'-'\n\t\t\t'*'\n\t\t\t'/': ")
#     if operador.lower() == 'exit':
#         print("Saiu")
#         break
#     operador = verifica_operador(operador)


#     n2 = input("2° número: ")
#     if n2.lower() == 'exit':
#         print("Saiu")
#         break
#     n2 = verifica_float(n2)

#     result = calculo(n1, n2, operador)

#     print(result)

# 24. Classificador

def verifica_float(n):
     try:
         return float(n)
     except ValueError:
         raise ValueError(f"Número inválido. {n} não é um número! ")
    
def classificador(n):
    if n == 0:
       return "Zero"
    elif n < 0:
        return "Negativo"
    else:
        return "Positivo"
    
def impar_par(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
# def obter_entrada(mensagem, validador):
#     while True:
#         entrada = input(mensagem).strip()
#         if entrada.lower() == 'exit':
#             print('Saindo...')
#             sys.exit()
#         try:
#             return validador(entrada)
#         except ValueError as e:
#             print(f"erro: {e}")

# def main():
#     while True:
#         print('\nDigite "exit" a qualquer momento para sair.')
#         n = obter_entrada("Número: ", verifica_float)

#         try:
#             classificacao = classificador(n)
#             print(f"O n° {n} é {classificacao}")
#         except Exception as e:
#             print(f"Erro durante a classificação: {e}")

#         try:
#             parimpar = impar_par(n)
#             print(f"O n° {n} é {parimpar}")
#         except Exception as e:
#             print(f"Erro durante a o impar_par: {e}")

# if __name__ == "__main__":
#     main()

# 25. Conversão de tipo com validação
def verifica_separador(mensagem):

    l_input = mensagem.split(',')
    if len(l_input) <= 1:
        raise SyntaxError("Nenhum separador ',' foi encontrado")
    else:
        return (l_input)

def obter_entrada2(mensagem, verifica_separador):
    while True:
        entrada = input(mensagem).strip()

        if entrada.lower() == 'exit':
            print('Saindo...')
            sys.exit()
        try:
            partes = verifica_separador(entrada)
            
            numeros = [verifica_float(parte.strip()) for parte in partes]
            return numeros
        
        except ValueError as e:
            print(f"erro: {e}. Tente novamente! ")
        except SyntaxError as e2:
            print(f"Erro: {e2}. Tente novamente! ")
if __name__ == "__main__":
    valores = obter_entrada2(
        "Digite números separados por vírgula (ex: 3, 5.2): ",
        verifica_separador
    )
    print("Valores válidos:", valores)

  
