"""
Routes and views for the bottle application.
"""
import json

from bottle import error, get, request, response, route, template, view
from misc import photo_list


@route("/about")
@view("about")
def about():
    """About page - about.tpl"""
    return dict()


@route("/album/<albumno>")
@view("album")
def album(albumno):
    """Album pages."""
    albumdict = get_albums()
    if not albumno in albumdict:
        return template("albumunknown.tpl", missing=albumno, albums=albumdict)
    return dict(albumno=albumno, albumdata=albumdict)


@error(404)  # this function will be invoked for HTTP status code 404 errors
@view("404error")
def custom404handler(error):
    """Custom handler for 404 errors."""
    return dict(err=error)


def get_album(albumno, albumdict=None):
    """For specified albumno, return (slug, name, description, photos).
    albumdict is optional; can be passed to avoid re-creating it.
    Photos are returned as an ordered list of tuples containing
    (photono, filename, location, caption) for each photo.
    """

    if not albumdict:
        albumdict = get_albums()
    if albumno in albumdict:
        slug = albumdict[albumno]["slug"]
        name = albumdict[albumno]["name"]
        desc = albumdict[albumno]["description"]
    else:
        name = "UNKNOWN ALBUM: " + albumno
        desc = ""

    return (slug, name, desc, photo_list(albumno))


def get_albums():
    """Create dictionary of album metadata from albums.json."""
    return json.loads(open("static/json/albums.json").read())


@route("/")
@route("/home")
@view("index")
def home():
    """Renders the home page."""
    return dict()


@route("/sysinfo")
@view("sysinfo")
def sysinfo():
    """Display runtime environment info."""
    return dict(client_ip=request.environ.get("REMOTE_ADDR"))
