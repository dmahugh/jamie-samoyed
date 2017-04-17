% from routes import get_album
% name, desc, photos = get_album(album_id)
% rebase('layout.tpl', title=album_id)

<h2>{{ name }}</h2>

<p>{{! desc }}</p>

% for photo in photos:
<div class="photo">
  <img src="/static/photos/{{ photo[0] }}" alt="{{ photo[1] }}" class="img-responsive" />
  <p>{{ photo[2] + ' @ ' + photo[1] }}</p>
</div>
