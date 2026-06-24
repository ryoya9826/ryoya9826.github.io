---
layout: archive
title: "Publications"
permalink: /papers/
last_modified_at: 2026-04-21
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

