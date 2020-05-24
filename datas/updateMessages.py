# Para adicionar uma validacao na toolbox com mensagem de erro customizada para que o usuario
# nao coloque a mesma pasta no input e no output, precisamos alterar a funcao updateMessages
# (clicar com o botao direito no script dentro da toolbox criada, ir em propriedades e na aba
# validação clicar em editar, alterar o codigo no bloco de notas, salvar e aplicar):

# Entre com o seguinte código dentro da função updateMessages:

def updateMessages(self):
    """Modify the messages created by internal validation for each tool
parameter. This method is called after internal validation."""
#A pasta de entrada não pode ser a mesma pasta de saída
    if str(self.params[0].value) == str(self.params[1].value):
        self.params[1].setErrorMessage("Input folder is the same as output folder")
    else:
        self.params[1].clearMessage()