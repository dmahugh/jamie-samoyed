"""
Routes for API endpoints.
"""
import json

from bottle import error, get, request, response, route, template, view
from misc import photo_list

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

@get('/api/album.html')
def api_album_html(): #------------------------------------------------------<<<
    """Pretty-printed version of /API/ALBUM endpoint.
    """
    response.headers['Cache-Control'] = 'no-cache'
    return template('prettyprint.tpl',
                    pprint_json=open('static/json/albums.json').read(),
                    api_route='/api/album.html')

@get('/api/album/<identifier>')
def api_album_by_id(identifier): #-------------------------------------------<<<
    """Handler for GET /API/ALBUM/<identifier> endpoint.
    """
    if identifier.lower().endswith('.html'):
        identifier = identifier.split('.')[0]
        html = True
    else:
        html = False

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

    # albumno = the key, identifier = what was passed in the URL

    retval = albumdict[albumno]
    retval['albumno'] = albumno # add albumno to returned dictionary
    retval['photos'] = photo_list(albumno) # add list of photos

    if html:
        response.headers['Cache-Control'] = 'no-cache'
        return template('prettyprint.tpl',
                        pprint_json=json.dumps(retval, indent=4),
                        api_route='/api/album/{0}.html'.format(identifier))
    else:
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
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
    if photono.lower().endswith('.html'):
        photono = photono.split('.')[0]
        html = True
    else:
        html = False

    photos = json.loads(open('static/json/photos.json').read())
    if not photono in photos:
        return dict(errmsg='unknown photo identifier: ' + photono)

    if html:
        response.headers['Cache-Control'] = 'no-cache'
        return template('prettyprint.tpl',
                        pprint_json=json.dumps(photos[photono], indent=4),
                        api_route='/api/photo/{0}.html'.format(photono))
    else:
        response.headers['Content-Type'] = 'application/json'
        response.headers['Cache-Control'] = 'no-cache'
        return photos[photono]
