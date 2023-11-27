from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamentos/')
def pagementos():
    return render_template('pagamentos.html')