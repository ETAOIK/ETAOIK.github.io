---
layout: default
permalink: /publications/
title: "Publications"
author_profile: true
---

<style>
  #main {
    display: flex !important;
    flex-direction: row;
    align-items: flex-start;
  }
  .sidebar {
    width: 250px !important;
    min-width: 250px;
  }
  .page {
    flex-grow: 1;
    padding-left: 40px !important;
    width: calc(100% - 250px);
  }
  .masthead__menu-home-item { display: none !important; }
  @media (max-width: 800px) {
    #main { flex-direction: column; }
    .page { width: 100%; padding-left: 0 !important; }
  }
</style>

# 📝 Publications 
(*: equal contribution, ✉: corresponding authors)

<div class="publications">
{% assign publications_by_year = site.data.publications | group_by_exp: "item", "item.year" | sort: "name" | reverse %}
{% for year_group in publications_by_year %}
  <h2 class="year" style="margin-top: 50px; border-bottom: 1px solid #eee; padding-bottom: 10px;">{{ year_group.name }}</h2>
  {% for entry in year_group.items %}
  <div class="paper-box" style="margin-bottom: 20px; display: flex; gap: 20px;">
    {% if entry.image %}
    <div class="paper-box-image" style="width: 30%; min-width: 200px;">
      <div style="position: relative;">
        {% if entry.badge %}<div class="badge" style="position: absolute; top: 0; left: 0;">{{ entry.badge }}</div>{% endif %}
        <img src="{{ entry.image | relative_url }}" alt="paper_image" style="width: 100%; border: 1px solid #eee;">
      </div>
    </div>
    {% endif %}

    <div class="paper-box-text" style="flex: 1;" markdown="1">

[{{ entry.title }}]({{ entry.url }})  
{{ entry.authors }}

**Keywords** {% for kw in entry.keywords %}- {{ kw }}; 
{% endfor %}

    </div>
  </div>
  {% endfor %}
{% endfor %}
</div>