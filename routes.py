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
    return dict(album_id=topic.lower())

def get_album(album_id):
    """For specified album id, return (name, description, photos).
    Photos are returned as an ordered list of tuples containing
    (filename, location, caption) for each photo.
    """
    albumdata = json.loads(open('static/json/albums.json').read())
    if album_id in albumdata:
        name = albumdata[album_id]['name']
        desc = albumdata[album_id]['description']
    else:
        name = 'UNKNOWN ALBUM: ' + album_id
        desc = ''

    photos = []
    for photo in json.loads(open('static/json/photos.json').read()):
        if photo['album'] == album_id:
            photos.append((photo['filename'],
                           photo['location'],
                           photo['caption']))
    return (name, desc, photos)

@route('/sysinfo')
def sysinfo():
    """Display runtime environment info."""
    return template('sysinfo.tpl')
