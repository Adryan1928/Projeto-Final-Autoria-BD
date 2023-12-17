from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/pix', methods=['GET', 'POST'])
def pix():
    if request.args.get('step') == 'select' or not request.args.get('step'):
        return render_template('pix.html')
    elif request.args.get('step') == 'confirm':
        return render_template('pix_confirm.html')
