% rebase('layout.tpl', title='Travel')

<h2>Travel</h2>

<div class="photo">
  <img src="/static/photos/travel01.jpg" alt="Pacific Ocean beach" align="center" class="img-responsive">
  <h2 class="caption"><span>Crescent City, CA<span class="spacer"></span><br/><span class="spacer"></span>Pacific Ocean beach</span></h2>
</div>

% for filename in photos:
<p><img src="/static/photos/{{ filename }}" align="center" class="img-responsive"/></p>

