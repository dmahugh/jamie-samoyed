% rebase('layout.tpl', title=album_id)

<h2>{{ album_id }} photo album</h2>

% for filename in photos:
<div class="photo">
  <img src="/static/photos/{{ filename }}" alt="///description" class="img-responsive" /><br/>
  ///caption, ///location
</div>
