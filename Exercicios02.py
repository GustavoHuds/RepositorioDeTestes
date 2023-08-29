def exercicio(): 

 def questao1():
    ida = int(input("Digite sua idade: "))
    
    if ida>=18:
        print("Você pode tirar a CNH!")
    
    else: 
        print("Infelizmente você ainda não pode tirar a CNH.")


 def questao2():
    velocidade = int(input("Digite a velocidade detectada: "))
    if velocidade>80:
        print(f"Você foi multado!\aValor: R${(velocidade-80)*7}")
    else :
        print("Você não foi multado.")


 def questao3():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    maior = num1
    menor = num2

    if num2>num1 and num2>num3:
       maior = num2
    if num3>num1 and num3>num2:
       maior = num3
    if num1<num2 and num1<num3:
       menor = num1
    if num3<num2 and num3<num1:
       menor = num3

    print(f"O maior número é: {maior}, e o menor número é: {menor}")

 def questao4():
    canetaA = int(input("Digite o número de canetas azuis: "))
    canetaP = int(input("Digite o número de canetas pretas: "))
    vA = 2.0
    vP = 2.5

    print(f"O valor das canetas azuis foi:R${canetaA*vA}\nO valor das canetas pretas foi:R${canetaP*vP}")

 def questao5():
    nome = str(input(f"Qual o meu nome?: "))
    if nome=="joao Maia":
        print("Oi, eu sou João Maia.")
    elif nome=="joao Abrantes":
        print("Oi, eu sou João Abrantes.")
    elif nome=="pedro":
        print("Oi, eu sou Pedro.")
    else:
        print(f"Oi, eu sou {nome}")
    
    #Escolha uma questão:
questao()
#exercicio()






