<DOCTYPE html>

<html>
	<head>
        {% block head %}
		<title>{% block title %}{% endblock title %} - Gallery</title>
		<link rel="stylesheet" type="text/css" href="styles/default.css" />
        {% endblock head %}
	</head>
	
	
    <body>
		<div id="header">
            <h2>{% block header %}no header specified{% endblock header %}</h2>
        </div>
		<div id="container">
            <p>{% block content %}no content specified{% endblock content %}</p>
            <ul>{% block webthumbs %}<li>nothing here</li>{% endblock webthumbs %}</ul>
        </div>
		<div id="footer">
            <p>{% block footer %}no footer specified{% endblock footer %}</p>
        </div>
	</body>
</html>
