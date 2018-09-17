#from flask import Flask
#from flask_mysql import MySQL


#mysql = MySQL()
#app = Flask(__name__)

# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
#app.config['MYSQL_DATABASE_DB'] = 'fresco_segment'
##app.config['MYSQL_DATABASE_HOST'] = 'mysqldb'
#mysql.init_app(app)


import mysql.connector
db_host='localhost'
database='fresco_segment'
def getMysqlConnection():
    return mysql.connector.connect(host=db_host,database=database,user='root',password='root')