---
layout: default
title: Publications
permalink: /publications/
author_profile: true
---

# 📝 Publications 
(*: equal contribution, ✉: corresponding authors)

<div class="publications">
  {% assign publications_by_year = site.data.publications | group_by_exp: "item", "item.year" | sort: "name" | reverse %}
  
  {% for year_group in publications_by_year %}
    <h2 class="year" style="margin-top: 50px; border-bottom: 1px solid #eee; padding-bottom: 10px;">{{ year_group.name }}</h2>
    
    {% for entry in year_group.items %}
    <div class='paper-box'>
      
      {% if entry.image %}
      <div class='paper-box-image'>
        <div>
          {% if entry.badge %}<div class="badge">{{ entry.badge }}</div>{% endif %}
          <img src='{{ entry.image | relative_url }}' alt="paper_image" width="100%">
        </div>
      </div>
      {% endif %}

      <div class='paper-box-text' {% unless entry.image %}style="width: 100%; margin-left: 0;"{% endunless %} markdown="1">
[{{ entry.title }}]({{ entry.url }})
{{ entry.authors }}

{% if entry.keywords %}
**Keywords**
{% for kw in entry.keywords %}
- {{ kw }}; 
{% endfor %}
{% endif %}
      </div>
    </div>
    {% endfor %}

  {% endfor %}
</div>