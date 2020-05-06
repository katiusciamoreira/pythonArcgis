# Exemplo de código para gerar app declividade > 45 graus:

# 1 Verificar se extensão spatial analyst está disponível e habilitada

# 2 Importar biblioteca arcpy

# 3 Definir função "calculaAppDeclividade" e variáveis "decliv" e "app_decliv" 

# 4 Definir arquivos de saída como "decliv" e "app"

# O nome do arquivo raster usado para o MDE(Modelo Digital de Elevação) para rodar o Slope foi "MDE.tif"

import arcpy

def calculaAppDeclividade(MDE):
	decliv=arcpy.sa.Slope("DEM","DEGREE")
	app_decliv=decliv>=45
	return decliv, app_decliv

decliv, app= calculaAppDeclividade("DEM.tif")

# Resultado: irá retornar dois arquivos de saída nomeados como "slope" com as declividades calculadas e  "app" que retorna
# app com atributos 0 e 1, sendo 1 (true) para app com declividade >= 45 graus, caso houver, e 0(false) para app <=45 graus.
