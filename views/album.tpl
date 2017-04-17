% rebase('layout.tpl', title=album)

<h2>{{ album.upper() }} photo album</h2>

% for filename in photos:
<div class="photo">
  <img src="/static/photos/{{ filename }}" alt="///description" class="img-responsive" /><br/>
  ///caption, ///location
</div>
