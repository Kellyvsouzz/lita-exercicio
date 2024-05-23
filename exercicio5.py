  
altura_trapezio = 145
base_maior = 120
base_menor = 75
area_trapezio = ((base_maior + base_menor) / 2) * altura_trapezio
largura_palco = 15
altura_palco = 8.5
area_palco = largura_palco * altura_palco
area_disponivel = area_trapezio - area_palco
lotacao_maxima_por_m2 = 4
snumero_maximo_ingressos = area_disponivel * lotacao_maxima_por_m2
  
print ("NC:mero mC!ximo de ingressos que podem ser vendidos:",
	   int (numero_maximo_ingressos))

