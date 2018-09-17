import json, os
from flask import Flask, jsonify, request, abort
from flask_restplus import Resource, Api
from models.CustomerSeg import CustomerSeg
from functools import wraps
from binascii import hexlify
from flask.views import MethodView


key = hexlify(os.urandom(40))
print (key)
generate_key ='6632a4056249a1d63160e0e9f52b52738b7ed5585b63c92c0647195aee803b3efc23b752f6534a41'
app = Flask(__name__)
#api = Api(app)
app.debug = True


# using api key ##

# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if request.headers.get('API-Key') and request.headers.get('API-Key') == generate_key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

	
@app.route('/api')
def home():
	key = request.headers.get('API-Key')
	print (key)
	return 'GOT the %s key'%key


	
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'API-Key'
    }
}
def apikey(func):
    return api.doc(security='apikey')(func)	
api = Api(app, authorizations=authorizations,security='apikey')	

	
##using erorr handler as decorator	
@app.errorhandler(404)
def not_found(error=None):
		message = {
			'status': 404,
			'message': 'Invalid Input : Input Value doesnot exist' 
		}
		resp = jsonify(message)
		resp.status_code = 404
		return resp


api.namespaces.clear()
ns = api.namespace('fresco', description='Operations related to user segmentations')
	
@ns.route('/hello')
class HelloWorld(Resource):
	def get(self):
		"""Start of API"""
		return ("Hello! This is a mock api for Fresco(testing Flask with mysql)")
#api.add_resource(HelloWorld, '/')

api.add_namespace(ns)



@ns.route('/users')
#@ns.apiKey(generate_key)
class UserAll(Resource):
	#@require_appkey
	#@apikey
	#@api.doc(security='apikey')
	def get(self):
		"""Returns details of All Users"""
	#	.filter(party_id).all()
		users = CustomerSeg.objects.all()
		user=[user.get_data() for user in users]
		return (user)

#api.add_resource(UserAll, '/users')
#@api.response(201, 'Category successfully created.')

#@apis.route("/user/<fresco13_seg>")

@ns.route('/users/<id>')
class UserSearch(Resource):
	
	def get(self,id):
		"""Returns details of only selected Users"""
		
		users = CustomerSeg.objects.all().filter(party_id=id)
		user=[user.get_data() for user in users]
		if (len(user)) != 0:
			return (user)
		else: 
			return not_found()
		
#api.add_resource(UserSearch, '/users/<id>')



@ns.route('/user_seg')
class UserAllSegment(Resource):
	
	def get(self):
		"""Returns list of all segments"""
		users = CustomerSeg.objects.all()
		user=list(set([user.fresco13_seg for user in users]))
		return (user)
#api.add_resource(UserAllSegment, '/user_seg')

@ns.route('/user_seg/<seg_cd>')
@api.response(200, 'Segment found.')
@api.response(404, 'Segment not found.')
@api.doc(params={'seg_cd': 'An ID'})
class UserSegment(Resource):
	
	def get(self,seg_cd):
		"""Returns list of all users in the selected segment"""
		users = CustomerSeg.objects.all().filter(fresco13_seg=seg_cd)
		userseg=[user.get_data() for user in users]
		if (len(userseg)) != 0:
			return (userseg)
		else: 
			return not_found()

