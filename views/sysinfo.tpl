% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}</h2>

<table>
<tr>
  <th>Python version:</th>
  <td>{{ py_version }}</td>
</tr>
<tr>
  <th>Python location:</th>
  <td>{{ py_loc }}</td>
</tr>
<tr>
  <th>Installed packages:</th>
  <td>{{ installed_pkgs }}</td>
</tr>
<tr>
  <th>Python search path:</th>
  <td>{{ sys_path }}</td>
</tr>
</table>
