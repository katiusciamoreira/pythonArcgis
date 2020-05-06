// Exemplo de código para gerar app declividade > 45 graus

// 1 Verificar se extensão spatial analyst está disponível e habilitada. 

// 2 Importar Biblioteca Arcpy

// 3 Definir variáveis calculaAppDeclividade , decliv e app_decliv 

//Obs.: O nome do arquivo raster usado para o MDE(Modelo Digital de Elevação) para rodar o Slope foi MDE.tif

import arcpy

def calculaAppDeclividade(MDE):
	decliv=arcpy.sa.Slope("DEM","DEGREE")
	app_decliv=decliv>=45
	return decliv, app_decliv

decliv, app= calculaAppDeclividade("DEM.tif")

// Resultado: irá retornar o arquivo decliv que é o slope de declividade e o arquivo app que retorna
app com atributos 0 e 1, sendo 1 (true) para app com declividade >= 45 graus, caso houver, e 0(false) para app <=45 graus.
