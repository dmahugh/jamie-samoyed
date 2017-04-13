"""
Routes and views for the bottle application.
"""
import os
import platform
import shutil
import socket
import sys

from bottle import route, view
from datetime import datetime
from pip.operations import freeze

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
    """About page."""
    return dict(
        title='About',
        message='About page content.',
        year=datetime.now().year
    )

@route('/sysinfo')
@view('sysinfo')
def sysinfo():
    """Display runtime environment info."""
    #/// to ease moving to a sysinfo.tpl approach, this code is divided into
    # collecting the values (in Python) and rendering them (in HTML)

    # collect values
    os_version = platform.platform()
    total, used, free = shutil.disk_usage('/')
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    home_dir = os.getcwd()
    runtime_txt = \
        '<br/><b>runtime.txt:</b> ' + open('runtime.txt', 'r').read() \
        if os.path.isfile('runtime.txt') else ''

    return dict(
        title='System Information',
        year=datetime.now().year,
        py_version=sys.version,
        py_loc=sys.prefix,
        installed_pkgs=', '.join([_ for _ in freeze.freeze()]),
        sys_path = ', '.join(sys.path)
    )
    """
    # return rendered HTML
    return '<h1>System Info</h1>' + '<a href="/">return to home page</a>' + \
        '<p style="font-family:Consolas,Monaco,Lucida Console,Courier New, monospace">' + \
        '<b>Python version:</b>&nbsp;&nbsp;{0}'.format(py_ver) + '<br/>' + \
        '<b>Python location:</b> {0}'.format(py_loc) + '<br/><br/>' + \
        '<b>Installed packages:</b><br/>' + installed_pkgs + '<br/><br/>' + \
        '<b>Python search path (sys.path):</b><br/>' + py_path + '<br/><br/>' + \

        '<b>Operating system:</b> {0}'.format(os_version) + '<br/>' + \
        '<b>Disk total:</b> {0:,}'.format(total) + '<br/>' + \
        '<b>Disk used:</b>&nbsp;&nbsp;{0:,}'.format(used) + '<br/>' + \
        '<b>Disk free:</b>&nbsp;&nbsp;{0:,}'.format(free) + '<br/><br/>' + \
        '<b>Host name:</b>&nbsp;&nbsp;{0}'.format(hostname) + '<br/>' + \
        '<b>IP address:</b>&nbsp;&nbsp;{0}'.format(ip_addr) + '<br/><br/>' + \

        '<b>Home directory:</b>&nbsp;&nbsp;{0}'.format(home_dir) + \
        runtime_txt + '</p>'
    """
