% rebase('layout.tpl', title='Travel')

<h2>Travel</h2>

% for filename in photos:
<div class="photo">
  <img src="/static/photos/{{ filename }}" alt="///description" class="img-responsive" /><br/>
  ///caption, ///location
</div>
