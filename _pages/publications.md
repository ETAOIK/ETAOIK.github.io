---
layout: default
permalink: /publications/
title: "Publications"
author_profile: true
---

<style>
  #main {
    display: flex !important;
    max-width: 1200px;
    margin: 0 auto;
    align-items: flex-start;
  }
  .sidebar {
    width: 260px !important;
    position: sticky;
    top: 2em;
  }
  .page {
    width: calc(100% - 260px) !important;
    padding-left: 40px !important;
    flex-shrink: 1;
  }


  .paper-box {
    display: flex;
    margin-bottom: 40px;
    gap: 25px;
    border-bottom: 1px solid #f2f2f2;
    padding-bottom: 20px;
  }
  .paper-box-image {
    flex: 0 0 300px;
    position: relative;
  }
  .paper-box-text {
    flex: 1;
  }
  .badge {
    background: #004085;
    color: white;
    padding: 2px 8px;
    font-size: 12px;
    border-radius: 3px;
    position: absolute;
    top: 5px;
    left: 5px;
    z-index: 10;
  }
  
  @media (max-width: 768px) {
    #main { flex-direction: column; }
    .sidebar, .page { width: 100% !important; padding: 10px !important; }
    .paper-box { flex-direction: column; }
  }
</style>

# 📝 Publications 
(*: equal contribution, ✉: corresponding authors)

<div class="publications">
{% assign publications_by_year = site.data.publications | group_by_exp: "item", "item.year" | sort: "name" | reverse %}
{% for year_group in publications_by_year %}
  <h2 class="year" style="margin-top: 40px; border-bottom: 2px solid #333; padding-bottom: 5px;">{{ year_group.name }}</h2>
  
  {% for entry in year_group.items %}
  <div class="paper-box">
    <div class="paper-box-image">
      {% if entry.badge %}<div class="badge">{{ entry.badge }}</div>{% endif %}
      <img src="{{ entry.image | relative_url }}" style="width: 100%; border-radius: 4px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
    </div>

    <div class="paper-box-text">
      <p style="margin: 0; font-size: 1.1em; font-weight: bold;">
        <a href="{{ entry.url }}">{{ entry.title }}</a>
      </p>
      <p style="margin: 5px 0; color: #555;">{{ entry.authors }}</p>
      
      {% if entry.keywords %}
      <div class="keywords" style="font-size: 0.9em; color: #666;">
        <strong>Keywords:</strong>
        <ul style="margin: 5px 0; padding-left: 20px;">
          {% for kw in entry.keywords %}
          <li>{{ kw }}</li>
          {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
  </div>
  {% endfor %}
{% endfor %}
</div>