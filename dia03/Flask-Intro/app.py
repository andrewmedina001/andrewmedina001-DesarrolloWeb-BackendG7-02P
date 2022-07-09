from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

userss=[
    {
        'nombre':'Eduardo',
        'apellido':'De Rivero'
    },
    {
        'nombre':'Jorge',
        'apellido':'Garnica'
    }
]

@app.route('/')
def helloWorld():
    return 'Welcome to page of Hello World.'

@app.route('/alumns',methods=['GET'])
def listAlumns():
    return jsonify({
        'alumnos':userss
    })

@app.route('/name/<string:name>')
def name(name):
    return jsonify({
        'message':'Mi name is {}'.format(name)
    }),200

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        return 'This is a POST method of login()'
    else:
        return 'this is other method login'

@app.route('/users/<string:name>',methods=['GET'])
def users(name):
    for user in userss:
        if user['nombre']==name:
            return jsonify({
                'success':True,
                'message':'The user {} if exist.'.format(name),
                'content':user
            }),200
    return jsonify({
        'success':False,
        'message':'The user {} dont exist.'.format(name),
        'content':None
    }),400