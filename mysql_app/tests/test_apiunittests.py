from views.api import app
import unittest
import json
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection

BASE_URL = 'http://127.0.0.1:8081/users'
BAD_USR_URL = '{}/5'.format(BASE_URL)
GOOD_USR_URL = '{}/114215967'.format(BASE_URL)

BASE_SEG_URL = 'http://127.0.0.1:8081/user_seg'
BAD_SEG_URL = '{}/50'.format(BASE_SEG_URL)
GOOD_SEG_URL = '{}/3'.format(BASE_SEG_URL)

KEYSPACE = "fresco_seg"


cluster = Cluster()
session = cluster.connect(keyspace=KEYSPACE)

class TestIntegrations(unittest.TestCase):

	#def test_table(self):
	
	
	def setUp(self):
        #self.backup_items = deepcopy(app.items)  # no references!
		self.app = app.test_client()
		self.app.testing = True
		
	def test_01_get_verify(self):
		""" Test that the flask server is running and reachable"""
		r = self.app.get('http://127.0.0.1:8081')
		self.assertEqual(r.status_code, 200)

	def test_get_users(self):
		response = self.app.get(BASE_URL)
		data = json.loads(response.get_data())
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(data), 400)
		
	# def test_get_user(self):
		# response = self.app.get(BASE_URL)
		# data = json.loads(response.get_data())
		# self.assertEqual(response.status_code, 200)
		# self.assertEqual(data[0]['party_id'], '123')

	def test_user_exist(self):
		response = self.app.get(GOOD_USR_URL)
		self.assertEqual(response.status_code, 200)
	

	def test_user_not_exist(self):
		response = self.app.get(BAD_USR_URL)
		self.assertEqual(response.status_code, 404)
	
	def test_seg_exist(self):
		response = self.app.get(GOOD_SEG_URL)
		self.assertEqual(response.status_code, 200)
	
	def test_segment_not_exist(self):
		response = self.app.get(BAD_SEG_URL)
		self.assertEqual(response.status_code, 404)
		

		
if __name__ == "__main__":
	connection.setup(['127.0.0.1'], KEYSPACE, protocol_version=3)
	unittest.main()