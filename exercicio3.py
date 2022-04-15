nome = input("Digite seu nome, porfavor")
salario = input("Digite seu salario de Abril, porfavor")
if (isinstance(nome, str) and isinstance(salario,int)):
    print("o salario de ", nome, " foi de R$", salario[0 : 4], ",", salario[4 : 6], " reais", sep='')
else:
    print("Você digitou um nome no lugar do numero ou o contrario, tente de novo")


