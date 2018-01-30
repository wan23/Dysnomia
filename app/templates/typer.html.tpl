<html>
  <head>
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
   <h2> LEVEL {{ level.number }} </h2>
  </div>
  <div class="question">
    <h1>{{ level.question }}</h1>
  </div>
  <form class="answer" action="/answer" method="POST">
    <input type="text" name="answer" required>
    <input type="hidden" name="game_id" value="{{ game.id }}">
  	<br/>
    <input type="submit" value="submit"/>
  </form>
  <div class="hint">
    Hint: {{ level.hint }}
  </div>
  </body>
</html>
