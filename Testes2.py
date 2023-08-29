def questao1():

 salario = float(input("Digite seu salário:R$"))
 limite = salario/2.5
 print(f"Seu limite é:R${limite}")

 saldo = float(input("Digite seu saldo:R$ "))
 divida = float(input("Digite o valor da do boleto:R$ "))

 if saldo>=divida:
    print("Você pode pagar!")

 else:
    print("Você não pode pagar!")
    print(f"Você possui R${limite} disponível para empréstimo.")
    emprestimo = float(input("Qual o valor do empréstimo?:R$ "))
 
 if emprestimo<limite:
    meses = int(input("Em quantos meses quer parcelar?: "))
 else:
    print("Você não pode resgatar esse valor.")

 if (saldo+emprestimo)>=divida:
    print(f"Você poderá pagar o boleto! \nVocê pagará R${emprestimo//meses} de empréstimo por mês, durante {meses} meses.")
 else:
    print("Você é pobre!")

 valorEmConta = (emprestimo+saldo)-divida
 print(f"Saldo restante em conta:R${valorEmConta}")


questao1()
