"""
Routes and views for the bottle application.
"""
import os
import platform
import shutil
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
    total, used, free = shutil.disk_usage('/')
    return '<p style="font-family:Consolas,Monaco,Lucida Console,Courier New, monospace">' + \
        '<b>Python version:</b>&nbsp;&nbsp;{0}'.format(sys.version) + '<br/>' + \
        '<b>Python location:</b> {0}'.format(sys.prefix) + '<br/><br/>' + \
        '<b>Bottle version:</b>&nbsp;&nbsp;{0}'.format(bottle_version) + '<br/>' + \
        '<b>Bottle location:</b> {0}'.format(bottle_location) + '<br/><br/>' + \
        '<b>Python search path (sys.path)):</b><br/>' + ('<br/>'.join(sys.path)) + '<br/><br/>' + \
        '<b>Operating system:</b> {0}'.format(platform.platform()) + '<br/>' + \
        '<b>Disk total:</b> {0:,}'.format(total) + '<br/>' + \
        '<b>Disk used:</b>&nbsp;&nbsp;{0:,}'.format(used) + '<br/>' + \
        '<b>Disk free:</b>&nbsp;&nbsp;{0:,}'.format(free) + '<br/><br/>' + \
        '<b>Current directory:</b>&nbsp;&nbsp;{0}'.format(os.getcwd()) + '<br/>' + \
        '<b>Directory contents:</b> ' + str(sorted(os.listdir())) + '<br/>' + \
        '</p>' + '<a href="/">return to home page</a>'
