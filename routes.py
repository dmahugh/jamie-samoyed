"""
Routes and views for the bottle application.
"""
import os
import sys

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """About page displays Python configuration info."""
    bottle_version = getattr(sys.modules['bottle'], '__version__', 'unknown')
    bottle_location = getattr(sys.modules['bottle'], '__file__', 'unknown')
    return '<b>Python version:</b> {0}'.format(sys.version) + '<br/>' + \
        '<b>Python location:</b> {0}'.format(sys.prefix) + '<br/>' + \
        '<b>Current folder:</b> {0}'.format(os.getcwd()) + '<br/>' + \
        '<b>Bottle version:</b> {0}'.format(bottle_version) + '<br/>' + \
        '<b>Bottle location:</b> {0}'.format(bottle_location) + '<br/><br/>' + \
        '<b>sys.path (Python search path):</b><br/>' + ('<br/>'.join(sys.path))
