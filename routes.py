"""
Routes and views for the bottle application.
"""
import json

from bottle import route, view, template, error

@route('/about')
@view('about')
def about(): #---------------------------------------------------------------<<<
    """About page."""
    return dict()

@route('/album/<topic>')
@view('album')
def album(topic): #----------------------------------------------------------<<<
    """Album pages."""
    albumdict = get_albums()
    if not topic.lower() in albumdict:
        return '***ERROR*** UNKNOWN ALBUM: ' + topic
    return dict(album_id=topic.lower(), albumdata=albumdict)

@error(404) # this function will be invoked for HTTP status code 404 errors
@view('404error')
def custom404handler(error): #-----------------------------------------------<<<
    """Custom handler for 404 errors."""
    return dict(error=error)

def get_album(album_id, albumdict=None): #-----------------------------------<<<
    """For specified album id, return (name, description, photos).
    albumdict is optional; can be passed to avoid re-creating it.
    Photos are returned as an ordered list of tuples containing
    (filename, location, caption) for each photo.
    """
    if not albumdict:
        albumdict = get_albums()
    if album_id in albumdict:
        name = albumdict[album_id]['name']
        desc = albumdict[album_id]['description']
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

def get_albums(): #----------------------------------------------------------<<<
    """Create dictionary of album metadata from albums.json."""
    return json.loads(open('static/json/albums.json').read())

@route('/')
@route('/home')
@view('index')
def home(): #----------------------------------------------------------------<<<
    """Renders the home page."""
    return dict()

@route('/sysinfo')
def sysinfo(): #-------------------------------------------------------------<<<
    """Display runtime environment info."""
    return template('sysinfo.tpl')
