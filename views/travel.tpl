% rebase('layout.tpl', title='Travel')

<h2>Travel</h2>

<div id="myCarousel" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#myCarousel" data-slide-to="1"></li>
    <li data-target="#myCarousel" data-slide-to="2"></li>
    <li data-target="#myCarousel" data-slide-to="3"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="/static/photos/travel01.jpg" alt="Travel - xxx">
      <div class="carousel-caption">
        <h3>Travel - xxx</h3>
        <p>/// caption for travel01 ///</p>
      </div>
    </div>

    <div class="item">
      <img src="/static/photos/travel02.jpg" alt="Travel - xxx">
      <div class="carousel-caption">
        <h3>travel - xxx</h3>
        <p>/// caption for travel02 ///</p>
      </div>
    </div>

    <div class="item">
      <img src="/static/photos/travel03.jpg" alt="Travel - xxx">
      <div class="carousel-caption">
        <h3>travel - xxx</h3>
        <p>/// caption for travel03 ///</p>
      </div>
    </div>

    <div class="item">
      <img src="/static/photos/travel04.jpg" alt="Travel - xxx">
      <div class="carousel-caption">
        <h3>travel - xxx</h3>
        <p>/// caption for travel04 ///</p>
      </div>
    </div>

  </div>

  <!-- Left and right controls -->
  <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
