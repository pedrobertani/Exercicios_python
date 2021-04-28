#metros cúbicos em litros
 n1=float(input("Metros³: "))
n2=1000*n1
print("Convertido em Litros: %.2f" %n2)

#litros em metros cúbicos
 n1=float(input("Litros: "))
n2=n1/1000
print("Convertido em M³: %.2f" %n2)

# Kgs convertidos em libras
 n1=float(input("Kg: "))
n2=n1/0.45
print("Convertido em Libras: %.2f" %n2)

#Libras convertidos em Kgs
 n1=float(input("Libras: "))
n2=n1*0.45
print("Convertido em Kg: %.2f" %n2)

#Jardar em metros 
 n1=float(input("Jardas: "))
n2=0.91*n1
print("Convertido em Metros: %.2f" %n2)

#Metros em jardas
 n1=float(input("Metros: "))
n2=n1/0.91
print("Convertido em Jardas: %.2f" %n2)

#Metros ² em acres
 n1=float(input("M²: "))
n2=n1*0,000247
print("Convertido em Acres: %.2f" %n2)

#Acres em Metros² 
n1=float(input("Acres: "))
n2=n1*4048.58
print("Convertido em M²: %.2f" %n2)

#Metros em hectares
 n1=float(input("M²: "))
n2=n1*0.0001
print("Convertido em Hectares: %.2f" %n2)

#Hectares em metros
 n1=float(input("H: "))
n2=n1*10000
print("Convertido em M²: %.2f" %n2)

#soma de números ao quadrado
 n1=float(input("Digite um número: "))
n2=float(input("Digite um número: "))
n3=float(input("Digite um número: "))
n4=pow(n1,2)+pow(n2,2)+pow(n3,2)
print("Soma de todos os números ao quadrado é: %.f" %n4)

#média
 n1=float(input("Digite a primeira nota: "))
n2=float(input("Digite a segunda nota: "))
n3=float(input("Digite a terceira nota: "))
n4=float(input("Digite a quarta nota: "))
m=(n1+n2+n3+n4)/4
print(“média: %.2f” %m)
if m >= 6.0:
    if m == 10.0:
        print("Aprovado")
    else:
        print("Aprovado")
else:
    print ("Reprovado")

#Conversão dólar em real
n1=float(input("Digite o valor em R$: "))
n2=float(input("Digite a cotação do dólar: "))
n3=n1/n2
print("O valor de Reais em dólares é: %.2f" %n3)

#numero sucessor e antecessor n1=float(input("Digite um número: "))
n2=n1-1
n3=n1+1
print("O número antecessor é: %.f" %n2)
print("O número sucessor é: %.f" %n3)


#soma de sucessor

 n1=float(input("Digite um número: "))
n2=(n1*3)+1
n3=(n1*2)-1
n4=n2+n3
print("A soma do sucessor de seu triplo com o antecessor de seu dobro: %.f " %n4)

#calculo de área de um quadrado
 print("Entre com valor de um dos lados do quadrado para ter p valor de sua area.")
n1=float(input("Lado: "))
n2=pow(n1,2)
print("O valor da area do quadrado é: %.2f" %n2)

# valor de área de um circulo
import math
n1=float(input("Raio do circulo: "))
n2=3.14*pow(n1,2)
print("O valor da area do circulo é: %.2f" %n2)

#valor de hipotenusa 
 n1=float(input("Entre com valor de do cateto 1: "))
n2=float(input("Entre com valor do cateto 2 : "))
n3=pow(pow(n1,2)+pow(n2,2),0.5)
print("O valor da hipotenusa é: %.2f" %n3)

#unidades de medidas
número=int(input"número: "))
unidade=int(número/100)
número=int(número%100)
dezena=int(número/10)
centena=int(número%10)
print("unidade: ", unidade)
print("dezena: ", deneza)
print("centena: ", centena)
soma=centena*100+dezena*10+unidade
print("número invertido: %d" %soma)

