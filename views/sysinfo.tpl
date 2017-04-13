% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}</h2>

<table>
<tr>
  <th valign="top">Python version:</th>
  <td>{{ py_version }}</td>
</tr>
<tr>
  <th>Python location:</th>
  <td>{{ py_loc }}</td>
</tr>
<tr>
  <th>Operating system:</th>
  <td>{{ os_version }}</td>
</tr>
<tr>
  <th>Host machine:</th>
  <td>{{ host_name }}</td>
</tr>
<tr>
  <th>IP address:</th>
  <td>{{ ip_addr }}</td>
</tr>
<tr>
  <th>Working directory:</th>
  <td>{{ home_dir }}</td>
</tr>
<tr>
  <th>runtime.txt:</th>
  <td>{{ runtime_txt }}</td>
</tr>
<tr>
  <th>Free disk space:</th>
  <td>{{ disk_free }}</td>
</tr>
<tr>
  <th valign="top">Installed packages:</th>
  <td>{{! '<br/>'.join(pkg_list) }}</td>
</tr>
<tr>
  <th valign="top">Python&nbsp;search&nbsp;path:</th>
  <td>{{! '<br/>'.join(sys_path) }}</td>
</tr>
</table>
