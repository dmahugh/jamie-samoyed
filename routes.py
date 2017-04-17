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

@route('/album/<topic>')
@view('album')
def album(topic):
    """Album pages."""
    files = [photo['filename'] for photo in \
        json.loads(open('static/json/photos.json').read()) \
        if photo['album'] == topic.lower()]
    return dict(photos=files, album_id=topic.lower())

@route('/sysinfo')
#@view('sysinfo')
def sysinfo():
    """Display runtime environment info."""
    return template('sysinfo.tpl')
