#Exercicio MATEMATICO
#10/03/2026
#Max Guzman

import os

est = 0
while est == 0:
	print("#########################################")
	print("               Calculadora               ")
	print("#########################################")
	operacao = input("Selecione a operação:\n\n1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n5 - POTENCIAÇÃO\n6 - RADICIAÇÃO\n\nEscolha(numero): ")
	operacao = int(operacao)

	if operacao == 1:
		#SOMA
		os.system('cls' if os.name == 'nt' else 'clear')
		print("#########################################")
		print("                 SOMADOR                 ")
		print("#########################################")

		a = input("Digite o primeiro numero: ")

		a = int(a)

		b = input("Digite o segundo numero: ")

		b = int(b)

		c = a + b

		print(f"A soma de {a} e {b} é {c}")

		print("\n\n")
		at = input("1 - Reiniciar\n2 - Fechar\n\nEscolha(numero): ")
		at = int(at)
		if at == 1:
			est = 0
			os.system('cls' if os.name == 'nt' else 'clear')
		elif at == 2:
			est = 1
			os.system('cls' if os.name == 'nt' else 'clear')
	elif operacao == 2:
		#SUBTRAÇÃO
		os.system('cls' if os.name == 'nt' else 'clear')
		print("#########################################")
		print("                 SUBTRAIR                ")
		print("#########################################")
	
		a = input("Digite o primeiro numero: ")
	
		a = int(a)
	
		b = input("Digite o segundo numero: ")
	
		b = int(b)
	
		c = a - b
		
		print(f"A subtração de {a} e {b} é {c}")
	
		print("\n\n")
		at = input("1 - Reiniciar\n2 - Fechar\n\nEscolha(numero): ")
		at = int(at)
		if at == 1:
			est = 0
			os.system('cls' if os.name == 'nt' else 'clear')
		elif at == 2:
			est = 1
			os.system('cls' if os.name == 'nt' else 'clear')
	elif operacao == 3:
		#MULTIPLICACAO
		os.system('cls' if os.name == 'nt' else 'clear')
		print("#########################################")
		print("                 MULTIPLICACAO           ")
		print("#########################################")

		a = input("Digite o primeiro numero: ")

		a = int(a)

		b = input("Digite o segundo numero: ")

		b = int(b)

		c = a*b

		print(f"A multiplicação de {a} por {b} é {c}")

		print("\n\n")
		at = input("1 - Reiniciar\n2 - Fechar\n\nEscolha(numero): ")
		at = int(at)
		if at == 1:
			est = 0
			os.system('cls' if os.name == 'nt' else 'clear')
		elif at == 2:
			est = 1
			os.system('cls' if os.name == 'nt' else 'clear')
	elif operacao == 4:
		#DIVISAO
		os.system('cls' if os.name == 'nt' else 'clear')
		print("#########################################")
		print("                 DIVISAO                 ")
		print("#########################################")

		a = input("Digite o primeiro numero: ")

		a = int(a)

		b = input("Digite o segundo numero: ")

		b = int(b)

		c = a/b

		print(f"A divisão de {a} por {b} é {c}")

		print("\n\n")
		at = input("1 - Reiniciar\n2 - Fechar\n\nEscolha(numero): ")
		at = int(at)
		if at == 1:
			est = 0
			os.system('cls' if os.name == 'nt' else 'clear')
		elif at == 2:
			est = 1
			os.system('cls' if os.name == 'nt' else 'clear')
	elif operacao == 5:
		#POTENCIACAO
		os.system('cls' if os.name == 'nt' else 'clear')
		print("#########################################")
		print("                 POTENCIACAO             ")
		print("#########################################")

		a = input("Digite o numero: ")

		a = int(a)

		b = input("Digite a potencia: ")

		b = int(b)

		c = a**b

		print(f"A potencia de {a} elevado a {b} é {c}")

		print("\n\n")
		at = input("1 - Reiniciar\n2 - Fechar\n\nEscolha(numero): ")
		at = int(at)
		if at == 1:
			est = 0
			os.system('cls' if os.name == 'nt' else 'clear')
		elif at == 2:
			est = 1
			os.system('cls' if os.name == 'nt' else 'clear')
	elif operacao == 6:
		#RADICIACAO
		os.system('cls' if os.name == 'nt' else 'clear')
		print("#########################################")
		print("                 RADICIACAO              ")
		print("#########################################")

		a = input("Digite o numero: ")

		a = int(a)

		b = input("Digite o numero da raiz: ")

		b = int(b)

		c = a**(1/b)

		print(f"A raiz {b} de {a} é {c}")
		
		print("\n\n")
		at = input("1 - Reiniciar\n2 - Fechar\n\nEscolha(numero): ")
		at = int(at)
		if at == 1:
			est = 0
			os.system('cls' if os.name == 'nt' else 'clear')
		elif at == 2:
			est = 1
			os.system('cls' if os.name == 'nt' else 'clear')
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		at = input("Coloca um numero valido parça\n\n1 - Reiniciar\n2 - Fechar\n\nEscolha(numero): ")
		at = int(at)
		if at == 1:
			est = 0
			os.system('cls' if os.name == 'nt' else 'clear')
		elif at == 2:
			est = 1
			os.system('cls' if os.name == 'nt' else 'clear')
