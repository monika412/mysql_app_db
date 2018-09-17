from flask_sqlalchemy import SQLAlchemy
#from conf import config
from flask import Flask
#app = Flask(__name__)
from conf.config import getMysqlConnection

db = SQLAlchemy()



class CustomerSeg(db.Model):
	__tablename__="customer_segment"
	party_id = db.Column(db.String(20),primary_key=True)
	fresco13_mseg = db.Column(db.String(5))
	fresco13_seg = db.Column(db.String(2))
	fresco13_sseg = db.Column(db.String(5))
	
	def get_data(self):
		return {
			'party_id': str(self.party_id),
			'fresco_mseg': str(self.fresco13_mseg),
			'fresco_seg': str(self.fresco13_seg),
			'fresco_sseg': str(self.fresco13_sseg),
			#'match_flag': str(self.match_flag)
		}

