from flask import Flask, render_template, request, url_for, redirect
import model
import time
from pprint import pprint

app = Flask(__name__)
app.jinja_env.autoescape = True

@app.route('/')
def home():
    posts = model.obter_posts()
    print(posts)
    return render_template('home.html',posts=posts)

@app.route('/postar/', methods=['GET','POST'])
def postar():
    if request.method == 'GET':
        return render_template('postar.html')
    else:
        texto = request.form['texto']
        horario = time.time()
        
        model.postar(texto, horario)
        return redirect(url_for('home'))
    
@app.route('/post/<id>', methods=['GET'])
def post(id):
    texto = model.obter_posts(id)[0]['texto']
    hora = model.obter_posts(id)[0]['hora']
    data = model.obter_posts(id)[0]['data']
    return render_template('post.html',texto=texto,hora = hora,data=data)

app.run(debug=True)
