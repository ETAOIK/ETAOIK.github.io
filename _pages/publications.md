---
layout: default
permalink: /publications/
title: "Publications"
author_profile: true
---

<style>
  #main {
    display: flex !important;
    max-width: 1280px;
    margin: 0 auto;
    align-items: flex-start;
  }
  .sidebar {
    width: 260px !important;
    position: sticky;
    top: 2em;
    flex-shrink: 0;
  }
  .page {
    width: calc(100% - 260px) !important;
    padding-left: 40px !important;
    flex-grow: 1;
  }

  .paper-box {
    display: flex;
    margin-bottom: 20px;
    gap: 20px;
    border-bottom: 1px solid #eee;
    padding-bottom: 20px;
  }
  .paper-box-image {
    flex: 0 0 250px;
    position: relative;
  }
  .paper-box-text {
    flex: 1;
    line-height: 1.4;
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
  <h2 class="year" style="margin-top: 30px; border-bottom: 2px solid #333; padding-bottom: 5px; font-size: 1.5em;">{{ year_group.name }}</h2>
  
  {% for entry in year_group.items %}
  <div class="paper-box">
    <div class="paper-box-image">
      {% if entry.badge %}<div class="badge">{{ entry.badge }}</div>{% endif %}
      <img src="{{ entry.image | relative_url }}" style="width: 100%; border-radius: 4px;">
    </div>

    <div class="paper-box-text">
      <p style="margin: 0; font-size: 1.1em; font-weight: bold;">
        <a href="{{ entry.url }}">{{ entry.title }}</a>
      </p>
      
      <div style="margin: 4px 0; color: #444;">
        {{ entry.authors | markdownify | remove: '<p>' | remove: '</p>' }}
      </div>
      
      {% if entry.keywords %}
      <div class="keywords" style="font-size: 0.9em; color: #666; margin-top: 5px;">
        <strong>Keywords:</strong>
        <ul style="margin: 2px 0; padding-left: 18px; list-style-type: disc;">
          {% for kw in entry.keywords %}
          <li style="margin-bottom: 0;">{{ kw }}</li>
          {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
  </div>
  {% endfor %}
{% endfor %}
</div>