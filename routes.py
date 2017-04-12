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
    return '<b>Python version & location:</b><br/>' + \
        sys.version + '<br/>' + sys.prefix + '<br/><br/>' + \
        '<b>Current working directory:</b></br>' + os.getcwd() + '<br/><br/>' + \
        '<b>sys.path:</b><br/>' + ('<br/>'.join(sys.path))
