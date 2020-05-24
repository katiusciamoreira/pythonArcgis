# Alguns conteúdos em python para tarefas em arcgis

* <b>Exemplo 1 - CALCULAR APP DE DECLIVIDADE > 45 GRAUS:</b> [calcula-app-decliv.py](https://github.com/katiusciamoreira/pythonArcgis/blob/master/datas/calcula-app-decliv.py)<br>
<b>Descrição:</b> cálculo de APPs de Declividade acima de 45 graus. APP:Áreas de preservação permanente no código florestal brasileiro (Lei 12.651/2012)<br>

* <b>Exemplo 2 - SCRIPT TOOL PARA PROJETAR VÁRIOS ARQUIVOS DE UMA PASTA:</b> <br>
<b>Descrição:</b>o objetivo do script é alterar o sistema de coordenadas de todos os arquivos Shapefiles que estiverem dentro de uma pasta indicada, sendo que se o Shapefile for do tipo polígono e o sistema de coordenada de saída do tipo projetado(ex: UTM), também será criado um campo no qual será calculado o valor das áreas dessas geometrias(neste exemplo calculo em hectares).<br>
<b>Passo 1:</b> Script:[ProjectFolder.py](https://github.com/katiusciamoreira/pythonArcgis/blob/master/datas/ProjectFolder.py)<br>
<b>Passo 2:</b> Criar Toolbox e adicionar o Script criado: [ProjetarPasta.tbx](https://github.com/katiusciamoreira/pythonArcgis/blob/master/datas/ProjetarPasta.tbx)<br>
Obs.: Configuração para as colunas Display Name / Data Type da Toolbox com o script que está sendo adicionado:<br>
a. Input Folder/ Folder;<br>
b. Output Folder/ Folder;<br>
c. Output Coordinate System/ Coordinate System.<br>
<b>Passo 3 (Opcional):</b> Caso queira colocar uma mensagem de erro customizada para o usuario não colocar a mesma pasta no input e no output, precisamos alterar a função updateMessages (é só clicar com o botao direito no script dentro da toolbox criada, ir em propriedades e na aba validação clicar em editar, alterar o codigo no bloco de notas, salvar e aplicar):
<br>Para tanto copie e cole essa parte de código para alterar a função updateMessages [updateMessages.py](https://github.com/katiusciamoreira/pythonArcgis/blob/master/datas/updateMessages.tbx):
<br><b>PRONTO!</b> Já pode rodar sua Toolbox e projetar todos os arquivos de uma vez, já com a área calculada.<br>
* <b>Exemplo 3 - ADICIONAR OS CENTROIDES EM VÁRIOS ARQUIVOS DE UMA PASTA:</b> <br>
<b>Descrição:</b>usar a função Calculate Field para adicionar as coordenadas x e y na tabela de atributos de todas as classes de feição de uma pasta selecionada.<br>
<b>Passo 1:</b> Script:[centroidCalculateField.py](https://github.com/katiusciamoreira/pythonArcgis/blob/master/datas/ProjectFolder.py)<br>
<b>Passo 2:</b> Criar Toolbox e adicionar o Script criado: [CalcularCentroides.tbx](https://github.com/katiusciamoreira/pythonArcgis/blob/master/datas/CalcularCentroides.tbx)<br>
Obs.: Configuração para as colunas Display Name / Data Type da Toolbox com o script que está sendo adicionado:<br>
a. Input Folder/ Folder;<br>

Obs.: explicações em comentários dentro dos códigos
____________________________________________________________________________________________________________________________

# Some python content for arcgis tasks

Obs.: explanations by coments inside codes

**Thanks! - Katiuscia Moreira**
<br>
[Linkedin Profile](https://www.linkedin.com/in/katiuscia-moreira-0026833b/)
