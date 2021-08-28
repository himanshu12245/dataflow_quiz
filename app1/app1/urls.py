"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include 
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from quiz import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view(),name='logout'),
    # path('home/',views.set_main,name="home"),
    path('issue/',views.set_issue,name="issue"),
    path('home/',views.HomeView.as_view(),name="home"),
    path('comment/',views.AddCommentView.as_view(),name="comment"),
    path('export/',views.export,name='export'),
    path('issue/home/',views.HomeView.as_view(),name="home"),
    path('edit/<int:pk>',views.Updateissue.as_view(),name='update_issue'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
