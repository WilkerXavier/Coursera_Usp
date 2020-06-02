largura = int(input("Digite a largura do retangulo: "))
altura = int(input("Digite a altura do retangulo: "))

c = 1
l = 0

while l < altura:
    while c < largura:
        print("#", end = "\t")
        c = c + 1
    print("#")
    l = l + 1 
    c = 1