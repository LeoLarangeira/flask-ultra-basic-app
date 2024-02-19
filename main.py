from flask import Flask, jsonify, render_template


app = Flask(__name__, template_folder='')
d = {
    "name": "Nikola", 
    "surname": "Tesla", 
    "idade": 60
      }


@app.route('/index')

def index():
    return '<h1>Hello world</h1>'



data = [
        {"Number": 1, "Name": "Teste", "Age": 22, "City": "São Paulo", "Country": "Brazil"},
        {"Number": 1, "Name": "Teste", "Age": 22, "City": "São Paulo", "Country": "Brazil"},
        {"Number": 1, "Name": "Teste", "Age": 22, "City": "São Paulo", "Country": "Brazil"},
        {"Number": 1, "Name": "Teste", "Age": 22, "City": "São Paulo", "Country": "Brazil"},
    ]
    #

@app.route('/')
def home():
    # Simular a leitura da planilha de dados
    # Retornar os dados como JSON
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run(debug=True)