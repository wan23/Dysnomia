<html>
  <head>
    <!-- Refresh in case the level was solved -->
    <meta http-equiv="refresh" content="20">
    <title>Abstruse</title>

        <link rel="stylesheet" href="/static/css/normalize.css">
        <link rel="stylesheet" href="/static/css/main.css">
  </head>

  <body>
	<header>

<img class="logo responsive" src="/static/img/logo.png">

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
    LEVEL {{ level.number }}
  </div>
  <div class="question-image">
    <image src="{{ level.image_url }}">
  </div>
  </body>
</html>
