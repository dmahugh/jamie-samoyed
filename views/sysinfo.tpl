% from datetime import datetime
% rebase('layout.tpl', title='System Information', year=datetime.now().year)
% import os
% import platform
% import socket
% import sys
% import shutil
% from pip.operations import freeze

%py_version = sys.version.strip().split(' ')[0] + \
%    (' (64-bit)' if '64 bit' in sys.version else ' (32-bit)')
% total, _, free = shutil.disk_usage('/')
% free_space = '{0}% &mdash; {1} bytes free'. \
%     format(int(100*free/total), format(free, ','))

<h2>System Information</h2>

<style>td {font-family:Consolas,Monaco,Lucida Console,Courier New, monospace}</style>
<table>
<tr>
  <th valign="top">Python version:</th>
  <td>{{ py_version }}</td>
</tr>
<tr>
  <th>Python location:</th>
  <td>{{ sys.prefix }}</td>
</tr>
<tr>
  <th>Operating system:</th>
  <td>{{ platform.platform() }}</td>
</tr>
<tr>
  <th>Host machine:</th>
  <td>{{ socket.gethostname() }}</td>
</tr>
<tr>
  <th>IP address:</th>
  <td>{{ socket.gethostbyname(socket.gethostname()) }}</td>
</tr>
<tr>
  <th>Working directory:</th>
  <td>{{ os.getcwd() }}</td>
</tr>
<tr>
  <th>runtime.txt:</th>
  <td>{{ open('runtime.txt', 'r').read() if os.path.isfile('runtime.txt') else '' }}</td>
</tr>
<tr>
  <th>Free disk space:</th>
  <td>{{! free_space }}</td>
</tr>
<tr>
  <th valign="top">Installed packages:</th>
  <td>{{! '<br/>'.join([_ for _ in freeze.freeze()]) }}</td>
</tr>
<tr>
  <th valign="top">Python&nbsp;search&nbsp;path:</th>
  <td>{{! '<br/>'.join(sys.path) }}</td>
</tr>
</table>
