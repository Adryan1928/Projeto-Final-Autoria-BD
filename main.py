from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagamentos/')
def pagementos():
    return render_template('pagamentos.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/pix', methods=['GET', 'POST'])
def pix():
    if request.args.get('step') == 'select' or not request.args.get('step'):
        return render_template('pix.html')
    elif request.args.get('step') == 'confirm':
        return render_template('pix_confirm.html')

@app.route('/real-state-financing/')
def real_state_financing():
    return render_template('financing.html')