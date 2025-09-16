
class retangulo: # criando classe
    def __init__(self, retangulo_altura, retangulo_largura): # construtor padrao
        self.altura = retangulo_altura
        self.largura = retangulo_largura

    def area(self): # funcao da classe
            area = self.altura * self.largura
            print("A area do retangulo é:" + str(area))

class esfera:
     def __init__(self, esfera_raio):
        self.raio = esfera_raio

     def volume(self):
            volume = ((self.raio ** 3) * 3.14 ) * 4/3
            print("O volume da esfera é: " + str(round(volume, 2))) # round serve para limitar as casas decimais de um float

op = 0
while op != 3:
    op = int(input("1 - Area de um retangulo \n2 - Volume de uma esfera \n3 - Sair \nopçao: "))

    if op == 1:
        altura, largura = map(float, input("Informe a altura e largura: ").split()) # input q pega mais de uma variavel
        ob1 = retangulo(altura, largura)
        ob1.area()
    elif op == 2: 
        raio = float(input("Informe o raio da esfera: "))
        ob2 = esfera(raio)
        ob2.volume()
    elif op == 3:
      print("tchau")
    else:
      print("informe um valor valido")



    





    

