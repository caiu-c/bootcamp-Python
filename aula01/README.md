# Aula 01 - Setup Inicial: Python, Git & GitHub, VSCode  

## Exercícios  

### 1. Contar Caracteres do Nome  
Crie um programa que solicita ao usuário que digite seu nome e retorna o número de caracteres.  

### 2. Soma de Dois Valores  
Crie um programa onde o usuário digite dois valores e o programa exiba a soma.  

## Desafio  

### KPI do Bônus de 2024  

#### Instruções:  
1. O programa deve solicitar o nome do usuário.  
2. Solicitar o valor do salário (número decimal).  
3. Solicitar a porcentagem do bônus (número decimal).  
4. Calcular o KPI do bônus usando a fórmula:  
    ```
    KPI = 1000 + salario * bônus
    ```  
5. Exibir a mensagem no formato:  
    ```
    Olá [nome], o seu valor bônus foi de [valor calculado].
    ```  

#### Exemplo de Saída:  
Se o usuário digitar:  
- Nome: Luciano  
- Salário: 5000  
- Bônus: 1.5  

O programa deve exibir:  
```
Olá Luciano, o seu bônus foi de 8500
```  

#### Código:  
Salve o script como `kpi.py`.  

## Documentação  

### Como Executar o Programa  

1. Certifique-se de ter o Python instalado em sua máquina.  
2. Salve o arquivo `kpi.py` no diretório desejado.  
3. Abra o terminal e navegue até o diretório onde o arquivo foi salvo.  
4. Execute o programa com o comando:  
    ```bash  
    python kpi.py  
    ```  
5. Siga as instruções exibidas no terminal.  

### Versionamento com Git e GitHub  

1. Inicialize o repositório Git:  
    ```bash  
    git init  
    ```  
2. Adicione o arquivo ao repositório:  
    ```bash  
    git add kpi.py README.md  
    ```  
3. Faça o commit:  
    ```bash  
    git commit -m "Adiciona script KPI e documentação"  
    ```  
4. Conecte ao repositório remoto no GitHub:  
    ```bash  
    git remote add origin <URL_DO_REPOSITORIO>  
    ```  
5. Envie os arquivos para o GitHub:  
    ```bash  
    git push -u origin main  
    ```  