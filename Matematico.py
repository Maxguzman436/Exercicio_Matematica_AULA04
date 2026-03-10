#Exercicio MATEMATICO
#10/03/2026
#Max Guzman

operacao = input("selecione a operação:\n\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n5 - POTENCIAÇÃO\n6 - RADICIAÇÃO\n\nEscolha(numero): ")
operacao = int(operacao)

if operacao == 1:
	#SOMA
	print("\n\n")
	print("#########################################")
	print("                 SOMADOR                 ")
	print("#########################################")

	a = input("Digite o primeiro numero: ")

	a = int(a)

	b = input("Digite o segundo numero: ")

	b = int(b)

	c = a + b

	print(f"A soma de {a} e {b} é {c}")

	input()
elif operacao == 2:
	#SUBTRAÇÃO
	print("\n\n")
	print("#########################################")
	print("                 SUBTRAIR                ")
	print("#########################################")
	
	a = input("Digite o primeiro numero: ")
	
	a = int(a)
	
	b = input("Digite o segundo numero: ")
	
	b = int(b)
	
	c = a - b
		
	print(f"A subtração de {a} e {b} é {c}")
	
	input()
elif operacao == 3:
	#MULTIPLICACAO
	print("\n\n")
	print("#########################################")
	print("                 MULTIPLICACAO           ")
	print("#########################################")

	a = input("Digite o primeiro numero: ")

	a = int(a)

	b = input("Digite o segundo numero: ")

	b = int(b)

	c = a*b

	print(f"A multiplicação de {a} por {b} é {c}")

	input()
elif operacao == 4:
	#DIVISAO
	print("\n\n")
	print("#########################################")
	print("                 DIVISAO                 ")
	print("#########################################")

	a = input("Digite o primeiro numero: ")

	a = int(a)

	b = input("Digite o segundo numero: ")

	b = int(b)

	c = a/b

	print(f"A divisão de {a} por {b} é {c}")

	input()
elif operacao == 5:
	#POTENCIACAO
	print("\n\n")
	print("#########################################")
	print("                 POTENCIACAO             ")
	print("#########################################")

	a = input("Digite o numero: ")

	a = int(a)

	b = input("Digite a potencia: ")

	b = int(b)

	c = a**b

	print(f"A potencia de {a} elevado a {b} é {c}")

	input()
elif operacao == 6:
	#RADICIACAO
	print("\n\n")
	print("#########################################")
	print("                 RADICIACAO              ")
	print("#########################################")

	a = input("Digite o numero: ")

	a = int(a)

	b = input("Digite o numero da raiz: ")

	b = int(b)

	c = a**(1/b)

	print(f"A raiz {b} de {a} é {c}")

	input()
else:
	print("\n")
	input("Coloca um numero valido parça\nAperta ENTER para fechar")