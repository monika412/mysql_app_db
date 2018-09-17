from views.api import app
import pytest
import json
from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from validator import send_request_and_validate_response
from multiprocessing import Process
import time,os,sys

BASE_URL = 'http://127.0.0.1:8081/'

KEYSPACE = "fresco_seg"


cluster = Cluster()
session = cluster.connect(keyspace=KEYSPACE)


	
	
def setUp():
        #self.backup_items = deepcopy(app.items)  # no references!
		app = app.test_client()
		app.testing = True
#@pytest.fixture()
def test_number_of_clients():
	print('function')
	for i in range(1,300):
		p = Process(target=send_request_and_validate_response, args=(BASE_URL,))
		p.start()
		sys.stdout.write('calling process: ' + str(i)+'\n')
		time.sleep(1)
		p.join()

if __name__ == '__main__':
	test_number_of_clients()

