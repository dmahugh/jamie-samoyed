% rebase('layout.tpl', title='unknown album')

<h2>Unknown album: {{ missing }}</h2>

<table>
<tr><td><img src="/static/images/albumunknown.jpg" class="img-responsive"/></td></tr>

<tr><td>Try one of these albums instead:</td></tr>

% for album in albums:
  <tr><td style="padding: 4px"><a href="/album/{{ album }}" class="btn btn-primary" role="button" style="width: 100%">{{ albums[album]['name'] }}</a></td></tr>
% end

</table>
