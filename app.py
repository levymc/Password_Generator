from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tamanho = 10
    caracteres = string.ascii_letters + string.digits

    if request.method == 'POST':
        tamanho = int(request.values.get('tamanho')) if int(request.values.get('tamanho')) else 0

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))

    return render_template('index.html', senha=senha)

if __name__ == '__main__':
    app.run(debug=True, port=2500)
