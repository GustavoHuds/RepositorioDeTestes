def case1():

    class Pessoa():
        def __init__(self, nome, idade, profissao):
            self.nome = nome
            self.idade = idade
            self.profissao = profissao

        def saudacao(self):
            return (f"oi, meu nome é {self.nome}, tenho {self.idade} anos, e trabalho como {self.profissao}.")
        
    pedro = Pessoa("Pedro", 25, "Reporter")
    print(pedro.saudacao())

    guilherme = Pessoa("Guilherme", 17, "Estagiário")
    print(guilherme.saudacao())

    joao = Pessoa("João", 24, "Empresário")
    print(joao.saudacao())


def case2():

    class ContaBancaria():
        def __init__(self, titular, saldo, banco):
            self.titular = titular
            self.saldo = saldo
            self.banco = banco

        def infos(self):
            return (f"Boa tarde {self.titular}, seu saldo é de R${self.saldo}, no banco {self.banco}.")
        
        def depositar(self, dep):
            self.saldo += dep
        
        def sacar(self, qtd):
            self.saldo -= qtd
        
    rodrigo = ContaBancaria("Rodrigo", 100, "Santander")
    print(rodrigo.infos())

    valor = int(input("Digite 1 para sacar e 2 para depositar: "))
    if valor == 1:
        qtd = float(input("Quanto deseja sacar?: R$"))
        rodrigo.sacar(qtd)
        print (f"{rodrigo.infos()}")
    elif valor == 2:
        dep = float(input("Quanto deseja depositar?: R$"))
        rodrigo.depositar(dep)
        print (f"{rodrigo.infos()}")

def case3():

    class Carro():
        def __init__(self, marca, modelo, ano):
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

        def infos(self):
            return (f"O carro é da marca {self.marca}, modelo {self.modelo}, do ano {self.ano}")

        def acelerar(self):
            print (f"O {self.modelo} foi acelerado")

    carro1 = Carro("Toyota", "Supra", 2019)
    print(carro1.infos())

    carro1.acelerar()
        

def case4():

    class FormaGeometrica:
        def calcular_a_área(self, raio):
            return 3.14*(raio**2)
        
    class Circulo(FormaGeometrica):
        pass

    class Retangulo(FormaGeometrica):
        def calcular_a_área(self, base, altura):
            return base*altura
        
    class Quadrado(Retangulo):
        pass

    circulo = Circulo()
    area = circulo.calcular_a_área(20)
    print(area)

    retangulo = Retangulo()
    area = retangulo.calcular_a_área(5, 10)
    print(area)

    quadrado = Quadrado()
    area = quadrado.calcular_a_área(10, 9)
    print(area)


def case5():

    class Animal:
        def som_do_animal(self, som):
            pass
        
    class Cachorro(Animal):
        def som_do_animal(self, som):
            return (som)
        
    class Gato(Animal):
        def som_do_animal(self, som):
            return (som)
        
    cachorro = Cachorro()
    fala = cachorro.som_do_animal("Au Au")
    print(fala)
    
    gato = Gato()
    fala = gato.som_do_animal("Miau")
    print(fala)

#Escolha a questão:
case5()