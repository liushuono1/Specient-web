# SpecAgent AI

The official website for **SpecAgent AI**, a platform showcasing "Spec-Driven" intelligent agents. This project utilizes a data-driven architecture where content is decoupled from presentation, powered by Django and Tailwind CSS.

## 🚀 Features

- **Data-Driven Architecture**: Content is stored in JSON files (`hello_world/data/`), acting as a lightweight CMS.
- **Modern UI/UX**: Designed with a "Bento Grid" and "Futuristic/Scientific" style using **Tailwind CSS**.
- **Django 5.x**: Robust backend framework.
- **Easy Content Management**: Update text and structure by editing JSON files without touching HTML.

## 🛠 Tech Stack

- **Backend**: Python 3, Django 5.x
- **Frontend**: Django Templates, Tailwind CSS (via CDN)
- **Data**: JSON-based flat file storage

## 📦 Installation & Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

3. **Run Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the site at `http://localhost:8000`.

## 📂 Project Structure

- `hello_world/core/views.py`: Contains all view logic.
- `hello_world/data/*.json`: Content source files. Edit these to change text/images.
- `hello_world/templates/`: HTML structures extending `base.html`.
- `hello_world/static/`: CSS, JS, and image assets.

## 📝 Developer Workflow

### Updating Content
To update text on the homepage, edit `hello_world/data/home_data.json`. The changes will reflect immediately upon refresh.

### Adding New Pages
1. Create a data file: `hello_world/data/[page_name]_data.json`.
2. Create a template: `hello_world/templates/[page_name].html`.
3. Add a view function in `views.py` using `load_json_data`.
4. Register the URL in `hello_world/urls.py`.

## 🎨 Styling
Tailwind classes are used directly in templates. Configuration is handled in the `<head>` of `base.html`.
Key colors:
- Background: `#FAF8F2` (bg-spec-bg)
- Primary Text: `#1B325F` (text-spec-navy)
- Accent: `#C49A48` (text-spec-earth)

---
*Powered by SpecAgent AI*
