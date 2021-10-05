---
layout: archive
title: "Papers"
permalink: /papers/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

# Publications (Refereed)

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

# Preprints

{% for post in site.preprints reversed %}
  {% include archive-single.html %}
{% endfor %}

