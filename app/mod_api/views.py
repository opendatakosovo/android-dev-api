from flask import Blueprint, render_template, Response, request
from flask.views import View
from bson import json_util
from app import mongo 

mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('', methods=['GET'])
def index():
    '''
    Show home page
    '''
    return 'Welcome to Shprehu API'

@mod_api.route('/version.json', methods=['GET'])
def get_app_version():
    ver_json = get_app_version_json()
    return Response(response=json_util.dumps(ver_json), status=200,  mimetype='application/json')

@mod_api.route('/config.json', methods=['GET'])
def get_app_config():
    cfg_json = get_app_config_json()
    return Response(response=json_util.dumps(cfg_json), status=200, mimetype='application/json')

@mod_api.route('/report', methods=['POST'])
def post_report():
    report = json_util.loads(request.data)
    print report
    return Response(status=200)

    
def get_app_config_json():
    json = {
        "_id":0,
        "types": [
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Verbal&w=300&h=300", 'id': 'verbal', 'name': 'Verbal'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Stalking&w=300&h=300", 'id': 'stalking', 'name': 'Stalking'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Groping&w=300&h=300", 'id': 'groping', 'name': 'Groping'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Assault&w=300&h=300", 'id': 'assault', 'name': 'Assault'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Flashing&w=300&h=300", 'id': 'flashing', 'name': 'Flashing'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Racism&w=300&h=300", 'id': 'racism', 'name': 'Racism'}
        ],
        "locations": [
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Home&w=300&h=300", 'id': 'home', 'name': 'Home'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Work&w=300&h=300", 'id': 'work', 'name': 'Work'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=School&w=300&h=300", 'id': 'school', 'name': 'School'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Public+Space&w=300&h=300", 'id': 'public_space', 'name': 'Public_Space'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Public+Transit&w=300&h=300", 'id': 'public_transit', 'name': 'Public_Transit'},
                {'imageUrl': "https://placeholdit.imgix.net/~text?txtsize=33&txt=Online&w=300&h=300", 'id': 'online', 'name': 'Online'}
        ]
    }

    return json


def get_app_version_json():
    json = {
        "versions":{
            "app": 0.1,
            "config": 0.1
        },
        "forceUpdate": False
    }

    return json