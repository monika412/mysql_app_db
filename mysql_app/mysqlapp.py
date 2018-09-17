from flask import Flask, jsonify
#from models.CustomerSeg import CustomerSeg
from views.api import app
from conf.config import getMysqlConnection
#from flask_mysql import MySQL
import mysql.connector

app = Flask(__name__)
#mysql = MySQL()
#mysql.init_app(app)


#conn = mysql.connect()

db=getMysqlConnection()



if __name__ == '__main__':
	 print ("in main")
	 synctable(CustomerSeg)
	 app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
	
	
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from conf import config

# def create_app(config_filename):
    # app = Flask(__name__)
    # app.config(config_filename)
    
    # #from app import api_bp
    # #app.register_blueprint(api_bp, url_prefix='/api')

    # from Model import db
    # db.init_app(app)

    # return app


# if __name__ == "__main__":
    # app = create_app("config")
    # app.run(debug=True)	