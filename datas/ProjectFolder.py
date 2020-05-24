# Importa a biblioteca arcpy
import arcpy

# Para capturar os parametros de entrada e saida da interface
input_folder = arcpy.GetParameterAsText(0)
output_folder = arcpy.GetParameterAsText(1)
coord_sys = arcpy.GetParameterAsText(2)

# Para listar os shapefiles da pasta de entrada
arcpy.env.workspace = input_folder
listaFC = arcpy.ListFeatureClasses("*.shp")

# Caso nao sejam encontrados os arquivos Shapefiles, emite-se um aviso
if len(listaFC) == 0:
    arcpy.AddWarning("Not found shapefiles in " + input_folder)

# Para cada Feature Class na lista, projetar para a pasta indicada
for FC_name in listaFC:
    output_FC = output_folder + "//" + FC_name
    arcpy.Project_management(FC_name, output_FC, coord_sys)

# Caso o Feature Class tenha geometria do tipo poligono e seja UTM
# a area sera calculada no novo sistema de coordenada no campo AREA
descr = arcpy.Describe(output_FC)
expr="!shape.area@HECTARES!" # variavel para expressao do calculo
if descr.shapeType == "Polygon" and descr.spatialReference.type =="Projected":
    arcpy.AddField_management(output_FC, "AREA", "DOUBLE")
    arcpy.CalculateField_management(output_FC, "AREA", expr, "PYTHON")
 