% rebase('layout.tpl', title='Travel')

<h2>Travel</h2>

% for filename in photos:
<div class="photo">
  <img src="/static/photos/{{ filename }}" alt="Pacific Ocean beach" align="center" class="img-responsive">
  <h2 class="caption"><span>///location<span class="spacer"></span><br/><span class="spacer"></span>/// caption</span></h2>
</div>


