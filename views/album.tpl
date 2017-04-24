% rebase('layout.tpl', title=albumno, albumdict=albumdata)
% from routes import get_album
% albumno, name, desc, photos = get_album(albumno, albumdata)

<h2>{{ name }}</h2>

<p>{{! desc }}</p>

% for photo in photos:
<div class="photo">
  <a href="{{ photo['filename'] }}">
  <img src="{{ photo['filename'] }}" alt="{{ photo['location'] }}" class="img-responsive" /></a>
  <p>{{! photo['caption'] + (' &mdash; ' if photo['location'] and photo['caption'] else '') + photo['location'] }}</p>
</div>
% end
