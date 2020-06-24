from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/facil.html')
def facil():
    return render_template('facil.html')

@app.route('/medio.html')
def medio():
    return render_template('medio.html')

@app.route('/dificil.html')
def dificil():
    return render_template('dificil.html')

@app.route('/acertar')
def acertar():
	var = request.args['palpite']  # Criei uma variavel, chamada var, que recebe os valores que a classe request.args captura. 
	return render_template('acertou.html', nome=var )

if __name__ == '_main_':
    app.run(debug=True,port=5000)
   

# @app.route('/votar')
# def votar():
# 	var = request.args['nome']
# 	return render_template('votou.html', nome=var	)