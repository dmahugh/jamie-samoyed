% rebase('layout.tpl', title='Friends')

<h2>Friends</h2>

% for filename in photos:
<p><img src="/static/photos/{{ filename }}" align="center" class="img-responsive"/></p>
