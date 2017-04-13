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

@route('/alice')
@view('alice')
def about():
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

    py_ver = sys.version.strip().split(' ')[0] + \
        (' (64-bit)' if '64 bit' in sys.version else ' (32-bit)')
    total, _, free = shutil.disk_usage('/')
    free_space = '{0}% &mdash; {1} bytes free'. \
        format(int(100*free/total), format(free, ','))

    return dict(
        title='System Information',
        year=datetime.now().year,
        py_version=py_ver,
        py_loc=sys.prefix,
        os_version=platform.platform(),
        disk_total=format(total, ','),
        disk_free=free_space,
        host_name=socket.gethostname(),
        ip_addr=socket.gethostbyname(socket.gethostname()),
        home_dir=os.getcwd(),
        runtime_txt=open('runtime.txt', 'r').read() \
            if os.path.isfile('runtime.txt') else '',
        pkg_list=[_ for _ in freeze.freeze()],
        sys_path=sys.path
    )

@route('/travel')
@view('travel')
def friends():
    """Travel Adventures page."""
    return dict(
        title='Travel Adventures',
        year=datetime.now().year
    )

