def calcular_porcentagem(porcetagem, numero):
    return(porcentagem/100)* numero
    
    porcentagem = flot(input("Digite a porcentagem:"))
    numero = float(input("Digite o número:"))
    resultado = calcular_porcentagem(porcentagem, numero)
    print(f"{porcentagem}% de {numero} é {resultado}")


