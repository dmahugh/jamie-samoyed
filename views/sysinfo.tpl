% rebase('layout.tpl', title='sysinfo')
% import os
% from misc import sysinfo
% sysdict = sysinfo()
% runtime_txt = open('runtime.txt', 'r').read() if os.path.isfile('runtime.txt') else ''
% free = int(sysdict['DISK_FREE'].replace(',', ''))
% total = int(sysdict['DISK_SIZE'].replace(',', ''))
% free_space = '{0} ({1}% of total)'. \
%     format(sysdict['DISK_FREE'], int(100*free/total))

<h2>System Information</h2>

<table class="sysinfo">
  <tr><th valign="top">Python version:</th>
    <td>{{ sysdict['PY_VERSION'] }}</td></tr>
  <tr><th>runtime.txt:</th>
    <td>{{! runtime_txt }}</td></tr>
  <tr><th>Python location:</th>
    <td>{{ sysdict['PY_LOCATION'] }}</td></tr>
  <tr><th>Python packages:</th>
    <td>{{! sysdict['PY_PACKAGES'].replace(',', '<br/>') }}</td></tr>
  <tr><th>Python&nbsp;search&nbsp;path:</th>
    <td>{{! sysdict['PY_PATH'] }}</td></tr>
  <tr><th>OS version:</th>
    <td>{{ sysdict['OS_VERSION'] }}</td></tr>
  <tr><th>Host&nbsp;machine&nbsp;name:</th>
    <td>{{ sysdict['HOST_NAME'] }}</td></tr>
  <tr><th>Processor:</th>
    <td>{{ sysdict['HOST_PROC'] }}</td></tr>
  <tr><th>Server IP address:</th>
    <td>{{ sysdict['HOST_IPADDR'] }}</td></tr>
  <tr><th>Client IP address:</th>
    <td>{{ client_ip }}</td></tr>
   <tr><th>Working directory:</th>
    <td>{{ sysdict['DIRECTORY'] }}</td></tr>
   <tr><th>Files:</th>
    <td>{{ ', '.join([_ for _ in os.listdir() if os.path.isfile(_)]) }}</td></tr>
  <tr><th>Free disk space:</th>
    <td>{{! free_space }}</td></tr>
</table>

<hr />

<p><a href="https://bottlepy.org/docs/dev/"><img src="/static/images/sysinfo.jpg" align="center" class="img-responsive"/></a></p>
