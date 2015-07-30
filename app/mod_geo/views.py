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
    insert_sexual_harassment_types_into_database()
    json_obj = mongo.db.sht.find({})

    return Response(response=json_util.dumps(json_obj[0]), mimetype='application/json')


@mod_geo.route('reports-api', methods=['GET'])
def reports():

    json_obj = mongo.db.sht.find({})

    return Response(response=json_util.dumps(json_obj[0]['locations']['reports']['types']), mimetype='application/json')

    
def insert_sexual_harassment_types_into_database():

    mongo.db.sht.remove({})

    mongo.db.sht.insert({
        "_id":0,
        "main_screen":{
            "types": [
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Report&w=300&h=300", 'id': 'report', 'name': 'Report'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Light&w=300&h=300", 'id': 'light', 'name': 'Light'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Maps&w=300&h=300", 'id': 'maps', 'name': 'Maps'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Analytics&w=300&h=300", 'id': 'analytics', 'name': 'Analytics'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Settings&w=300&h=300", 'id': 'settings', 'name': 'Settings'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Contact&w=300&h=300", 'id': 'contact', 'name': 'Contact'}
                ]
            },
        "reports":{
            "types": [
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Verbal&w=300&h=300", 'id': 'verbal', 'name': 'Verbal'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Stalking&w=300&h=300", 'id': 'stalking', 'name': 'Stalking'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Groping&w=300&h=300", 'id': 'groping', 'name': 'Groping'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Assault&w=300&h=300", 'id': 'assault', 'name': 'Assault'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Flashing&w=300&h=300", 'id': 'flashing', 'name': 'Flashing'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Racism&w=300&h=300", 'id': 'racism', 'name': 'Racism'}
                ]
            },
        "locations":{
            "types": [
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Home&w=300&h=300", 'id': 'home', 'name': 'Home'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Work&w=300&h=300", 'id': 'work', 'name': 'Work'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=School&w=300&h=300", 'id': 'school', 'name': 'School'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Public+Space&w=300&h=300", 'id': 'public_space', 'name': 'Public_Space'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Public+Transit&w=300&h=300", 'id': 'public_transit', 'name': 'Public_Transit'},
                    {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Online&w=300&h=300", 'id': 'online', 'name': 'Online'}
                ]
            }

    })

    