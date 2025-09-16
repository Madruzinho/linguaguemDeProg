"""1. Saudação Personalizada:
Peça o nome do usuário e mostre a mensagem: "Olá, [nome]! Bem-vindo(a)!". """

print("1. Saudaçao Personalizada")
nome1 = input("Insira o seu nome: ")  

print("Olá," + nome1 + "! Bem-vindo(a)!")

# -------------------------------

""" 2. Cadastro Simples:
Solicite o nome, a idade e a cidade do usuário. Ao final, exiba a frase: "Seu nome é [nome],
você tem [idade] anos e mora em [cidade]."""

print("2. Cadastro Simples")

nome2 = input("Insira o seu nome: ")
idade = int(input("\nInsira a sua idade: "))
cidade = input("\nInsira o nome da sua cidade: ")

print("Seu nome é " + nome2 + " você tem " + str(idade) + " anos e mora em " + cidade)

# ------------------------------- 

""" 3. Etiqueta de Endereço:
Escreva um programa que imprima seu nome completo, endereço e telefone, cada informação
em uma linha separada. """
print("3. Etiqueta de Endereço")

nome3 = input("Insira o seu nome")
endereco = input("Insira o seu endereço")
telefone = input("Insira o seu telefone")

print("Nome: " + nome3)
print("Endereço: " + endereco)
print("telefone: " + telefone)

# -------------------------------

""" 4. União de Palavras:
Peça ao usuário para digitar duas palavras. Junte-as em uma única frase e depois mostre a
frase inteira em letras maiúsculas. """
print("4. União de Palavras")

palavra1 = input("Primeira palavra: ")
palavra2 = input("Segunda palavra: ")
frase = palavra1 + " " + palavra2
fraseMaiscula = frase.upper()
print(fraseMaiscula)

# -------------------------------

""" 5. Conversor de Medidas:
Leia um valor em metros e o converta para centímetros e milímetros. """

print("5. Conversor de Medidas")

valorMetros = float(input("Insira um valor em metros"))
valorCm = valorMetros * 100
valorMm = valorMetros * 1000

print("Centimetros" + str(valorCm))
print("Milimetros" + str(valorMm))

# -------------------------------

""" 6. Cálculos Simples:
Leia um número inteiro e mostre o dobro e a terça parte dele."""

print("6. Calculos Simples")

Num = int(input("Informe o valor de um inteiro"))
NumDobro = Num * 2
NumTerço = Num / 3
print("Dobro: " + str(NumDobro))
print("Terça parte dele" + str(NumTerço))

# -------------------------------

""" 7. Calculadora de Quatro Operações:
Peça dois números e mostre os resultados da soma, subtração, multiplicação e divisão entre
eles. """

print("7. Calculadora de Quatro Operaçoes")
PrimeiroNum = float(input("Insira o primeiro valor: "))
SegundoNum = float(input("Insira o segundo valor: "))
Soma = PrimeiroNum + SegundoNum
Subtracao = PrimeiroNum - SegundoNum
Multiplicao = PrimeiroNum * SegundoNum
Divisao = PrimeiroNum / SegundoNum
print("Soma: " + str(Soma))
print("Subtraçao: " + str(Subtracao))
print("Multiplicaçao: " + str(Multiplicao))
print("Divisão: " + str(Divisao))

# -------------------------------

""" 8. Cálculo de Média Escolar:
Leia três notas de um aluno e calcule a sua média final. """

print("8. Calculo de Media Escolas")

PrimeiraNota = float(input("Primeira nota: "))
SegundaNota = float(input("Segunda nota: "))
TerceiraNota = float(input("Terceira nota: "))

mediaFinal = (PrimeiraNota + SegundaNota + TerceiraNota) / 3

print("Media final: " + str(mediaFinal))

# -------------------------------

""" 9. Cálculo de Área:
Peça a base e a altura de um retângulo e calcule sua área. """

print("9. Calculo de Area")

Base = float(input("Informe a base: "))
Altura = float(input("Informe a altura: "))

Area = Base * Altura

print("A area total é: " + str(Area))

# -------------------------------

""" 10. Calculadora de Números Decimais:
Crie uma calculadora que aceite números com casas decimais (float) para as quatro operações
básicas. """

print("Calculadora de decimais")
PrimeiroNum2 = float(input("Insira o primeiro valor: "))
SegundoNum2 = float(input("Insira o segundo valor: "))

Soma2 = PrimeiroNum2 + SegundoNum2
Subtracao2 = PrimeiroNum2 - SegundoNum2
Multiplicao2 = PrimeiroNum2 * SegundoNum2
Divisao2 = PrimeiroNum2 / SegundoNum2
print("Soma: " + str(Soma2))
print("Subtraçao: " + str(Subtracao2))
print("Multiplicaçao: " + str(Multiplicao2))
print("Divisão: " + str(Divisao2))

# -------------------------------

""" 11. Reajuste Salarial:
Leia o salário de um funcionário e a porcentagem de reajuste. Calcule e mostre o novo salário. """

print("11. Reajuste salarial")

Salario = float(input("Informe o salario do funcionario: "))
Reajuste = float(input("Informe o reajuste em porcentagem: "))

reajustePorcentagem = (Reajuste / 100) + 1

novoSalario = Salario *  reajustePorcentagem

print("novo salario: " + str(novoSalario))

# -------------------------------

""" 12. Índice de Massa Corporal (IMC):
Peça o peso (kg) e a altura (m) de uma pessoa e calcule o seu IMC.(Fórmula: IMC =
Peso/altura²) """

print("12. Indice de Massa Corporal")

Peso = float(input("Insira o seu peso: "))
AlturaCorpo = float(input("Insira a sua altura(em metros): "))

IMC = Peso / AlturaCorpo ** 2

print("seu IMC é: " + str(IMC))




