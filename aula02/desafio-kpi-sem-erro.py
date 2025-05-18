import sys

def verificar_nome(nome):
    nomeverifica = nome.strip()
    nomeverifica = nomeverifica.replace(' ', '')
    if not nomeverifica.isalpha():
        raise TypeError("Digite seu nome completo: ")
    
    elif len(nome.split(' ')) < 2:
        raise ValueError("Digite seu nome completo: ")

    else:
        return(nome)

def verifica_valor(n):
    if n <= 0:
        raise ValueError("Proibido números <= 0")
    return float(n)
def verifica_float(n):
    try:
        n =  float(n)
        return (verifica_valor(n))
    except ValueError as e:
        raise ValueError(f"Número inválido. '{n}' não é um número MAIOR QUE ZERO! ") from e

def obter_entrada(mensagem, validador):
     while True:
        entrada = input(mensagem).strip()
        if entrada.lower() == 'exit':
            print('Saindo...')
            sys.exit()
        try:
            return validador(entrada)
        except ValueError as e:
            print(f"\nError: {e}")
            print("Please try again")

def calculo(n1, n2):
    CONST = 1000
    KPI = CONST + (n1 * n2)
    return KPI

def main():
    while True:

        try:
            print('\nDigite "exit" a qualquer momento para sair.')
            nome = obter_entrada("Nome Completo: ", verificar_nome)
            n1 = obter_entrada("Salário: ", verifica_float)
            n2 = obter_entrada("Bônus: ", verifica_float)

            bonus = calculo(n1, n2)
            print(f"{nome.title()}, sem bônus é: ")
            print(f"R$: {bonus:.2f}")
        except Exception as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
