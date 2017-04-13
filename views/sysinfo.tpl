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
  <th valign="top">Installed packages:</th>
  <td>{{ installed_pkgs }}</td>
</tr>
<tr>
  <th valign="top">Python&nbsp;search&nbsp;path:</th>
  <td>{{ sys_path }}</td>
<tr>
  <th>Operating system:</th>
  <td>{{ os_version }}</td>
</tr>
<tr>
  <th>Disk space - total:</th>
  <td>{{ disk_total }}</td>
</tr>
<tr>
  <th>Disk space - used:</th>
  <td>{{ disk_used }}</td>
</tr>
<tr>
  <th>Disk space - free:</th>
  <td>{{ disk_free }}</td>
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
</table>
