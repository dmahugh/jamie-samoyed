"""
Routes and views for the bottle application.
"""
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
    """Renders the about page."""
    #return dict(
    #    title='About the runtime environment',
    #    message='Python version: ' + sys.version + ' >>>>> sys.path: ' + str(sys.path),
    #    year=datetime.now().year
    #)
    return '<b>Python version:</b><br/>' + \
        sys.version + '<br/><br/><b>sys.path:</b><br/>' + \
        ('<br/>'.join(sys.path))
