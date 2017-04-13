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

@route('/about')
@view('about')
def about():
    """About page."""
    return dict(
        title='About',
        year=datetime.now().year
    )

@route('/sysinfo')
@view('sysinfo')
def sysinfo():
    """Display runtime environment info."""

    py_ver = sys.version.strip().split(' ')[0] + \
        (' (64-bit)' if '64 bit' in sys.version else ' (32-bit)')
    total, _, free = shutil.disk_usage('/')

    return dict(
        title='System Information',
        year=datetime.now().year,
        py_version=py_ver,
        py_loc=sys.prefix,
        os_version=platform.platform(),
        disk_total=format(total, ','),
        disk_free=format(free, ',') + \
            ' ({0}% of {1} total)'.format(int(100*free/total), format(total, ',')),
        host_name=socket.gethostname(),
        ip_addr=socket.gethostbyname(socket.gethostname()),
        home_dir=os.getcwd(),
        runtime_txt=open('runtime.txt', 'r').read() \
            if os.path.isfile('runtime.txt') else '',
        installed_pkgs='<br/>'.join([_ for _ in freeze.freeze()]),
        sys_path='<br/>'.join(sys.path)
    )
