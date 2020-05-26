crescente = True
anterior = int(input("Digite o primeiro numero da sequencia: "))

valor = 1

while valor != 0 and crescente:
    valor = int(input("Digite o proximo numero da sequencia: "))
    if valor > anterior:
        crescente = False
    anterior = valor
     
if crescente:
    print ("A sequencia está em ordem crescente !!!!")
else: 
    print ("A sequencia não está em ordem crescente !!!!")