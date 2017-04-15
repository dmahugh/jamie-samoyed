% rebase('layout.tpl', title='Travel')

<h2>Travel</h2>

% for filename in photos:
<p><img src="/static/photos/{{ filename }}" align="center" class="img-responsive"/></p>
