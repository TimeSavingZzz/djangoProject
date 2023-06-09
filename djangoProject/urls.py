"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from app01.views import views, activity
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', views.admin),
    path('contribute/list/', views.contribute_list),
    path('user/', views.user),
    path('login/', views.login),
    path('logout/', views.logout),
    path('activity/', activity.add_activity),
    path('update_opportunity/', views.update_opportunity, name='update_opportunity'),
    path('mining/', views.mining),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
