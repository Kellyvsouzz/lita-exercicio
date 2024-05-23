def calcular_valor_com_lucro(valor_vendido, percentual_vendido, lucro_desejado):
    valor_original = valor_vendido / (percentual_vendido / 100)
    valor_com_lucro = valor_original * (1 + (lucro_desejado / 100))
    return valor_com_lucro

valor_vendido = 360
percentual_vendido = 80
lucro_desejado = 20

valor_com_lucro = calcular_valor_com_lucro(valor_vendido, percentual_vendido, lucro_desejado)
print(f"Para ter um lucro de {lucro_desejado}%, Guilherme deveria ter vendido por: R$ {valor_com_lucro:.2f}")
