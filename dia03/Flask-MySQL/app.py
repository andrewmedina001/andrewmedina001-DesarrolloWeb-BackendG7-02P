from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
# name of database
app.config['MYSQL_DB']='vacunaciones02'
mysql=MySQL(app)


@app.route('/')
def index():
    return 'The SERVER is functional'

@app.route('/prove')
def conexion():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM campanias")
    data=cur.fetchall()
    data_serializada=[]

    # cur.close()
    # for dat in data:
    #     data_serializada.append(dat)
    # print(cur)
    return str(data)