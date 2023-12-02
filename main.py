from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamentos/')
def pagementos():
    return render_template('pagamentos.html')

@app.route('/pix')
def pix():
    return render_template('pix.html')

@app.route('/pix2')
def pix_password():
    return render_template('pix2.html')