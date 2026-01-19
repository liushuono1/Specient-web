# Copilot Instructions for SpecAgent AI (Django)

## 🧠 Project Context & Architecture
You are working on the **SpecAgent AI** official website, a Django-based application designed to showcase "Spec-Driven" AI agents.
- **Core Concept**: The site distinguishes itself with a **Data-Driven Architecture**. Content is decoupled from presentation.
- **Tech Stack**:
    - **Backend**: Django 5.x.
    - **Frontend**: Django Templates + Tailwind CSS (via CDN).
    - **Data**: JSON files in `hello_world/data/` act as a lightweight CMS.

## 📂 Code Structure & Key Paths
- **Views & Logic**: `hello_world/core/views.py` (Contains all view logic).
- **URLs**: `hello_world/urls.py`.
- **Content Data**: `hello_world/data/*.json` (Edit these for text/content changes).
- **Templates**: `hello_world/templates/` (HTML structure).
    - `base.html`: Contains the Tailwind configuration and global layout.
- **Static Assets**: `hello_world/static/` (CSS/JS/Images).
- **Utilities**: `hello_world/utils.py` (Helper functions like `load_json_data`).

## 🛠 Developer Workflow

### 1. Running the Server
```bash
python manage.py runserver
```
Note: access the site via the forwarded port 8000. Codespaces CSRF mapping is pre-configured in `settings.py`.

### 2. Adding New Pages
1.  **Create Data**: Add `[page_name]_data.json` in `hello_world/data/`.
2.  **Create Template**: Add HTML file in `hello_world/templates/` extending `base.html`.
3.  **Define View**: Add function in `hello_world/core/views.py` using `load_json_data`.
4.  **Map URL**: Add entry in `hello_world/urls.py`.

### 3. Styling Paradigm
- **Tailwind CSS**: Use utility classes directly in templates.
- **Configuration**: Tailwind config is located in the `<head>` of `base.html`.
- **Custom Colors**:
    - `bg-spec-bg` (Background: #FAF8F2)
    - `text-spec-navy` (Primary Text: #1B325F)
    - `text-spec-earth` (Accent: #C49A48)
- **Design Style**: "Bento Grid", "Futuristic/Scientific", "Clean".

## 📝 Coding Conventions

### Content Management
**DO NOT** hardcode text content in HTML templates.
- **Correct**: `<h1>{{ page_data.hero.title }}</h1>`
- **Incorrect**: `<h1>SpecDriver Intelligent Agents</h1>`
- Always verify the JSON structure in `hello_world/data/` matches the template variable access.

### View Logic
- Use `load_json_data(filename)` helper in strict `try/except` blocks (handled inside the util) to safely load content.
- Pass `page_data` context variable to templates.
- For dynamic industry solutions, use the `industry_id` pattern seen in `solution_detail` view.

### Frontend
- All templates must extend `base.html`.
- Use `{% block content %}` for unique page content.
- Use `{% static 'path/to/asset' %}` for images/styles.

## ⚠️ Critical Dependencies
- **Tailwind CDN**: The site relies on the script tag in `base.html`. There is no `node_modules` or `npm build`.
- **Browser Reload**: `django_browser_reload` is installed for DX.

## 🔍 Common Tasks
- **Update Homepage Text**: Edit `hello_world/data/home_data.json`.
- **Add Industry Solution**: Create `hello_world/data/[industry]_data.json` and ensure a link exists in `home_data.json` or navigation.
