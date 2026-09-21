#Validação perfil de consumo

#Solicita o tipo de imóvel
tipo_imovel = int(input('Qual tipo de imóvel?'
                        '\n[1] - Comercial'
                        '\n[2] - Casa'
                        '\n[3] - Apartamento\n'
                        'Digite: '))

#Solicita o consumo de água 
consumo = float(input('Qual o consumo mensal? [m³] '))

#Estrutura lógica que verifica as variaveis e retorna uma mensagem
if tipo_imovel == 1:
    print('Tarifa comercial aplicada - consulte o plano corporativo.')
elif tipo_imovel == 3 and consumo < 10:
    print('Consumo econômico - excelente controle de água!')
elif (tipo_imovel == 3 or tipo_imovel == 2) and consumo <= 25:
    print('Consumo mederado - dentro do padrão residencial.')
elif consumo > 25:
    print('Consumo excessivo - adote medidas de economia e verifique vazamentos.')
