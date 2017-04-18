% rebase('layout.tpl', title='unknown album')

<h2>Unknown album: {{ missing }}</h2>

<img src="/static/images/albumunknown.jpg" class="img-responsive"/>

<p>Try one of these albums instead:</p>

% for album in albums:
  <p><a href="/album/{{ album }}" class="btn btn-primary btn-responsive" role="button" width="400">{{ albums[album]['name'] }}</a></p>
% end

</table>
