% from datetime import datetime
% rebase('layout.tpl', title='System Information', year=datetime.now().year)
% import os
% import platform
% import socket
% import sys
% import shutil
% from pip.operations import freeze
% from dougerino import sub_dir, bytecount
% py_version = sys.version.strip().split(' ')[0] + \
%     (' (64-bit)' if '64 bit' in sys.version else ' (32-bit)')
% total, _, free = shutil.disk_usage('/')
% free_space = '{0} ({1}% of {2} total)'. \
%     format(bytecount(free), int(100*free/total), bytecount(total))

<style>
th {text-align: right;
    vertical-align: text-top
    }
td {font-family:Consolas,Monaco,Lucida Console,Courier New, monospace;
    vertical-align: text-top
    }
</style>

<table>
  <tr><td></td><td><h3>Python Configuration</h3></td></tr>
  <tr><th valign="top">Version:</th>
    <td>{{ py_version }}</td></tr>
  <tr><th>Location:</th>
    <td>{{ sys.prefix }}</td></tr>
  <tr><th>Packages:</th>
    <td>{{! '<br/>'.join([_ for _ in freeze.freeze()]) }}</td></tr>
  <tr><th>Search path:</th>
    <td>{{! '<br/>'.join(sys.path) }}</td></tr>
  <tr><td></td><td><h3>Operating System</h3></td></tr>
  <tr><th>Version:</th>
    <td>{{ platform.platform() }}</td></tr>
  <tr><th>Host machine:</th>
    <td>{{ socket.gethostname() }}</td></tr>
  <tr><th>IP address:</th>
    <td>{{ socket.gethostbyname(socket.gethostname()) }}</td></tr>
  <tr><th>Free&nbsp;disk&nbsp;space:</th>
    <td>{{! free_space }}</td></tr>
  <tr><td></td><td><h3>Root Folder</h3></td></tr>
   <tr><th>Directory:</th>
    <td>{{ os.getcwd() }}</td></tr>
   <tr><th>Files:</th>
    <td>{{ ', '.join([_ for _ in os.listdir() if os.path.isfile(_)]) }}</td></tr>
  <tr><th>runtime.txt:</th>
    <td>{{ open('runtime.txt', 'r').read() if os.path.isfile('runtime.txt') else '' }}</td></tr>
  <tr><th>requirements.txt:</th>
    <td>{{ open('requirements.txt', 'r').read() if os.path.isfile('requirements.txt') else '' }}</td></tr>
  <tr><td></td><td><h3>File Locations</h3></td></tr>
  <tr><th>bottle.py:</th>
    <td>{{! '<br/>'.join(sub_dir('bottle.py'))}}</td></tr>
  <tr><th>dougerino.py:</th>
    <td>{{! '<br/>'.join(sub_dir('dougerino.py'))}}</td></tr>
</table>
