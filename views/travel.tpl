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
      <img src="/static/photos/travel01.jpg" alt="Crescent City, California">
      <div class="carousel-caption">
        <h3>Crescent City, California</h3>
        <p>early morning on a Pacific Ocean beach</p>
      </div>
    </div>

    <div class="item">
      <img src="/static/photos/travel02.jpg" alt="Gulfport, Mississippi">
      <div class="carousel-caption">
        <h3>Gulfport, Mississippi</h3>
        <p>Playing in the Gulf of Mexico</p>
      </div>
    </div>

    <div class="item">
      <img src="/static/photos/travel03.jpg" alt="Alberta, Canada">
      <div class="carousel-caption">
        <h3>Alberta, Canada</h3>
        <p>Approaching the top of Whistler Summit</p>
      </div>
    </div>

    <div class="item">
      <img src="/static/photos/travel04.jpg" alt="San Francisco, California">
      <div class="carousel-caption">
        <h3>San Francisco, California</h3>
        <p>Golden Gate Bridge</p>
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
