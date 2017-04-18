% rebase('layout.tpl', title='unknown album')

<h2>Unknown album: {{ missing }}</h2>

<p><img src="/static/images/albumunknown.jpg" class="img-responsive"/></p>

<p>Try one of these albums instead:</p>

% for album in albums:
    <p><a href="///">{{ albums[album]['name'] }}</a></p>
