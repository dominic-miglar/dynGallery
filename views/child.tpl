{% extends "base.tpl" %}

{% block head %}
    {{ super() }}
    <script type="text/javascript" src="js/lightbox/js/prototype.js"></script>
    <script type="text/javascript" src="js/lightbox/js/scriptaculous.js?load=effects,builder"></script>
    <script type="text/javascript" src="js/lightbox/js/lightbox.js"></script>
    <link rel="stylesheet" href="js/lightbox/css/lightbox.css" type="text/css" media="screen" />
{% endblock head %}

{% block title %}
	{{ mytitle }}
{% endblock title %}

{% block header %}
	{{ myheader }}
{% endblock header %}

{% block content %}
	{{ mycontent }}
{% endblock content %}

{% block webthumbs %}
    {% for thumb in thumbs %}
        <a href="{{ picDir }}/{{ thumb }}" rel="lightbox[gallery]"><img src="{{ thumbDir }}/{{ thumb }}" /></a>
    {% endfor %}
{% endblock webthumbs %}

{% block footer %}
	{{ myfooter }}
{% endblock footer %}
