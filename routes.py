"""
Routes and views for the bottle application.
"""
from datetime import datetime
from bottle import route, view

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """About page."""
    return dict(
        title='About',
        year=datetime.now().year
    )

@route('/alice')
@view('alice')
def alice():
    """Raising Alice page."""
    return dict(
        title='Raising Alice',
        year=datetime.now().year
    )

@route('/friends')
@view('friends')
def friends():
    """Friends page."""
    return dict(
        title='Friends of Jamie & Alice',
        year=datetime.now().year
    )

@route('/sysinfo')
@view('sysinfo')
def sysinfo():
    """Display runtime environment info."""
    pass # all functionality is in the sysinfo.tpl template

@route('/travel')
@view('travel')
def travel():
    """Travel Adventures page."""
    return dict(
        title='Travel Adventures',
        year=datetime.now().year
    )

