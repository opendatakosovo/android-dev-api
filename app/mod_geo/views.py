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

    json_obj = json_util.loads(request.data)
    
    mongo.db.geodata.remove({})
    
    mongo.db.geodata.insert(json_obj)
    
    return Response(status=200)
