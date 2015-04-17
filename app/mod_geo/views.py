from flask import Blueprint, render_template, Response, request
from flask.views import View
from bson import json_util
from app import mongo 

mod_geo = Blueprint('geo', __name__, url_prefix='/')

@mod_geo.route('', methods=['GET'])
def home():
	'''
	Show home page
	'''
	return render_template('mod_geo/geo.html')


@mod_geo.route('geo-api', methods=['POST'])
def geo():
	json_string = request.data
	json_obj = json_util.loads(json_string)
	print request.data
	mongo.db.geodata.insert(json_obj)
	
	resp = Response(status=200, mimetype='application/json')

	return resp