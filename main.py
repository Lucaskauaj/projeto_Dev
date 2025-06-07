from flask import Flask,render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/List')
def list_contatos():
    return render_template('List_contato.html')
@app.route('/arquivos')
def enviar_arquivos():
    return render_template('envio_arquivos.html')
@app.route('/adicionar_cont')
def adicionar_cont():
    return render_template('adicionar_cont.html')
if __name__ == '__main__':
    app.run(debug=True)
