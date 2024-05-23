def converter_pés_para_metros(pés):
  return pés *0.3048

pés =  float(input("Digite a altura em pés:"))
metros = converter_pés_para_metros(pés)
print(f"{pés} pés é igual a {metros} metros")
