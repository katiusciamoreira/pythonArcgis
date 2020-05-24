# Usar a funcao Calculate Field para adicionar as coordenadas x e y dos centroides de uma feicao 
# criando estes campos na tabela de atributos da feicao desejada
# Valido para arquivos classes de feicao do tipo poligono linha e ponto etc
# Obs No caso de pontos as coordenadas centrais adicionadas coincidirao com as mesmas da localizacao do ponto

# Importar os modulos
import arcpy
from arcpy import env

# Para capturar os parametros de entrada e saida da interface
input_folder = arcpy.GetParameterAsText(0)

# Para listar os shapefiles da pasta de entrada
arcpy.env.workspace = input_folder
listaFC = arcpy.ListFeatureClasses("*.shp")

# Caso nao sejam encontrados os arquivos Shapefiles emite-se um aviso
if len(listaFC) == 0:
    arcpy.AddWarning("Not found shapefiles in " + input_folder)

# Para cada Feature Class na lista do input, adicionar as coordenadas dos centroids na tabela de atributos
for file in listaFC:
    try: 
        env.workspace = input_folder    
    # Criar variaveis
        fieldName1 = "xCentroid"
        fieldName2 = "yCentroid"
        fieldPrecision = 18
        fieldScale = 11
 
    # Adicionar campos
        arcpy.AddField_management(file, fieldName1, "DOUBLE", fieldPrecision, fieldScale)
        arcpy.AddField_management(file, fieldName2, "DOUBLE", fieldPrecision, fieldScale)
 
    # Calcular centroide
        arcpy.CalculateField_management(file, fieldName1, "!SHAPE.CENTROID.X!", "PYTHON_9.3")
        arcpy.CalculateField_management(file, fieldName2, "!SHAPE.CENTROID.Y!", "PYTHON_9.3")
    except Exception as e:
    # Se um erro ocorrer imprimir o numero da linha e a mensagem de erro
        import traceback
        import sys
        tb = sys.exc_info()[2]
        print("Line {0}".format(tb.tb_lineno))
        print(e.message)

# Para este codigo usei algumas partes de bases da documentacao do arcgis disponivel em:
# http://resources.arcgis.com/en/help/main/10.1/index.html#//00170000004m000000