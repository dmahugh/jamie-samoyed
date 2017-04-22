% rebase('layout.tpl', title='sysinfo')
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
% runtime_txt = open('runtime.txt', 'r').read() if os.path.isfile('runtime.txt') else ''
% requirements_txt = open('requirements.txt', 'r').read() if os.path.isfile('requirements.txt') else ''
% requirements_txt = requirements_txt.strip().replace('\n', '<br/>')

<table class="sysinfo">
  <tr><td colspan=2><h3>System Information</h3></td></tr>
  <tr><th valign="top">Python version:</th>
    <td>{{ py_version }}</td></tr>
  <tr><th>Python location:</th>
    <td>{{ sys.prefix }}</td></tr>
  <tr><th>Python packages:</th>
    <td>{{! '<br/>'.join([_ for _ in freeze.freeze()]) }}</td></tr>
  <tr><th>Python search path:</th>
    <td>{{! '<br/>'.join(sys.path) }}</td></tr>
  <tr><th>OS version:</th>
    <td>{{ platform.platform() }}</td></tr>
  <tr><th>Host machine name:</th>
    <td>{{ socket.gethostname() }}</td></tr>
  <tr><th>Server&nbsp;IP&nbsp;address:</th>
    <td>{{ socket.gethostbyname(socket.gethostname()) }}</td></tr>
  <tr><th>Client IP address:</th>
    <td>{{ client_ip }}</td></tr>
  <tr><th>Free disk space:</th>
    <td>{{! free_space }}</td></tr>
   <tr><th>Working directory:</th>
    <td>{{ os.getcwd() }}</td></tr>
   <tr><th>Files:</th>
    <td>{{ ', '.join([_ for _ in os.listdir() if os.path.isfile(_)]) }}</td></tr>
  <tr><th>runtime.txt:</th>
    <td>{{! runtime_txt }}</td></tr>
  <tr><th>requirements.txt:</th>
    <td>{{! requirements_txt }}</td></tr>
</table>

<hr />

<p><a href="https://bottlepy.org/docs/dev/"><img src="/static/images/sysinfo.jpg" align="center" class="img-responsive"/></a></p>
