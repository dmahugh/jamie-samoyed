"""
Routes and views for the bottle application.
"""
import json

from datetime import datetime
from bottle import route, view, template

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict()

@route('/about')
@view('about')
def about():
    """About page."""
    return dict()

@route('/friends')
@view('friends')
def friends():
    """Friends page."""
    files = [photo['filename'] for photo in \
        json.loads(open('static/json/photos.json').read()) \
        if photo['album'] == 'friends']
    return dict(photos=files)

@route('/seattle')
@view('seattle')
def seattle():
    """Seattle page."""
    return dict()

@route('/sysinfo')
#@view('sysinfo')
def sysinfo():
    """Display runtime environment info."""
    return template('sysinfo.tpl')

@route('/travel')
@view('travel')
def travel():
    """Travel page."""
    return dict()
