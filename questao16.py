valor,taxa,tempo=float(input("Digite o valor da presta��o:")),float(input("Digite a taxa da presta��o:")),int(input("Digite o tempo da presta��o em meses:"))
resultado=valor+(valor*(taxa/100)*tempo)
print("O valor desta presta��o em atraso � %2.f:"%resultado)