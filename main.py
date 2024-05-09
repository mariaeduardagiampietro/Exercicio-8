from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', resultado='')

@app.route('/verificar', methods=['POST'])  # Define uma rota '/verificar' que aceita apenas requisições POST
def verificar(): # Verifica a condição
    # Obtém o nome e a senha enviado no formulário HTML e verifica se são iguais ou não
    usuario = (request.form['usuario']) #
    senha = (request.form['senha'])
    if usuario == senha:
        resultado= "Erro! O usuário não pode ser igual a senha"
    else:
        resultado="Correto!"

    # Retorna o resultado da verificação diretamente no template 'index.html'
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    # Inicia o servidor Flask em modo de depuração se este script for executado diretamente
    app.run(debug=True)