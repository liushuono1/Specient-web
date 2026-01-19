from django.shortcuts import render, Http404
from hello_world.utils import load_json_data

def get_lang(request):
    lang = request.GET.get('lang')
    if lang:
        request.session['lang'] = lang
    return request.session.get('lang', 'zh')

def index(request):
    lang = get_lang(request)
    data = load_json_data('home_data.json', lang=lang)
    context = {
        "page_data": data,
        "current_lang": lang,
    }
    return render(request, "index.html", context)

def technology(request):
    lang = get_lang(request)
    data = load_json_data('technology_data.json', lang=lang)
    context = {
        "page_data": data,
        "current_lang": lang,
    }
    return render(request, "technology.html", context)


def optimization(request):
    lang = get_lang(request)
    data = load_json_data('optimization_data.json', lang=lang)
    context = {
        "page_data": data,
        "current_lang": lang,
    }
    return render(request, "optimization.html", context)


def solution_detail(request, industry_id):
    lang = get_lang(request)
    filename = f"{industry_id}_data.json"
    data = load_json_data(filename, lang=lang)
    
    if not data:
        raise Http404("Solution not found")
        
    context = {
        "page_data": data,
        "industry_id": industry_id,
        "current_lang": lang,
    }
    return render(request, "solution_detail.html", context)

def portal_login(request):
    lang = get_lang(request)
    data = load_json_data('portal_data.json', lang=lang)
    context = {
        "page_data": data,
        "current_lang": lang,
    }
    return render(request, "portal/login.html", context)

def portal_dashboard(request):
    lang = get_lang(request)
    data = load_json_data('portal_data.json', lang=lang)
    context = {
        "page_data": data,
        "current_lang": lang,
    }
    return render(request, "portal/dashboard.html", context)

def portal_demo(request, industry_id="general"):
    # We can load specific industry data if needed, but for sandbox we stick to generic
    context = {
        "industry_id": industry_id,
    }
    return render(request, "portal/demo.html", context)
