---
layout: archive
title: "Publications"
description: "Publications of Ryoya Ando: refereed papers, preprints, Ph.D. thesis, proceedings and books, mainly on homological algebra over non-Noetherian commutative rings."
permalink: /papers/
---

{% include base_path %}

# Refereed papers

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

# Preprints

{% for post in site.preprints reversed %}
  {% include archive-single.html %}
{% endfor %}


# Thesis

{% for post in site.theses reversed %}
  {% include archive-single.html %}
{% endfor %}


# Miscellaneous

{% for post in site.miscellaneous reversed %}
  {% include archive-single.html %}
{% endfor %}


# Books 

{% for post in site.books reversed %}
  {% include archive-single.html %}
{% endfor %}

