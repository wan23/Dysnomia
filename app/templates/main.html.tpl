<html>
<link rel="stylesheet" href="/static/css/normalize.css">
<link rel="stylesheet" href="/static/css/main.css">
<!-- refresh every 10 seconds to see if games are ready -->
<meta http-equiv="refresh" content="20">

</head>

<body>
<header>

<img class="logo" src="/static/img/logo.png">

	</header>
  <section>
  Hello, {{session['user']}}

  <br/>

    Open Games:
    <table border="1"><tr>
      <th>Game Number</th><th>Viewer</th><th>Typer</th><tr>
      {% for game in games %}
        <tr>
          <td>{{ game.id }}</td>
          <td>
            {% if game.viewer_name %}
              {{ game.viewer_name }}
            {% elif game.typer_name == session['user'] %}
                <span>[Waiting]</span>
            {% else %}
              <form method="POST" action="/joingame">
                <input type="hidden" id="hviewer" name="role" value="viewer">
                <input type="hidden" name="gameid" value="{{ game.id }}">
                <input type="submit" name="submit" text="submit" value="Join"/>
              </form>
            {% endif %}
          </td>
          <td>
            {% if game.typer_name %}
              {{ game.typer_name }}
            {% elif game.viewer_name == session['user'] %}
              <span>[Waiting]</span>
            {% else %}
              <form method="POST" action="/joingame">
                <input type="hidden" id="htyper" name="role" value="typer">
                <input type="hidden" name="gameid" value="{{ game.id }}">
                <input type="submit" name="submit" text="submit" value="Join"/>
              </form>
            {% endif %}
          </td>
          {% if game.typer_name and game.viewer_name and session['user'] == game.typer_name or session['user'] == game.viewer_name %}
            <td><a href="/game/{{ game.id }}">Play Now!</a></td>
          {% endif %}
        </tr>
      {% endfor %}
    </table>
    <hr/>
    <br/>
    Create Game:
    <form method="POST" action="/newgame">
      <input type="radio" id="viewer"
     name="role" value="viewer">
    <label for="viewer">Viewer</label>

    <input type="radio" id="typer"
     name="role" value="typer">
    <label for="typer">Typer</label>
      <input type="submit" name="submit" text="submit" value="submit"/>
    </form>
  </section>
  </body>
</html>
