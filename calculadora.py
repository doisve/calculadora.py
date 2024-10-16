# somar
def adicionar(x, y):
    return x + y 

#  subtrair
def subtrair(x, y):
    return x - y 

# multiplicar
def multiplicar(x, y):
    return x * y 

# dividir 
def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"
    
# calculadora
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite sua escolha (1/2/3/4): ")

    # entrada de dados
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # executa a operção escolhida
    if escolha == '1':
        print(f"{num1} + {num2} = {adicionar(num1, num2)}")
    elif escolha == '2':
        print(f"{num1} - {num2} = {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else: 
        print("Opção inválida")    
    
calculadora()
