% rebase('layout.tpl', title=albumno, albumdict=albumdata)
% from routes import get_album
% albumno, name, desc, photos = get_album(albumno, albumdata)

<h2>{{ name }}</h2>

<p>{{! desc }}</p>

% for photo in photos:
<div class="photo">
  <a href="{{ photo[1] }}">
  <img src="{{ photo[1] }}" alt="{{ photo[2] }}" class="img-responsive" /></a>
  <p>{{! photo[3] + (' &mdash; ' if photo[2] and photo[3] else '') + photo[2] }}</p>
</div>
