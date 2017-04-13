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
    total, used, free = shutil.disk_usage('/')

    return dict(
        title='System Information',
        year=datetime.now().year,
        py_version=sys.version,
        py_loc=sys.prefix,
        installed_pkgs=', '.join([_ for _ in freeze.freeze()]),
        sys_path=', '.join(sys.path),
        os_version=platform.platform(),
        disk_total=total,
        disk_used=used,
        disk_free=free,
        host_name=socket.gethostname(),
        ip_addr=socket.gethostbyname(socket.gethostname()),
        home_dir=os.getcwd(),
        runtime_txt=open('runtime.txt', 'r').read() \
            if os.path.isfile('runtime.txt') else ''
    )
