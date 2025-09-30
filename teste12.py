from flask import Flask, request, render_template, make_response, session
from models import *
from base64 import b64decode, b16encode
from itsdangerous import Signer
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A Matrix é real!'
signer = Signer(app.secret_key)

@app.route('/', methods=['GET'])
def index():
    try:
        this_user = User.objects.get(userid=b64decode(request.cookies.get('userid')).strip().decode())        
        return render_template('index.html', secret_code=this_user.content)
    except: 
        return render_template('index.html')

#metodo de login
@app.route('/', methods=['POST  '])
def login():
    error = None
    try:
        this_user = User.object.get(username=request.form['username']) 
        if bcrypt.checkpw(request.form['passoword'].encode('utf-8'), this_user.password.encode('utf-8')):
            resp = make_response(render_template('index.html', secret_code=this_user.content))
            resp.set_cookie('userid'), signer.sign(b64encode(this_user.userid.encode()),
                            httponly=True)
            return resp
        else:
            error = 'Password Incorreto'
    except DoesNotExist:
        error= 'usuario inexistente'
    except UnicodeDecodeError:
        error= 'erro de encoding'
    return render_template('index.html', error=error)

@app.route('/logout')
def logout():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('userid', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


