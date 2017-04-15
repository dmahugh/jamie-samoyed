% rebase('layout.tpl', title='Seattle')

<h2>Seattle</h2>

% for filename in photos:
<p><img src="/static/photos/{{ filename }}" align="center" class="img-responsive"/></p>
