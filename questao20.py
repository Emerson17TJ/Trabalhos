dolar=float(input("Digite o valor em dolares que vc quer calcular:"))
sabe=input("Voc� sabe qual o valor da cota��o atual do dolar? ")
if(sabe=="sim" or sabe=="Sim"):
    cota=float(input("Digite o valor da cota��o atual do dolar:"))
else:
    cota=3.900
print("O valor aproximado em reais que voc� possui � ",dolar*cota)