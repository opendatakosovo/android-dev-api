from flask import Blueprint, render_template
from flask.views import View

from app import mongo 

mod_geo = Blueprint('geo', __name__)
@mod_geo.route('/')
def geo():
	'''
	Show geos page!
	'''
	return render_template('mod_geo/index.html')