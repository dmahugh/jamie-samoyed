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

@route('/album/<albumname>')
@view('album')
def album(albumname):
    """Album pages."""
    #/// handle case sensitivity
    #/// validate album name against albums.json, if not valid return error with
    #    a list of links to valid albums
    files = [photo['filename'] for photo in \
        json.loads(open('static/json/photos.json').read()) \
        if photo['album'] == albumname]
    return dict(photos=files, album=albumname)

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
    files = [photo['filename'] for photo in \
        json.loads(open('static/json/photos.json').read()) \
        if photo['album'] == 'seattle']
    return dict(photos=files)

@route('/sysinfo')
#@view('sysinfo')
def sysinfo():
    """Display runtime environment info."""
    return template('sysinfo.tpl')

@route('/travel')
@view('travel')
def travel():
    """Travel page."""
    files = [photo['filename'] for photo in \
        json.loads(open('static/json/photos.json').read()) \
        if photo['album'] == 'travel']
    return dict(photos=files)
