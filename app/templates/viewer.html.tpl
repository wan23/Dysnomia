<html>
  <head>
    <!-- Refresh in case the level was solved -->
    <meta http-equiv="refresh" content="20">
    <title>Abstruse</title>

        <link rel="stylesheet" href="/static/css/normalize.css">
        <link rel="stylesheet" href="/static/css/main.css">
  </head>

  <body class="game">
	<header>

<img class="logo" src="/static/img/logo.png">

	</header>
  {% with messages = get_flashed_messages() %}
    {% if messages %}
      <ul class=flashes>
      {% for message in messages %}
        <li>{{ message }}</li>
      {% endfor %}
      </ul>
    {% endif %}
  {% endwith %}
  <div class='level-display'>
   <h2> LEVEL {{ level.number }}</h2>
  </div>
  <div class="question-image">
    <image class="responsive" src="{{ level.image_url }}">
  </div>
  </body>
</html>
