"""
Routes and views for the bottle application.
"""
import json

from bottle import error, get, request, response, route, template, view

@route('/about')
@view('about')
def about(): #---------------------------------------------------------------<<<
    """About page - about.tpl"""
    return dict()

@route('/album/<albumno>')
@view('album')
def album(albumno): #--------------------------------------------------------<<<
    """Album pages."""
    albumdict = get_albums()
    if not albumno in albumdict:
        return template('albumunknown.tpl', missing=albumno, albums=albumdict)
    return dict(albumno=albumno, albumdata=albumdict)

@route('/api')
@view('api')
def api(): #-----------------------------------------------------------------<<<
    """API home page."""
    return dict()

@get('/api/album')
def api_album(): #-----------------------------------------------------------<<<
    """Handler for GET /API/ALBUM endpoint.
    """
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.loads(open('static/json/albums.json').read())

@get('/api/album/<identifier>')
def api_album_by_id(identifier): #-------------------------------------------<<<
    """Handler for GET /API/ALBUM/<identifier> endpoint.
    """
    albumdict = json.loads(open('static/json/albums.json').read())
    if identifier in albumdict:
        albumno = identifier
    else:
        for albumnum in albumdict:
            if albumdict[albumnum]['slug'] == identifier.lower():
                albumno = albumnum
                break
        if not 'albumno' in locals():
            return dict(errmsg='unknown album identifier: ' + identifier)

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    retval = albumdict[albumno]
    retval['albumno'] = albumno # add albumno to returned dictionary
    retval['photos'] = photo_list(albumno) # add list of photos
    return retval

@get('/api/photo')
def api_photo(): #-----------------------------------------------------------<<<
    """Handler for GET /API/PHOTO endpoint.
    """
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.loads(open('static/json/photos.json').read())

@get('/api/photo.html')
def api_photo_html(): #------------------------------------------------------<<<
    """Pretty-printed HTML version of /API/PHOTO endpoint.
    """
    response.headers['Cache-Control'] = 'no-cache'
    data = open('static/json/photos.json').read()
    return template('prettyprint.tpl', pprint_json=data, api_route='/api/photo')

@get('/api/photo/<photono>')
def api_photono(photono): #--------------------------------------------------<<<
    """Handler for GET /API/PHOTO/<photono> endpoint.
    """
    photos = json.loads(open('static/json/photos.json').read())
    if not photono in photos:
        return dict(errmsg='unknown photo identifier: ' + photono)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return photos[photono]

@error(404) # this function will be invoked for HTTP status code 404 errors
@view('404error')
def custom404handler(error): #-----------------------------------------------<<<
    """Custom handler for 404 errors."""
    return dict(err=error)

def get_album(albumno, albumdict=None): #-----------------------------------<<<
    """For specified albumno, return (slug, name, description, photos).
    albumdict is optional; can be passed to avoid re-creating it.
    Photos are returned as an ordered list of tuples containing
    (photono, filename, location, caption) for each photo.
    """

    if not albumdict:
        albumdict = get_albums()
    if albumno in albumdict:
        slug = albumdict[albumno]['slug']
        name = albumdict[albumno]['name']
        desc = albumdict[albumno]['description']
    else:
        name = 'UNKNOWN ALBUM: ' + albumno
        desc = ''

    return (slug, name, desc, photo_list(albumno))

def get_albums(): #----------------------------------------------------------<<<
    """Create dictionary of album metadata from albums.json."""
    return json.loads(open('static/json/albums.json').read())

@route('/')
@route('/home')
@view('index')
def home(): #----------------------------------------------------------------<<<
    """Renders the home page."""
    return dict()

def photo_list(albumno): #---------------------------------------------------<<<
    """Return list of photos for specified album.
    Return list contains tuples of (photono, filename, location, caption)
    """
    photodata = json.loads(open('static/json/photos.json').read())
    photolist = []
    for photono in photodata:
        if photodata[photono]['albumno'] == albumno:
            photolist.append((photono,
                              photodata[photono]['filename'],
                              photodata[photono]['location'],
                              photodata[photono]['caption']))
    return sorted(photolist, key=lambda _: _[1].upper()) # sort by filename

@route('/sysinfo')
@view('sysinfo')
def sysinfo(): #-------------------------------------------------------------<<<
    """Display runtime environment info."""
    return dict(client_ip=request.environ.get('REMOTE_ADDR'))
