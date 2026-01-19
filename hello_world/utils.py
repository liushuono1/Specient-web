import json
import os
from django.conf import settings

def load_json_data(filename, lang='zh'):
    """
    Load JSON data from the hello_world/data directory.
    If lang is provided and not 'zh', try to load the localized version first.
    e.g. filename='home_data.json', lang='en' -> try 'home_data_en.json'
    """
    if lang and lang != 'zh':
        name_part, ext_part = os.path.splitext(filename)
        localized_filename = f"{name_part}_{lang}{ext_part}"
        localized_path = os.path.join(settings.BASE_DIR, 'hello_world', 'data', localized_filename)
        if os.path.exists(localized_path):
            filename = localized_filename

    file_path = os.path.join(settings.BASE_DIR, 'hello_world', 'data', filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
