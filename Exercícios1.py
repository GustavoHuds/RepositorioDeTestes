def questao1():
    num = int(input("Digite um número: "))
    print(f"O número antecessor é {num-1} e o sucessor é {num +1}")



def questao2():
    num = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"A soma é: {num+num2}, a subtração é: {num-num2}, a multiplicação é: {num*num2}, e a divisão é: {num/num2}")


def questao3():
    num = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if num>num2:
        print(True)
    else:
        print(False)


def questao4():
    celsius = float(input("Digite a temperatura em celsius: "))
    print(f"A temperatura em celsius é: {celsius}, e a temperatura em fahrenheit é: {((celsius * 9) / 5) + 32}")



#Digite a questão desejada:
questao4()