n=input("n: ")
print(n[2])
print(n[1])
print(n[0])
soma=int(n[0]+int(n[1])*10+int(n[2])*100
print("número invertido %d" %soma)

#LISTA DE EXERCÍCIOS 2
#dinheiro
dinheiro=int(input("dinheiro: "))
if(dinheiro >=10):
 print("cinema")
 print("pipoca")
 print("dorme")
else:
 print("casa")
 print("durmo")
 print("internet")
print("namora")

veiculo=float(input("Veiculo: "))
cliente=float(input("Cliente: "))
if(veiculo<=cliente):
    print("a vista")
else:
    parcela=(veiculo-cliente)/2
    print("Valor a prazo: 2x %.2f" %parcela)

#Exercícios da lista 2:

 x=int(input("Entre com valor de X: "))
y=int(input("Entre com valor de Y: "))
if(x > y):
    print("X é maior que Y")
    print("valor de X é: %d" %x)
else:
    print("Y é menor que X")
    print("Valor de Y é: %d" %y)

#2
 n1=int(input("Entre com um número: "))
if(n1 >=1):
    n2=n1 ** (1/2.0)
    print("Número %d é valido." %n1)
    print("Raiz quadrada do seu número é: %d" %n2)
else:
          print("Número invalido.")

#3
 n1=int(input("Entre com um número: "))
if(n1 >=1):
    n2=n1 ** (1/2.0)
    print("Número %d positivo." %n1)
    print("Raiz quadrada do seu número é: %d" %n2)
elif(n1 <=0):
    n3=n1**2
    print("Número %d negativo." %n1)
    print("O quadrado do seu número é: %d" %n3)
    
#4
 n1=int(input("Entre com um número: "))
if(n1 >=1):
    n2=n1**2
    n3=n1 ** (1/2.0)
    print("Número %d positivo." %n1)
    print("O quadrado do número é: %d" %n2)
    print("Raiz quadrada do seu número é: %d" %n3)
else:
    print("Número invalido.")
#5
 n1=int(input("Digite um valor: "))
if int(n1) % 2 == 0:
    print("O numero informado e par")
else:
    print("O numero informado e impar")

#6
 n1=int(input("Digite um valor X: "))
print("Valor de X é: %d" %n1)
n2=int(input("Digite um valor Y: "))
print("Valor de Y é: %d" %n2)
n3 = n1-n2 
print(" A diferença entre X e Y é: %d" %n3)
if n1 > n2:
    print("o maior valor é : %d" %n1)
else:
    print("o maior valor é : %d" %n2)

#7
 n1=int(input("Digite um valor X: "))
print("Valor de X é: %d" %n1)
n2=int(input("Digite um valor Y: "))
print("Valor de Y é: %d" %n2)
if n1 > n2:
    print("o maior valor é : %d" %n1)
elif n1==n2:
    print("Números iguais")
else:
    print("o maior valor é : %d" %n2)

#8
 n1=float(input("Entre com valor da primeira nota: "))
n2=float(input("Entre com valor da segunda nota: "))
n3=(n1+n2)/2
if n3 >= 0.0 and n3 <= 10.0:
    print("A média do aluno é: %1.f" %n3)
else:
    print("Valor invalido, o sistema sera fechado em 10 segundos.")

#9
 print("Gostaria de fazer um emprestimo!?")
n1=float(input("Digite o valor do salário: "))
n2=float(input("Digite o valor da prestação"))
n3= n1/100*20
if n3 > n2:
    print("Emprestimo não concedido.")
else:
    print("Emprestimo pode ser concedido.")

#10
 print("Base de calculo de pontuação 0 a 100.")
print("Média de aprovação: 60 pontos.")
n1=int(input("Primeira nota: "))
n2=int(input("Segunda nota: "))
n3=int(input("Terceira nota: "))
soma=(1+1+2)
mp=((n1)+(n2)+(n3*2))/soma
print("média ponderada é: %d" %mp)

if(mp >=60):
    print("Aprovado.")
else:
    print("Reprovado.")

#11

a=float(input("Lado A: "))
b=float(input("Lado B: "))
c=float(input("Lado C: "))
if(a==b) and (a==c):
    print("Equilatero")
elif(a==b) or (a==c) or (b==c):
    print("Isosceles")
else:
    print("Escaleno")

#12
peso=float(input("Peso: "))
altura=float(input("Altura: "))
imc=peso/(altura**2)
print("IMC: %f" %imc)
if(imc <= 18.5):
    print("Abaixo do peso")

