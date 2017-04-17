"""
Routes and views for the bottle application.
"""
import json

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

def get_album():
    print('>>> get_album() called <<<')

@route('/sysinfo')
def sysinfo():
    """Display runtime environment info."""
    return template('sysinfo.tpl')
