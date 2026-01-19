import os
from django.conf import settings
from hello_world.utils import load_json_data

def global_settings(request):
    """
    Add global settings, ICP info and Common data to the context.
    """
    lang = request.session.get('lang', 'zh')
    common_data = load_json_data('common_data.json', lang=lang)

    icp_file_path = os.path.join(settings.BASE_DIR, 'ICP_BEIAN.txt')
    icp_info = ""
    try:
        with open(icp_file_path, 'r', encoding='utf-8') as f:
            icp_info = f.read()
    except Exception:
        pass
        
    return {
        'icp_info': icp_info,
        'common_data': common_data,
        'current_lang': lang
    }
