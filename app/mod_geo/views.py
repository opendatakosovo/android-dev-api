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
    insert_sexual_harassment_types_into_database()
    return render_template('mod_geo/geo.html')


@mod_geo.route('geo-api', methods=['GET'])
def geo():

    json_obj = mongo.db.sht.find({})

    return Response(response=json_util.dumps(json_obj[0]['types']), mimetype='application/json')
    
    

    
def insert_sexual_harassment_types_into_database():

    mongo.db.sht.remove({})

    mongo.db.sht.insert({
        "_id":0,
        "types": [
            {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Verbal&w=300&h=300", 'id': 'verbal', 'name': 'Verbal'},
            {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Stalking&w=300&h=300", 'id': 'stalking', 'name': 'Stalking'},
            {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Groping&w=300&h=300", 'id': 'groping', 'name': 'Groping'},
            {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Assault&w=300&h=300", 'id': 'assault', 'name': 'Assault'},
            {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Flashing&w=300&h=300", 'id': 'flashing', 'name': 'Flashing'},
            {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Racism&w=300&h=300", 'id': 'racism', 'name': 'Racism'}
        ]
    })

