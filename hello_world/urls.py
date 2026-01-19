"""
URL configuration for hello_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views

urlpatterns = [
    path("", core_views.index, name="home"),
    path("technology/", core_views.technology, name="technology"),
    path("optimization/", core_views.optimization, name="optimization"),
    path("solutions/<str:industry_id>/", core_views.solution_detail, name="solution_detail"),
    path("portal/login", core_views.portal_login, name="login"),
    path("portal/dashboard", core_views.portal_dashboard, name="dashboard"),
    path("portal/demo/<str:industry_id>", core_views.portal_demo, name="demo"),
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
