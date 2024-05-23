gols_futebol = 2.53
tempo_nba = 4 * 12
tempo_futebol = 90 + 3 + 3

pontos_por_minuto_nba = gols_futebol / tempo_nba
gols_por_minuto_futebol = gols_futebol / tempo_futebol

diferenca_pontos = pontos_por_minuto_nba - gols_por_minuto_futebol
print("Diferença de pontos:", diferenca_pontos)
