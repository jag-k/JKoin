<!--
<div id="header">
    <a href="/">
        <div class="headimgs" id="upbutton_img">
            <img src="static/image/head.png" class="headimg head1" alt="Image not load(" height="100", width=300>
        </div>
    </a>
    <div id="button_container">
        <div class="buttons" id="upbutton_container">
            <a href="/" class="upbut">Home</a>
            <a href="/wallet" class="upbut">Wallet</a>
            <a href="/top" class="upbut">Top</a>
        </div>
    </div>
</div>
<script type="text/javascript" src="static/js/head.js"></script>
-->

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="/">JKoin</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="/">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/top">Top</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/wallet">Wallet</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/transfer">JKoin Transfer</a>
      </li>
    </ul>
  </div>
</nav>

<script>
    var loc = location.pathname;
    var elementsList = document.getElementsByClassName("nav-link");
    var liList = document.getElementsByClassName("nav-item")
    for (var i=0; i<elementsList.length; i++) {
        if (elementsList[i].getAttribute("href") == loc) {
            liList[i].classList += " active"
        }
        if (elementsList[i].className.includes("disabled")) {
            elementsList[i].removeAttribute('href')
        }
    }
</script>