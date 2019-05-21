"""occurrences URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from rest_framework import routers
from server import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from server.views import ContatoView, CadastroView



admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'^occurrences', views.OccurrenceViewSet)

from server.views import LoginView

urlpatterns = [
 #   url(r'^', include(router.urls)),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^blog', views.homeBlog, name='blog'),
    url(r'^depoimentos', views.depoimentos, name='depoimentos'),
    url(r'^payment-successful', views.successful, name='payment-successful'),
    url(r'^payment-processing', views.processing, name='payment-processing'),
    url(r'^fale-conosco', ContatoView.as_view(), name='fale-conosco'),
    url(r'^cadastro', CadastroView.as_view(), name='cadastro'),
    url(r'^posts/(?P<post_id>\d+)', views.post),
    url(r'^ckeditor', include('ckeditor_uploader.urls')),
    url(r'^admin', admin.site.urls),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="login"),
    url(r'^test', views.homeBlog),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
